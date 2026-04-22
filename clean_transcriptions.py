"""
Cleans and structures GT Sistemas ERP video transcriptions for better RAG retrieval.

Converts noisy spoken Portuguese into structured topical ### sections so Docling's
HybridChunker produces semantically coherent chunks instead of random text slices.

Usage:
    python clean_transcriptions.py

Output: sample_data/source/playlist_rag_clean.md
Then re-index:
    python main.py reset
    python main.py add -p sample_data/source/playlist_rag_clean.md
"""

import os
import re
import sys
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SYSTEM_PROMPT = """Você é um especialista no ERP GT Sistemas.
Você recebe o título e a transcrição de um vídeo tutorial em português brasileiro informal (fala corrida, sem pontuação).

Sua tarefa:
1. Identifique 2 a 5 tópicos distintos abordados no vídeo.
2. Para cada tópico, crie uma seção markdown com heading ### [Nome do Tópico].
3. Dentro de cada seção, reescreva o conteúdo em português escrito correto e conciso.
4. Preserve todos os detalhes técnicos (nomes de campos, menus, módulos, documentos fiscais, etc.).
5. Remova apenas palavras de preenchimento: "tá", "né", "aqui" repetido, "aí" repetido, "então" repetido, "beleza", "certo" como pausa.
6. Não invente informações que não estejam na transcrição.
7. Retorne APENAS o markdown com as seções ###, sem texto introdutório, sem comentários."""


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrado. Configure o arquivo .env")
    return OpenAI(api_key=api_key)


def clean_transcription(client: OpenAI, title: str, transcription: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Título do vídeo: {title}\n\nTranscrição:\n{transcription}"},
        ],
        temperature=0.1,
    )
    return response.choices[0].message.content.strip()


def parse_video_sections(content: str) -> tuple[str, list[dict]]:
    """Split the markdown into the file header and a list of video section dicts."""
    parts = content.split("\n---\n")
    header = parts[0].strip()
    sections = []

    for raw in parts[1:]:
        raw = raw.strip()
        if not raw:
            continue

        # Title: ## N. Title
        title_match = re.search(r'^(## .+)$', raw, re.MULTILINE)
        if not title_match:
            continue
        title = title_match.group(1)

        # Metadata table (lines between title and first ###)
        meta_match = re.search(
            r'^## .+\n\n((?:\|.+\n?)+)', raw, re.MULTILINE
        )
        metadata = meta_match.group(1).strip() if meta_match else ""

        # Tags from metadata (useful to keep as context)
        tags_match = re.search(r'\*\*Tags\*\*\s*\|\s*(.+)', raw)
        tags_line = f"**Tags:** {tags_match.group(1).strip()}" if tags_match else ""

        # Transcription text
        trans_match = re.search(r'### Transcrição\n\n(.+?)$', raw, re.DOTALL)
        transcription = trans_match.group(1).strip() if trans_match else ""

        if not transcription:
            continue

        sections.append({
            "title": title,
            "metadata": metadata,
            "tags_line": tags_line,
            "transcription": transcription,
        })

    return header, sections


def build_section(title: str, tags_line: str, cleaned: str) -> str:
    """Rebuild a video section with cleaned topical subsections."""
    lines = [title, ""]
    if tags_line:
        lines += [tags_line, ""]
    lines += cleaned.splitlines()
    return "\n".join(lines)


def main():
    input_path = "sample_data/source/playlist_rag.md"
    output_path = "sample_data/source/playlist_rag_clean.md"

    if not os.path.exists(input_path):
        print(f"❌ Arquivo não encontrado: {input_path}")
        sys.exit(1)

    print(f"📖 Lendo {input_path}...")
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("🔍 Parseando seções...")
    header, sections = parse_video_sections(content)
    print(f"✅ {len(sections)} seções encontradas\n")

    client = get_client()
    cleaned_sections = []
    errors = 0

    for i, sec in enumerate(sections):
        title_text = sec["title"].replace("## ", "")
        print(f"[{i+1:02d}/{len(sections)}] {title_text[:65]}...")

        try:
            cleaned = clean_transcription(client, title_text, sec["transcription"])
            rebuilt = build_section(sec["title"], sec["tags_line"], cleaned)
            cleaned_sections.append(rebuilt)
        except Exception as e:
            print(f"         ⚠️  Erro: {e} — mantendo original")
            cleaned_sections.append(
                build_section(sec["title"], sec["tags_line"], sec["transcription"])
            )
            errors += 1

        # Avoid rate limiting
        if (i + 1) % 15 == 0:
            time.sleep(2)

    separator = "\n\n---\n\n"
    output = header + separator + separator.join(cleaned_sections) + "\n"

    print(f"\n📝 Salvando em {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n✅ Concluído! {len(cleaned_sections) - errors}/{len(cleaned_sections)} seções limpas.")
    if errors:
        print(f"⚠️  {errors} seções mantiveram o texto original (erro na API).")
    print("\nPróximos passos:")
    print("  python main.py reset")
    print("  python main.py add -p sample_data/source/playlist_rag_clean.md")


if __name__ == "__main__":
    main()
