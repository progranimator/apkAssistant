import os
import sys
import subprocess
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QTextEdit, QCheckBox


class APKPusherGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("APK Pusher")
        layout = QGridLayout()

        self.apk_path_label = QLabel("APK Path:")
        self.apk_path_entry = QLineEdit()
        self.dest_path_label = QLabel("Destination Path:")
        self.dest_path_entry = QLineEdit()
        self.push_button = QPushButton(
            "Push APK", clicked=self.push_button_clicked)
        self.exit_button = QPushButton(
            "Exit", clicked=self.exit_button_clicked)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        layout.addWidget(self.apk_path_label, 0, 0)
        layout.addWidget(self.apk_path_entry, 0, 1)
        layout.addWidget(self.dest_path_label, 1, 0)
        layout.addWidget(self.dest_path_entry, 1, 1)
        layout.addWidget(self.push_button, 2, 0)
        layout.addWidget(self.exit_button, 2, 1)
        layout.addWidget(self.output_text, 3, 0, 1, 2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet(
            "background-color: #282828; color: Gray; QLineEdit { border: 1px solid black; }")
        self.setWindowIcon(QIcon('android_logo.png'))

    def push_button_clicked(self):
        apk_path = self.apk_path_entry.text()
        dest_path = self.dest_path_entry.text()

        if not os.path.isfile(apk_path):
            self.output_text.setPlainText("Error: APK file does not exist!")
            return

        # execute the adb push command using subprocess
        cmd = f"adb push {apk_path} {dest_path}"
        try:
            output = subprocess.check_output(cmd.split())
        except subprocess.CalledProcessError as e:
            self.output_text.setPlainText(f"Error: {e}")
            return

        # print the output of the command to the console
        self.output_text.setPlainText(output.decode("utf-8"))

    def exit_button_clicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = APKPusherGUI()
    mainWin.show()
    sys.exit(app.exec())
