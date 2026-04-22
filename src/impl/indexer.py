import re
from typing import List
from interface.base_datastore import DataItem
from interface.base_indexer import BaseIndexer


class Indexer(BaseIndexer):
    def index(self, document_paths: List[str]) -> List[DataItem]:
        items = []
        for path in document_paths:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            items.extend(self._chunk_markdown(content, path))
        return items

    def _chunk_markdown(self, content: str, source_path: str) -> List[DataItem]:
        current_h1 = ""
        current_h2 = ""
        chunks = re.split(r'\n(?=#{1,3} )', content)
        items = []

        for i, chunk in enumerate(chunks):
            chunk = chunk.strip()
            if not chunk:
                continue

            if chunk.startswith("# "):
                current_h1 = chunk.splitlines()[0].lstrip("# ").strip()
                continue

            if chunk.startswith("## "):
                current_h2 = chunk.splitlines()[0].lstrip("# ").strip()
                continue

            if chunk.startswith("### "):
                context = ", ".join(filter(None, [current_h1, current_h2]))
                full_text = f"## {context}\n{chunk}" if context else chunk
                items.append(DataItem(content=full_text, source=f"{source_path}:{i}"))

        return items