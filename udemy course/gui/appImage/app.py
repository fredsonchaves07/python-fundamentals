import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from design import Ui_MainWindow


class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChoiceFile.clicked.connect(self.open_img)
        self.btnResize.clicked.connect(self.resize_img)
        self.btnSave.clicked.connect(self.save)

    def open_img(self):
        img, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            '/home/fredsonchaves07/Imagens',
            options=QFileDialog.DontUseNativeDialog
        )

        self.inputOpenFile.setText(img)
        self.original_img = QPixmap(img)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def resize_img(self):
        width = int(self.inputLargura.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_img)
        self.inputLargura.setText(str(self.new_img.width()))
        self.inputAltura.setText(str(self.new_img.height()))
    
    def save(self):
        img, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Abrir imagem',
            '/home/fredsonchaves07/Imagens',
            options=QFileDialog.DontUseNativeDialog
        )

        self.new_img.save(img, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app_img = ResizeImage()
    app_img.show()
    qt.exec_()
