# PyQt5 imagens

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)  # x, y, width, height

        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)  # x, y, width, height

        pixmap = QPixmap("test/test.jpg")  # Replace "image.jpg" with your image file
        label.setPixmap(pixmap)

        label.setScaledContents(True)  # Scale the image to fit the label

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()