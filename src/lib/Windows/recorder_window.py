import PyQt5, rospy, os
from std_msgs.msg import Header
import numpy as np

class RecorderWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(RecorderWindow, self).__init__(parent)
        self.folderPath = self.parent.folderPath + "/" + rospy.get_param('gestures_folder')
        self.num_repetition = rospy.get_param('num_repetition')
        self.imagesNames = os.listdir(self.folderPath)

        self.gestures_order = np.repeat(np.arange(len(self.imagesNames)),self.num_repetition)
        np.random.shuffle(self.gestures_order)

        self.currentImage = 0
        self.progres_value = 0

        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 600

        self.interval = rospy.get_param("speed")
        self.image = PyQt5.QtWidgets.QLabel(self)
        self.image.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

        self.progress = PyQt5.QtWidgets.QProgressBar(self)
        self.progress.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.progress.setGeometry(self.left,self.top,self.width,20)
        self.progress.setMaximum(self.interval)

        self.Layout = PyQt5.QtWidgets.QVBoxLayout()
        self.Layout.addWidget(self.image)
        self.Layout.addWidget(self.progress)
        self.Layout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.setLayout(self.Layout)

        self.timer_image = PyQt5.QtCore.QTimer()
        self.timer_progress = PyQt5.QtCore.QTimer()

        self.timer_progress.setSingleShot(False)
        self.timer_progress.timeout.connect(self.progressIncrement)

        self.timer_image.setSingleShot(False)
        self.timer_image.timeout.connect(self.nextImage)

        self.timer_progress.start(10)
        self.timer_image.start(self.interval)

        self.gesture_publisher = self.parent.gesture_publisher

    def changeImage(self, path):
        pixmap = PyQt5.QtGui.QPixmap(path)
        pixmap = pixmap.scaledToHeight(self.height)
        self.image.setPixmap(pixmap)
        self.show()

    def progressIncrement(self):
        self.progres_value = self.progres_value + 10
        self.progress.setValue(self.progres_value)

    def nextImage(self):

        if self.currentImage >= len(self.gestures_order):
            print(self.currentImage)
            self.timer_image.stop()
            self.timer_progress.stop()
            exit()
        else:
            id = self.gestures_order[self.currentImage]
            self.gesture_publisher.publish(self.imagesNames[id])
            
            self.changeImage(self.folderPath+"/"+self.imagesNames[id])
            self.currentImage = self.currentImage + 1
            self.progres_value = 0
