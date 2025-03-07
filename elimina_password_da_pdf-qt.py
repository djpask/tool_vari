import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
import PyPDF2

class PDFPasswordRemover(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rimuovi Password da PDF')

        layout = QVBoxLayout()

        self.label = QLabel('Inserisci la password del PDF:')
        layout.addWidget(self.label)

        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_entry)

        self.remove_button = QPushButton('Seleziona PDF e Rimuovi Password')
        self.remove_button.clicked.connect(self.remove_password)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def remove_password(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleziona PDF", "", "PDF files (*.pdf)")
        if not file_path:
            return

        password = self.password_entry.text()
        if not password:
            QMessageBox.critical(self, "Errore", "Inserisci la password del PDF.")
            return

        try:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                if reader.is_encrypted:
                    reader.decrypt(password)
                    writer = PyPDF2.PdfWriter()
                    for page_num in range(len(reader.pages)):
                        writer.add_page(reader.pages[page_num])

                    output_path, _ = QFileDialog.getSaveFileName(self, "Salva PDF", "", "PDF files (*.pdf)")
                    if output_path:
                        with open(output_path, "wb") as output_file:
                            writer.write(output_file)
                        QMessageBox.information(self, "Successo", "La password è stata rimossa con successo.")
                else:
                    QMessageBox.information(self, "Informazione", "Il file PDF non è protetto da password.")
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFPasswordRemover()
    ex.show()
    sys.exit(app.exec_())