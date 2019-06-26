import PyQt5

class LanguageWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(LanguageWindow, self).__init__(parent)
        self.iconsPath = self.parent.iconsPath

        self.buttonEnglish = PyQt5.QtWidgets.QPushButton('', self)
        self.buttonItalian = PyQt5.QtWidgets.QPushButton('', self)

        self.buttonEnglish.setIconSize(PyQt5.QtCore.QSize(300,300))
        self.buttonEnglish.setIcon(PyQt5.QtGui.QIcon(self.iconsPath + '/englishFlag.png'))
        self.buttonItalian.setIconSize(PyQt5.QtCore.QSize(300,300))
        self.buttonItalian.setIcon(PyQt5.QtGui.QIcon(self.iconsPath + '/italianFlag.png'))

        self.Layout = PyQt5.QtWidgets.QHBoxLayout()
        self.Layout.addWidget(self.buttonEnglish)
        self.Layout.addWidget(self.buttonItalian)

        self.setLayout(self.Layout)