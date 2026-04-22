# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(500, 500, 500, 300)  # x, y, width, height
        self.setWindowIcon(QIcon("test/test.jpg"))  # Replace "icon.png" with your icon file

        # Create a label
        label = QLabel("Hello, PyQt5!", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 50)  # x, y, width, height
        label.setStyleSheet("color: blue;" 
                            "background-color: lightgray;" 
                            "font-weight: bold;" 
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()