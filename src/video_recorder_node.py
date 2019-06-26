#! /usr/bin/env python2

import numpy as np
import cv2, rospy

class VideoRecorder():
    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.file_name = 'output.mp4'
        self.out = cv2.VideoWriter(self.file_name,0x00000021, 30.0, (int(self.cap.get(3)),int(self.cap.get(4))))


if __name__ == '__main__':
    rospy.init_node('video_recorder_node', disable_signals=True)
    Vrecord = VideoRecorder() 

    while(Vrecord.cap.isOpened()):
        ret, frame = Vrecord.cap.read()
        if ret==True:
            # write the flipped frame
            Vrecord.out.write(frame)

            #cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything if job is finished
    Vrecord.cap.release()
    Vrecord.out.release()
    cv2.destroyAllWindows()