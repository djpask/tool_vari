import PyPDF2
import json

def pdf_to_json(pdf_path, json_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        document = {"Document": []}

        for page_num, page in enumerate(reader.pages):
            page_dict = {"Page": page_num + 1, "Lines": []}
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    page_dict["Lines"].append(line)
            document["Document"].append(page_dict)

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(document, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pdf_path = "esempio.pdf"
    json_path = "esempio.json"

    pdf_to_json(pdf_path, json_path)

    print(f"File PDF convertito in JSON e salvato in {json_path}")