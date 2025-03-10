import PyPDF2
import xml.etree.ElementTree as ET

def pdf_to_xml(pdf_path, xml_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        root = ET.Element("Document")

        for page_num, page in enumerate(reader.pages):
            page_element = ET.SubElement(root, "Page", number=str(page_num + 1))
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    line_element = ET.SubElement(page_element, "Line")
                    line_element.text = line

        tree = ET.ElementTree(root)
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    pdf_path = "esempio.pdf"
    xml_path = "esempio.xml"

    pdf_to_xml(pdf_path, xml_path)

    print(f"File PDF convertito in XML e salvato in {xml_path}")