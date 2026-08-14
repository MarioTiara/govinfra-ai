import json

import camelot

from document_processing.models.document_node import DocumentNode
from document_processing.pdf_extractor import PdfExtractor
from document_processing.structure_builder import StructureBuilder
from document_processing.text_cleaner import TextCleaner
from document_processing.text_normalizer import TextNormalizer
from document_processing.structure_detector import StructureDetector

PDF_PATH = "..\documents/raw/2023pmpupr5.pdf"

unwantedpatterns = [
    r"-\s*\d+\s*-",
    r"jdih\.pu\.go\.id"
]

def print_tree(
    node: DocumentNode,
    level: int = 0
):
    indent = "    " * level

    label = node.type

    if node.number:
        label += f" {node.number}"

    if node.title:
        label += f" - {node.title}"

    if node.text:
        label += f": {node.text[:100]}"

    print(f"{indent}{label}")

    for child in node.children:
        print_tree(
            child,
            level + 1
        )      


def write_tree(
    node: DocumentNode,
    file,
    level: int = 0
):
    indent = "    " * level

    label = node.type

    if node.number:
        label += f" {node.number}"

    if node.title:
        label += f" - {node.title}"

    if node.text:
        label += f": {node.text}"

    file.write(f"{indent}{label}\n")

    for child in node.children:
        write_tree(
            child,
            file,
            level + 1
        )

def main():

    structure_detector = StructureDetector()
    structure_builder = StructureBuilder()

    extractor = PdfExtractor()
    cleaner = TextCleaner()
    normalizer = TextNormalizer()

    pages = extractor.extract(PDF_PATH)

    all_nodes = []

    with open("normalized.txt", "w", encoding="utf-8") as normalized_file:

        for page in pages:

            clean_text = cleaner.clean(
                page.text,
                unwantedpatterns
            )

            normalized_text = normalizer.normalize(
                clean_text
            )

            # Save normalized text
            normalized_file.write(
                normalized_text
            )
            normalized_file.write("\n\n")

            # Detect structure
            nodes = structure_detector.detect(
                normalized_text
            )

            all_nodes.extend(nodes)

    # Build document tree
    document = structure_builder.build(
        all_nodes
    )

    # Convert tree → dictionary
    document_dict = document.to_dict()

    # Save dictionary → JSON
    with open(
        "structured.json",
        "w",
        encoding="utf-8"
    ) as structured_file:

        json.dump(
            document_dict,
            structured_file,
            ensure_ascii=False,
            indent=4
        )


if __name__ == "__main__":
    main()