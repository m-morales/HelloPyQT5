# pylint: disable-msg=E0611
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        label = QLabel('Python', self)
        label.move(50,50)
 
        label2 = QLabel('PyQt5', self)
        label2.move(100,100)
 
        label3 = QLabel('Examples', self)
        label3.move(150,150)


        label4 = QLabel('Hola mundo Python, utf-8 Ññqué ñoqís  hóla', self)
        label4.move(150,250)

        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
