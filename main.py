import sys
import random
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonRezerwuj.clicked.connect(self.specjalizacja)
        self.show()


    def specjalizacja(self):
        text =''
        price = 0
        days = 0
        if self.ui.radioButtonInternista.isChecked():
            text = self.ui.radioButtonInternista.text()
        if self.ui.radioButton_2Pediatra.isChecked():
            text = self.ui.radioButton_2Pediatra.text()
        if self.ui.radioButton_3Dermatolog.isChecked():
            text = self.ui.radioButton_3Dermatolog.text()

        if self.ui.checkBoxRodzajWizyty.isChecked():
            price = 200
            days = random.randint(1, 14)
        else:
            price = 0
            days = random.randint(1, 1000)

        self.ui.result.setText(f'pomyslnie zarezerwowano wizyte u lekarza: {text}. Termin wizyty przypada za {days} dni, Koszt wizyty: {price} zl')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())