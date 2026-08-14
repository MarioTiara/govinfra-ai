import re

from document_processing.models.document_node import DocumentNode


class StructureDetector:
    SECTION_PATTERNS = {
        "menimbang": re.compile(r"^\s*Menimbang:\s*$", re.I),
        "mengingat": re.compile(r"^\s*Mengingat:\s*$", re.I),
        "memutuskan": re.compile(r"^\s*MEMUTUSKAN:\s*$", re.I),
        "menetapkan": re.compile(r"^\s*Menetapkan:\s*$", re.I),
    }
    BAB_PATTERN = re.compile(
        r"^\s*BAB\s+([IVXLCDM]+)\s*(.*)$",
        re.IGNORECASE
    )

    PASAL_PATTERN = re.compile(
        r"^\s*Pasal\s+(\d+)\s*$",
        re.IGNORECASE
    )

    AYAT_PATTERN = re.compile(
        r"^\s*\((\d+)\)\s*(.*)$"
    )

    HURUF_PATTERN = re.compile(
        r"^\s*([a-z])\.\s*(.*)$"
    )

    def detect(self, text: str) -> list[DocumentNode]:
        if not text:
            return []

        nodes = []

        for line in text.splitlines():
            line = line.strip()

            if not line:
                continue

            node = self.detect_line(line)

            if node:
                nodes.append(node)

        return nodes

    def detect_line(self, line: str) -> DocumentNode | None:

        # Section
        section = self._detect_section(line)

        if section:
            return section
        
        match = self.BAB_PATTERN.match(line)

        if match:
            return DocumentNode(
                type="bab",
                number=match.group(1),
                title=match.group(2).strip() or None
            )

        match = self.PASAL_PATTERN.match(line)

        if match:
            return DocumentNode(
                type="pasal",
                number=match.group(1)
            )

        match = self.AYAT_PATTERN.match(line)

        if match:
            return DocumentNode(
                type="ayat",
                number=match.group(1),
                text=match.group(2)
            )

        match = self.HURUF_PATTERN.match(line)

        if match:
            return DocumentNode(
                type="huruf",
                number=match.group(1),
                text=match.group(2)
            )

        return None

    
    def _detect_section(self, line: str) -> DocumentNode | None:
        for section_type, pattern in self.SECTION_PATTERNS.items():
            if pattern.match(line):
                return DocumentNode(
                    type=section_type
                )

        return None