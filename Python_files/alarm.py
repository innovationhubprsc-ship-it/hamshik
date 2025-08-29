import sys
from PyQt5.QtWidgets import (QPushButton,QWidget,QBoxLayout,QLabel,QLineEdit,QApplication) # pyright: ignore[reportMissingImports]
from PyQt5.QtGui import (QIcon, QFont) # pyright: ignore[reportMissingImports]
from datetime import datetime

class AlarmClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm Clock")
        self.input = QLineEdit(self)
        self.button = QPushButton("Enter",self)
        self.setGeometry(20,20,180,50)
        self.button.setGeometry(155,0,60,30)
        self.input.setGeometry(0,0,154,30)
        self.input.setPlaceholderText("Enter the time(HH:MM:SS)")
        self.button.clicked.connect(self.submit)
        self.initUI()
    def initUI(self):
        print("!!!")

    def submit(self):
        text = self.input.text()
        self.Time(text)
    def Time(self, Time):
        while (1):
            try:
                time = datetime.strptime(Time, "%H:%M:%S")
                break
            except (ValueError):
                print("Invaild!!")
        return f"{time}"

def main():
    app = QApplication(sys.argv)
    window = AlarmClock()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
