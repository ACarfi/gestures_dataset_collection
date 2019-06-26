import PyQt5

class PInfoWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(PInfoWindow, self).__init__(parent)
        self.textPath = self.parent.textPath

        self.textSize = 40
        self.font = PyQt5.QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        self.font.setPixelSize(self.textSize)
        
        self.nameBox = PyQt5.QtWidgets.QLineEdit(self)
        self.nameBox.setText("Name")

        self.surnameBox = PyQt5.QtWidgets.QLineEdit(self)
        self.surnameBox.setText("Surname")

        self.emailBox = PyQt5.QtWidgets.QLineEdit(self)
        self.emailBox.setText("email")

        self.genderBox = PyQt5.QtWidgets.QLineEdit(self)
        self.genderBox.setText("male or female")

        self.ageBox = PyQt5.QtWidgets.QLineEdit(self)
        self.ageBox.setText("age")

        self.TextContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.TextContainer.setFont(self.font)
        self.TextContainer.setFixedHeight(self.textSize + 20)

        text = open(self.textPath + '/personal_info.txt').read()
        self.TextContainer.setPlainText(text)
        
        self.button = PyQt5.QtWidgets.QPushButton('',self)
        self.button.setText("Next")


        self.Layout = PyQt5.QtWidgets.QVBoxLayout()
        self.Layout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.Layout.addWidget(self.TextContainer)
        self.Layout.addWidget(self.nameBox)
        self.Layout.addWidget(self.surnameBox)
        self.Layout.addWidget(self.emailBox)
        self.Layout.addWidget(self.genderBox)
        self.Layout.addWidget(self.ageBox)
        self.Layout.addWidget(self.button)
        self.setLayout(self.Layout)