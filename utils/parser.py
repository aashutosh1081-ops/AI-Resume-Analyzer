import pdfplumber
from docx import Document


def extract_text(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    elif file_path.endswith(".docx"):

        document = Document(file_path)

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

    return text