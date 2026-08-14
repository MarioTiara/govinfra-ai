import re


class TextNormalizer:

    def normalize(self, text: str) -> str:
        if not text:
            return ""

        text = self._normalize_article_paragraph(text)
        text = self._normalize_letter_items(text)
        text= self._normalize_subpoint(text)
        # text = self._normalize_newlines(text)

        return text.strip()

    def _normalize_article_paragraph(self, text: str) -> str:
        """
        Separates article number from paragraph number.

        Example:
            Pasal 15 (1) Jembatan ...
        
        Becomes:
            Pasal 15
            (1) Jembatan ...
        """
        pattern = r'\b(Pasal\s+\d+)\s+(\(\d+\))'
        return re.sub(pattern, r'\1\n\2', text)

    def _normalize_letter_items(self, text: str) -> str:
        """
        Separates consecutive lettered items.

        Example:
            a. foo; dan b. bar.
        
        Becomes:
            a. foo; dan
            b. bar.
        """
        pattern = r'([;,.])\s+(dan\s+)?([a-z])\.'
        return re.sub(
            pattern,
            lambda m: f"{m.group(1)} {m.group(2) or ''}\n{m.group(3)}.",
            text
        )
    
    def _normalize_subpoint(self, text: str) -> str:
        """
        Joins a subpoint marker with its following text.

        Example:
            a.
            kecepatan rencana;

        Becomes:
            a. kecepatan rencana;
        """

        pattern = r'(?m)^(\s*[a-z])\.\s*\n\s*([^\n]+)'

        return re.sub(
            pattern,
            r'\1. \2',
            text
        )

    def _normalize_newlines(self, text: str) -> str:
        """
        Removes excessive blank lines.
        """
        text = re.sub(r'\n[ \t]+', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text