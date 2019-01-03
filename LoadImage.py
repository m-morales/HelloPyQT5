# pylint: disable-msg=E0611
# Siempre cargar la carpeta entera en el VS Code, pórque QPixelmap no reconoce el path absoluto.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap("me.jpg")
        print (pixmap.width(), pixmap.heightMM(),pixmap.height())
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())