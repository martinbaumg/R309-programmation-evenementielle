import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QMainWindow, QGridLayout, QLabel, QLineEdit, QComboBox

# Une fenêtre qui convertit des degrés en kelvin

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma première fenêtre")
        self.resize(300, 100)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel("Degrés : ")
        self.label2 = QLabel("°C")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Convertir")
        self.button.clicked.connect(self.valider)
        self.text = QLabel("")
        self.quit = QPushButton("Quitter")
        self.quit.clicked.connect(self.__actionQuitter)
        self.button2 = QPushButton("Aide")
        # mettre un menu déroulant avec degré et kelvin
        self.menu = QComboBox()
        self.menu.addItem("°C -> K")
        self.menu.addItem("K -> °C")

        # en fonction de ce qu'on a choisi, la conversion change
        self.menu.currentIndexChanged.connect(self.validation)

        # une fenêtre apparaît quand on clique sur le bouton aide
        self.button2.clicked.connect(self.aide)




        

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line_edit, 0, 1)
        layout.addWidget(self.button, 1, 0, 1, 2)
        layout.addWidget(self.text, 2, 0, 1, 2)
        layout.addWidget(self.quit, 3, 0, 1, 2)
        layout.addWidget(self.label2, 0, 2)
        layout.addWidget(self.menu, 0, 3)
        layout.addWidget(self.button2, 1, 3)    


        self.setLayout(layout)

    def aide(self):
        QMessageBox.information(self, "Aide", "Entrez un nombre de degrés et cliquez sur convertir")


    def validation(self):
        # verification que le nombre écrit est positif 
        if self.line_edit.text() != "-1":
            degres = self.line_edit.text()
            kelvin = float(degres) - 273.15
            self.text.setText(f"{kelvin} °C")
            self.label2.setText("K")
        else:
            QMessageBox.critical(self, "Erreur", "Entrez un nombre positif")
    


    def valider(self):
        try:
            degres = self.line_edit.text()
            kelvin = float(degres) + 273.15
            self.text.setText(f"{kelvin} K")
            self.label2.setText("°C")
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Entrez un nombre")
        

    def __actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
