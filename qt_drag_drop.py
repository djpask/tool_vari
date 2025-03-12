import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Drag and Drop Example')

        layout = QVBoxLayout()

        self.label = QLabel('Trascina qui un file:')
        layout.addWidget(self.label)

        self.drop_area = QPlainTextEdit()
        self.drop_area.setReadOnly(True)
        self.drop_area.setAcceptDrops(True)
        self.drop_area.setStyleSheet("background-color: lightgray;")
        layout.addWidget(self.drop_area)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                self.drop_area.setPlainText(f"File dropped: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DragDropWidget()
    ex.show()
    sys.exit(app.exec_())