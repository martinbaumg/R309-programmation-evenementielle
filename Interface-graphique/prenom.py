import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QMainWindow, QGridLayout, QLabel, QLineEdit

# Une fenêtre qui nous demande un prénom

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma première fenêtre")
        self.resize(300, 100)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel("Prénom : ")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Valider")
        self.button.clicked.connect(self.valider)
        self.text = QLabel("")
        self.quit = QPushButton("Quitter")
        self.quit.clicked.connect(self.__actionQuitter)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line_edit, 0, 1)
        layout.addWidget(self.button, 1, 0, 1, 2)
        layout.addWidget(self.text, 2, 0, 1, 2)
        layout.addWidget(self.quit, 3, 0, 1, 2)

        self.setLayout(layout)

    def valider(self):
        prenom = self.line_edit.text()
        self.text.setText(f"Bonjour {prenom} !")
    def __actionQuitter(self):
        QCoreApplication.exit(0)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

