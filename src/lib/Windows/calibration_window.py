import PyQt5, rospy
from sensor_msgs.msg import Imu
from lib.Tools.imu_monitor import ImuMonitor


class CalibrationWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(CalibrationWindow, self).__init__(parent)
        self.textPath = self.parent.textPath
        
        self.textSize = 40
        self.font = PyQt5.QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        self.font.setPixelSize(self.textSize)

        self.buttonCalibrate = PyQt5.QtWidgets.QPushButton('',self)
        self.buttonCalibrate.setText("Calibrate")
        self.buttonCalibrate.clicked.connect(self.verifyCalibration)

        self.button = PyQt5.QtWidgets.QPushButton('',self)
        self.button.setText("Next")

        self.publishContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.publishContainer.setFont(self.font)

        self.calibrationContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.calibrationContainer.setFont(self.font)

        self.TextContainer = PyQt5.QtWidgets.QTextBrowser(self)
        self.TextContainer.setFont(self.font)

        text = open(self.textPath + '/calibration.txt').read()
        self.TextContainer.setPlainText(text)

        self.timer = PyQt5.QtCore.QTimer() 
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateStatus)

        self.HLayoutOutput = PyQt5.QtWidgets.QHBoxLayout()
        self.HLayoutOutput.addWidget(self.publishContainer)
        self.HLayoutOutput.addWidget(self.calibrationContainer)

        self.HLayoutButtons = PyQt5.QtWidgets.QHBoxLayout()
        self.HLayoutButtons.addWidget(self.buttonCalibrate)
        self.HLayoutButtons.addWidget(self.button)

        self.Layout = PyQt5.QtWidgets.QVBoxLayout(self)
        self.Layout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.Layout.addWidget(self.TextContainer)
        self.Layout.addLayout(self.HLayoutOutput)
        self.Layout.addLayout(self.HLayoutButtons)
        self.setLayout(self.Layout)

        self.timer.start(100)
        
    def updateStatus(self):
        if self.parent.imuMonitor.published:
            self.publishContainer.setText("Smartwatch connected")
        else:
            self.publishContainer.setText("Smartwatch not connected")


    def verifyCalibration(self):
        if abs(self.parent.imuMonitor.data.linear_acceleration.x - 9) < 1:
            self.parent.imuMonitor.calibrated = True
            self.calibrationContainer.setText("The Smartwatch is calibrated")
        else:
            self.calibrationContainer.setText("ERROR")