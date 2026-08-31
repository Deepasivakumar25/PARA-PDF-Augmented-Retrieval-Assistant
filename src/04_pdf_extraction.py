from pypdf import PdfReader

reader = PdfReader("Visit-visa-checklist-Nov-2022.pdf")
pdf_text = ""

for page in reader.pages:
    pdf_text += page.extract_text()
