import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,\
    QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create a label and a text box for the first number
        label1 = QLabel("Enter the first number:", self)
        label1.move(20, 20)
        self.num1Edit = QLineEdit(self)
        self.num1Edit.move(20, 40)

        # create a label and a text box for the second number
        label2 = QLabel("Enter the second number:", self)
        label2.move(20, 80)
        self.num2Edit = QLineEdit(self)
        self.num2Edit.move(20, 100)

        # create a button to perform the calculation
        button = QPushButton("Calculate", self)
        button.move(20, 140)
        button.clicked.connect(self.onClick)

        # create a label to display the result
        self.resultLabel = QLabel("", self)
        self.resultLabel.move(20, 180)

        # set the size and title of the window
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Calculator")

    def onClick(self):
        # get the user input
        num1 = self.num1Edit.text()
        num2 = self.num2Edit.text()

        # convert the input to numbers and add them
        result = int(num1) + int(num2)

        # display the result
        self.resultLabel.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
