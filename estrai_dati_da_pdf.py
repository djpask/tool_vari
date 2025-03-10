import PyPDF2
import re
import pandas as pd

def extract_data_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    data = {
        "paga base": extract_value(text, r"IMPONIBILE INAIL\s*([\d,]+)"), #LAVORO ORDINARIO (giorni)
        "accantonamento premio ris. 2025": extract_value(text, r"AC\.MENS\. PREMIO RIS\. 2025:\s*([\d,]+)"),
        "rata addizionale reg. A.P.": extract_value(text, r"RATA ADDIZ\.REGIONALE A\.P\.\s*([\d,]+)")
    }

    return data

def extract_value(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def save_data_to_excel(data, excel_path):
    df = pd.DataFrame([data])
    df.to_excel(excel_path, index=False)

if __name__ == "__main__":
    pdf_path = "esempio.pdf"
    excel_path = "dati_estratti.xlsx"

    data = extract_data_from_pdf(pdf_path)
    save_data_to_excel(data, excel_path)

    print(f"Dati estratti e salvati in {excel_path}")