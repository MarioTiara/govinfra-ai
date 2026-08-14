import re


class TextCleaner:
    def clean(self, text: str, unwanthedpatterns:list[str] | None=None) -> str:
        if not text:
            return ""

        text = self._remove_excessives_whitespace(text)
        text=self._normalize_newlines(text)
        if unwanthedpatterns :
            text=self._remove_unwanted_text(text, unwanthedpatterns)

        return text.strip()

    def _remove_unwanted_text(self, text:str, unwanted_patterns:list[str])-> str:
        for pattern in unwanted_patterns:
            text= re.sub(pattern,"",text)

        return text
    
    def _remove_control_characters(self, text: str) -> str:
        return "".join(
            char
            for char in text
            if char == "\n" or char == "\t" or not char.isprintable()
        )

    def _remove_excessives_whitespace(self, text: str) -> str:
        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove spaces before newline
        text = re.sub(r" +\n", "\n", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove excessive spaces
        text = re.sub(r" {2,}", " ", text)

        return text

    def _normalize_newlines(self,text: str) -> str:
        if not text:
            return ""
        
        # 1. Hapus kata terpotong tanda hubung (misal: "mem- \n buat" -> "membuat")
        text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
        
        # 2. Hapus \n HANYA jika karakter SEBELUMNYA BUKAN titik (.), titik koma (;), atau titik dua (:)
        #    dan BUKAN newline ganda (paragraf baru).
        text = re.sub(r'(?<=[^;\.\:\n])\n(?=[^\n])', ' ', text)
        
        # 3. Rapikan spasi berlebih
        text = re.sub(r'[ \t]+', ' ', text)
        
        return text.strip()

