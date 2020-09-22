import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame, QCheckBox, QInputDialog, QAction, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QRect




class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'UnrealtoAndroid v1.1'
        self.left = 10
        self.top = 10
        self.setFixedSize(500, 700)
        self.width = 500
        self.height = 700
        self.initUI()
        #

    def initUI(self):

        #create window for buttons
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #

        #create textboxes
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 130)
        self.textbox.resize(400,30)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 320)
        self.textbox1.resize(400,30)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(45, 540)
        self.textbox2.resize(400,30)
        #

        # create lines
        line1 = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        line1.setPixmap(pixmap)
        line1.resize(900,9)
        line1.move(-300,100)

        line2 = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        line2.setPixmap(pixmap)
        line2.resize(900,3)
        line2.move(-300,280)
         
        line3 = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        line3.setPixmap(pixmap)
        line3.resize(900,3)
        line3.move(-300,480)
        #

        #create borders + dropshadows + icons
        leftBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        leftBorder.setPixmap(pixmap)
        leftBorder.resize(7,900)
        leftBorder.move(-2,0)

        rightBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        rightBorder.setPixmap(pixmap)
        rightBorder.resize(7,900)
        rightBorder.move(495,0)

        bottomBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        bottomBorder.setPixmap(pixmap)
        bottomBorder.resize(900,7)
        bottomBorder.move(-300,693)

        topBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        topBorder.setPixmap(pixmap)
        topBorder.resize(900,7)
        topBorder.move(-300,0)

        deleteAndroidButtonDropShadow = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        deleteAndroidButtonDropShadow.setPixmap(pixmap)
        deleteAndroidButtonDropShadow.resize(168,30)
        deleteAndroidButtonDropShadow.move(52,47)

        pushApkToAndroidDropShadow = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        pushApkToAndroidDropShadow.setPixmap(pixmap)
        pushApkToAndroidDropShadow.resize(160,30)
        pushApkToAndroidDropShadow.move(300,47)

        questionBoxBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        questionBoxBorder.setPixmap(pixmap)
        questionBoxBorder.resize(33,33)
        questionBoxBorder.move(453,653)

        leftCircleBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        leftCircleBorder.setPixmap(pixmap)
        leftCircleBorder.resize(20,20)
        leftCircleBorder.move(-2,95)

        rightCircleBorder = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/flat smoky black')
        rightCircleBorder.setPixmap(pixmap)
        rightCircleBorder.resize(20,20)
        rightCircleBorder.move(480,95)

        trashIcon = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/android trash icon')
        trashIcon.setPixmap(pixmap)
        trashIcon.resize(30,30)
        trashIcon.move(15,20)

        pushIcon = QLabel(self)
        pixmap = QPixmap('C:/Users/progr/Creative Cloud Files/Images/Textures/download icon')
        pushIcon.setPixmap(pixmap)
        pushIcon.resize(30,30)
        pushIcon.move(268,20)
        #

        # Create buttons
        button1 = QPushButton('^ ^ Enter Folder Location of .apk ^ ^', self)
        button1.move(108,185)
        button1.setStyleSheet("background-color : white")

        button2 = QPushButton('Delete Android Folder', self)
        button2.setToolTip('C:/Users/progr/Desktop/Oculus4.23')
        button2.move(50, 40)
        button2.clicked.connect(self.on_click1)
        button2.setStyleSheet("background-color : white")

        button3 = QPushButton('Push apk to Android', self)
        button3.setToolTip('Before pressing button, set .apk name below')
        button3.move(300, 40)
        button3.clicked.connect(self.on_click2)
        button3.setStyleSheet("background-color : white")

        button4 = QPushButton('^ ^ Enter name of .apk ^ ^', self)
        button4.move(135,380)
        button4.setStyleSheet("background-color : white")

        button5 = QPushButton('^ ^ Enter Location of UnrealtoAndroid.txt ^ ^', self)
        button5.move(70,600)
        button5.setStyleSheet("background-color : white")

        buttonInstructions = QPushButton('?', self)
        buttonInstructions.move(455,655)
        buttonInstructions.setStyleSheet("background-color : white")
        buttonInstructions.resize(30,30)
        #

        # connect button1 to function on_click3 // set location of apk file
        button1.clicked.connect(self.on_click3)
        button1.show()

        # connect button4 to function on_click4 // set name of .apk file
        button4.clicked.connect(self.on_click4)
        button4.show()

        # connect button5 to function on_click5 // set location of UnrealtoAndroid.txt
        button4.clicked.connect(self.on_click4)
        button4.show()

        # connect button(instructionWindow) to function show_new_window
        buttonInstructions.clicked.connect(self.show_new_window)
        buttonInstructions.show()

        self.show()
        app.setStyle('Oxygen')


    @pyqtSlot()
    def on_click1(self):
        import shutil
        import os
        dir = "Android_ETC2"
        location = apkFileLocation
        path = os.path.join(location, dir)
        shutil.rmtree(path)

    # Execute adb command 'apk install'
    @pyqtSlot()
    def on_click2(self):
        import subprocess
        subprocess.call(
            "adb install" + " -r " + apkFileLocation + apkName,
            shell=True)

    # Enter Location of apk file
    @pyqtSlot()
    def on_click3(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'location of apk file set', "" + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        global apkFileLocation
        apkFileLocation = textboxValue

        # read and write file
        #file = open('C:/Users/progr/Desktop/WriteToThisFile.txt', 'w') 
        #with open('C:/Users/progr/Desktop/WriteToThisFile.txt','w') as writer:
                #writer.write(textboxValue)
    
    
    # Enter name of apk file // set global variable 'apkName'
    @pyqtSlot()
    def on_click4(self): 
        textboxValue = self.textbox1.text()
        QMessageBox.question(self, 'apk name set', "" + textboxValue, QMessageBox.Close,)
        self.textbox1.setText("")
        global apkName
        apkName = textboxValue

    # Show new window detailing program instructions
    @pyqtSlot()
    def show_new_window(self): 
        msg = QMessageBox()
        msg.setText("        Welcome to 'UnrealtoAndroid'")
        msg.setWindowTitle("                               FAQs")
        msg.setDetailedText("What is UnrealtoAndroid? - - \nUnrealtoAndroid is a Python script designed to increase the efficiency of creating apk files for Android devices.\nHow does it work? - - \n")
        msg.setStandardButtons(QMessageBox.Close)
        msg.addButton(QPushButton('Ok'), msg.ActionRole)
        msg.setWindowIcon(QIcon('C:/Users/progr/Creative Cloud Files/Images/Textures/android question mark'))
        msg.setDefaultButton(QMessageBox.Close)
	
        openWindow = msg.exec_()
    



# app end
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())

    
