import cv2
import numpy as np
import os
import subprocess
import sys
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "faceDetector.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'X', 'Y', 'Z', 'A', 'B']

class VideoCamera(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def __del__(self):
        self.cam.release()

    def get_frame(self):
        self.cam.set(3, 640) # set video widht
        self.cam.set(4, 480)
        ret, img = self.cam.read()
        minW = 0.1*self.cam.get(3)
        minH = 0.1*self.cam.get(4)
        img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                subprocess.call(["python", "/home/pi/testing1.2/lockControl.py"])
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
         
                subprocess.call(["python", "/home/pi/testing1.2/notifyControl.py"])
               # p = subprocess.Popen([sys.executable, '/home/pi/faceRecognitionDoorLock/notifyControl.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

        ret, jpeg = cv2.imencode('.jpg', img)

        return jpeg.tobytes()

