import PyQt5

class ExplanationWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(ExplanationWindow, self).__init__(parent)
        self.textPath = self.parent.textPath

        self.font = PyQt5.QtGui.QFont()
        self.font.setFamily("Arial")

        self.TextContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.TextContainer.setFont(self.font)

        text = open(self.textPath + '/explanation.txt').read()
        self.TextContainer.setPlainText(text)
        
        self.button = PyQt5.QtWidgets.QPushButton('',self)
        #self.button.setIconSize(QtCore.QSize(100,20))
        self.button.setText("Next")

        self.Layout = PyQt5.QtWidgets.QVBoxLayout()
        self.Layout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.Layout.addWidget(self.TextContainer)
        self.Layout.addWidget(self.button)
        self.setLayout(self.Layout)
