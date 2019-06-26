import sys
sys.path.insert(0,'/usr/local/lib/python3.5/dist-packages')
import cv2
import numpy as np

class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.cap = None
        self.last_frame = np.zeros((1,1))
        #self.file_name = 'output.mp4v'
        self.out = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)
        #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        #self.out = cv2.VideoWriter(self.file_name,fourcc, 30.0, (int(self.cap.get(3)),int(self.cap.get(4))))

    def get_frame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def acquire_movie(self, num_frames):
        movie = []
        for _ in range(num_frames):
            movie.append(self.get_frame())
        return movie

    def set_brightness(self, value):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def close_camera(self):
        self.cap.release()

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)