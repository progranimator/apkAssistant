import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame, QCheckBox, QInputDialog,QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Unreal to Oculus v1.1'
        self.left = 10
        self.top = 10
        self.width = 540
        self.height = 300
        self.initUI()

    def initUI(self):
        #create window for buttons
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(60, 125)
        self.textbox.resize(400,40)
        

        # Create buttons
        button1 = QPushButton('^ ^ Enter File Path to adb folder ^ ^', self)
        button1.move(100,180)
        button1.setStyleSheet("background-color : white")

        button2 = QPushButton('Delete Android Folder', self)
        button2.setToolTip('C:/Users/progr/Desktop/Oculus4.23')
        button2.move(50, 40)
        button2.clicked.connect(self.on_click1)
        button2.setStyleSheet("background-color : white")

        button3 = QPushButton('Push adb to Oculus', self)
        button3.setToolTip('Push adb to Oculus')
        button3.move(300, 40)
        button3.clicked.connect(self.on_click2)
        button3.setStyleSheet("background-color : white")

        # connect button to function on_click
        button1.clicked.connect(self.on_click3)
        button1.show()

        self.show()
        app.setStyle('Oxygen')
        


    @pyqtSlot()
    def on_click1(self):
        import shutil
        import os
        dir = "Android_ETC2"
        location = "C:/Users/progr/Desktop/Oculus4.23"
        path = os.path.join(location, dir)
        shutil.rmtree(path)

    @pyqtSlot()
    def on_click2(self):
        import subprocess
        subprocess.call(
            "adb install -r C:/Users/progr/Desktop/Oculus4.23/Android_ETC2/Electropelago423-armv7-es2.apk",
            shell=True)

    @pyqtSlot()
    def on_click3(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

        # read and write file
        savedTextFile = textboxValue
        file = open('C:/Users/progr/Desktop/WriteToThisFile.txt', 'w') 
        with open('C:/Users/progr/Desktop/WriteToThisFile.txt','w') as writer:
                writer.write(textboxValue)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())

    
