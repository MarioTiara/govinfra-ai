from document_processing.pdf_extractor import PdfExtractor
from document_processing.text_cleaner import TextCleaner


PDF_PATH = "..\documents/raw/2023pmpupr5.pdf"

unwantedpatterns = [
    r"-\s*\d+\s*-",
    r"jdih\.pu\.go\.id"
]
def main():
    extractor = PdfExtractor()
    cleaner = TextCleaner()

    pages = extractor.extract(PDF_PATH)

    for page in pages:
        clean_text = cleaner.clean(page.text,unwantedpatterns)

        # if (page.page_number>20):
        #     break
        
        print("=" * 80)
        print(f"PAGE {page.page_number}")
        print("=" * 80)
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(f"{clean_text}\n")
        print(clean_text)


if __name__ == "__main__":
    main()