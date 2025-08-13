import pypdf
import os

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return f"Error extracting text: {e}"

pdf_path = os.path.join(os.getcwd(), 'LinkedIn Profile Analyzer - Product Requirements Document.pdf')
print(extract_text_from_pdf(pdf_path))
