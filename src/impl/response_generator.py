from typing import List
from interface.base_response_generator import BaseResponseGenerator
from util.invoke_ai import invoke_ai


SYSTEM_PROMPT = """
Você é um assistente especializado no ERP GT Sistemas.
Use o contexto fornecido para responder à pergunta do usuário em português.
O contexto é composto por transcrições de vídeos tutoriais em português brasileiro informal.
Se a resposta não estiver no contexto, diga que não encontrou a informação.
Não invente informações.
"""


class ResponseGenerator(BaseResponseGenerator):
    def generate_response(self, query: str, context: List[str]) -> str:
        """Generate a response using OpenAI's chat completion."""
        # Combine context into a single string
        context_text = "\n".join(context)
        user_message = (
            f"<context>\n{context_text}\n</context>\n"
            f"<question>\n{query}\n</question>"
        )

        return invoke_ai(system_message=SYSTEM_PROMPT, user_message=user_message)
