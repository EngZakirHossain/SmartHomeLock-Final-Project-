from flask import Flask, render_template, Response, jsonify, request
from recognition import VideoCamera
import datetime
import os
import base64
import io
from PIL import Image
import urllib
from urllib import urlopen
from datetime import datetime
import subprocess
import sys
import RPi.GPIO as GPIO
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

def video_stream():
    video_camera = VideoCamera()
    while True:
        frame = video_camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/open_lock',methods=['POST'])
def open_lock():
    json = request.get_json()

    status = json['status']

    if status == "true":
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11,True)
    else:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(11,False)
        GPIO.output(12,False)


@app.route("/saveimagedata", methods=['POST'])
def saveImage():
	n = datetime.now()
	imgData = request.form['img_val']
	urllib.urlretrieve(imgData, n.strftime('images/image_%m%d%Y_%H%M%S.jpg'))
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

