import PyQt5
from lib.Tools.camera import Camera

class CameraWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(CameraWindow, self).__init__(parent)
        self.textPath = self.parent.textPath

        self.textSize = 40
        self.font = PyQt5.QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        self.font.setPixelSize(self.textSize)

        self.cameraMonitor = self.parent.cameraMonitor
        #self.camera = Camera(0)
        #self.camera.initialize()

        self.TextContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.TextContainer.setFont(self.font)
        self.TextContainer.setFixedHeight(self.textSize + 20)
        self.TextContainer.setVerticalScrollBar
        
        text = open(self.textPath + '/video_adjustment.txt').read()
        self.TextContainer.setPlainText(text)

        self.timer = PyQt5.QtCore.QTimer() 
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateImage)

        self.imageView = PyQt5.QtWidgets.QLabel(self)
        self.imageView.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

        self.button = PyQt5.QtWidgets.QPushButton('',self)
        self.button.setText("Next")

        self.Layout = PyQt5.QtWidgets.QVBoxLayout()
        self.Layout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.Layout.addWidget(self.TextContainer)
        self.Layout.addWidget(self.imageView)
        self.Layout.addWidget(self.button)
        self.setLayout(self.Layout)

        self.timer.start(50)


    def updateImage(self):
        message = self.cameraMonitor.message
        qImg = PyQt5.QtGui.QImage(message.data, message.width, message.height, PyQt5.QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = PyQt5.QtGui.QPixmap.fromImage(qImg)
        self.imageView.setPixmap(pixmap)