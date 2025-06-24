from pypdf import PdfReader


def load_text_or_pdf(path: str) -> str:
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
