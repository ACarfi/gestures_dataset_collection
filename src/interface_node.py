#! /usr/bin/env python3.5
import sys, rospy, PyQt5
from pathlib import Path
from PyQt5 import QtWidgets
from lib.Windows.language_window import LanguageWindow
from lib.Windows.explanation_window import ExplanationWindow
from lib.Windows.camera_window import CameraWindow
from lib.Windows.pinfo_window import PInfoWindow
from lib.Windows.calibration_window import CalibrationWindow
from lib.Windows.recorder_window import RecorderWindow
from lib.Tools.imu_monitor import ImuMonitor
from lib.Tools.header_publisher import HeaderPublisher
from lib.Tools.camera_monitor import CameraMonitor

class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setGeometry(50, 50, 400, 450)
        #self.setFixedSize(400, 450)
        self.folderPath = str(Path(__file__).resolve().parent.parent)+"/gui_content/"
        self.iconsPath = self.folderPath + "icons"
        self.textPath = ""

        #Setting color
        self.setAutoFillBackground(True)
        p = self.palette() 
        p.setColor(self.backgroundRole(), PyQt5.QtGui.QColor(255,255,255))
        self.setPalette(p)

        self.imuMonitor = ImuMonitor('/inertial')
        self.cameraMonitor = CameraMonitor('/webcam/image_raw')
        self.startLanguageSelection()

        self.gesture_publisher = HeaderPublisher("/gestures")
        self.name_publisher = HeaderPublisher("/name")
        self.surname_publisher = HeaderPublisher("/surname")
        self.email_publisher = HeaderPublisher("/email")
        self.age_publisher = HeaderPublisher("/age")
        self.gender_publisher = HeaderPublisher("/gender")
        self.language_publisher = HeaderPublisher("/language")


    def startLanguageSelection(self):
        self.languageSelection = LanguageWindow(self)
        self.setWindowTitle("Language Selection")
        self.setCentralWidget(self.languageSelection)

        self.languageSelection.buttonEnglish.clicked.connect(self.handleEnglishButton)
        self.languageSelection.buttonItalian.clicked.connect(self.handleItalianButton)
        self.showMaximized()

    def handleItalianButton(self):
        self.language_publisher.publish("italian")
        self.textPath = self.folderPath + "text/italian"
        self.startExplanation()
    
    def handleEnglishButton(self):
        self.language_publisher.publish("english")
        self.textPath = self.folderPath + "text/english"
        self.startExplanation()

    def startExplanation(self):
        self.experimentExplanation = ExplanationWindow(self)
        self.setWindowTitle("Experiment Explanation")
        self.setCentralWidget(self.experimentExplanation)

        self.experimentExplanation.button.clicked.connect(self.startVideoAdjustment)
        self.showMaximized()

    def startVideoAdjustment(self):
        self.video = CameraWindow(self)
        self.setWindowTitle("Camera Adjustment")
        self.setCentralWidget(self.video)
        
        self.video.button.clicked.connect(self.startPersonalInfo)
        self.showMaximized()

    def startPersonalInfo(self):
        self.info = PInfoWindow(self)
        self.setWindowTitle("Personal info")
        self.setCentralWidget(self.info)
        self.info.button.clicked.connect(self.startCalibration)
        self.showMaximized()


    def startCalibration(self):
        self.name_publisher.publish(self.info.nameBox.text())
        self.surname_publisher.publish(self.info.surnameBox.text())
        self.email_publisher.publish(self.info.emailBox.text())
        self.age_publisher.publish(self.info.ageBox.text())
        self.gender_publisher.publish(self.info.genderBox.text())

        self.calibration = CalibrationWindow(self)
        self.setWindowTitle("Calibration")
        self.setCentralWidget(self.calibration)
        self.calibration.button.clicked.connect(self.startRecording)
        self.showMaximized()

    def startRecording(self):
        if self.imuMonitor.calibrated:
            self.recorder = RecorderWindow(self)
            self.setWindowTitle("Recording")
            self.setCentralWidget(self.recorder)
            self.showMaximized()

if __name__ == '__main__':
    rospy.init_node('qt_interface', disable_signals=True)

    app = PyQt5.QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())

'''    cam = Camera(0)
    cam.initialize()

    while(cam.cap.isOpened()):
        # write the frame
        frame = cam.get_frame()
        cam.out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.cap.release()
    cam.out.release()
    cv2.destroyAllWindows()'''