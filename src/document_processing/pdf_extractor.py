from dataclasses import dataclass
from pathlib import Path

import fitz


@dataclass
class ExtractedPage:
    page_number: int
    text: str


class PdfExtractor:
    def extract(self, file_path: str | Path) -> list[ExtractedPage]:
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"PDF file not found: {file_path}"
            )

        if file_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Expected a PDF file, got: {file_path.suffix}"
            )

        pages: list[ExtractedPage] = []

        with fitz.open(file_path) as document:
            for page_number, page in enumerate(document, start=1):
                text = page.get_text("text")
                print(text)
                pages.append(
                    ExtractedPage(
                        page_number=page_number,
                        text=text,
                    )
                )

        return pages