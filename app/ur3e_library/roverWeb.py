from flask import Flask, render_template, Response, request, redirect, url_for

import MDD10A as HBridge
import io
import socket
import logging
import socketserver
from threading import Condition
from http import server
import time


app = Flask(__name__)


speedleft = 0
speedright = 0

#app.config["DEBUG"] = True

def printspeed():
        print ("speedleft: " + str(speedleft))
        print ("speedright: " + str(speedright))
# Keyboard character retrieval method. This method will save
# the pressed key into the variable char


@app.route("/",methods=["GET"])
def index():
    return render_template('main.html')

@app.route("/fw")
def forward():
        global speedleft
        global speedright
        if speedleft > speedright:
                speedright = speedleft
        if speedright > speedleft:
                speedleft = speedright
        # accelerate the RaPi car
        speedleft = speedleft + 0.1
        speedright = speedright + 0.1
        if speedleft > 1:
                speedleft = 1
        if speedright > 1:
                speedright = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        print ("move forward")
        printspeed()
        return "move forward"
@app.route("/bk")
def backward():
        global speedleft
        global speedright
        if speedleft > speedright:
                speedleft = speedright
        if speedright > speedleft:
                speedright = speedleft
        # slow down the RaPi car
        speedleft = speedleft - 0.1
        speedright = speedright - 0.1
        if speedleft < -1:
                speedleft = -1
        if speedright < -1:
                speedright = -1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        print ("move backward")
        printspeed()
        return "move backward"

@app.route("/stop")
def stop():
        global speedleft
        global speedright
        speedleft = 0
        speedright = 0
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        print  ("motors stopped")
        printspeed()
        return "motors stopped"

@app.route("/right")
def right():
        global speedleft
        global speedright
        if speedleft > speedright:
                speedright = speedright - 0.1
                speedleft = speedleft + 0.1
        if speedright > speedleft:
                speedright = speedright - 0.1
                speedleft = speedleft + 0.1
        if speedright == speedleft:
            speedright = speedright - 0.1
            speedleft = speedleft + 0.1
        if speedright < -1:
                speedright = -1
        if speedleft > 1:
                speedleft = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        print ("move right")
        printspeed()
        return "right"

@app.route("/left")
def left():
        global speedleft
        global speedright
        if speedright > speedleft:
                speedleft = speedleft - 0.1
                speedright = speedright + 0.1
        if speedleft > speedright:
                speedleft = speedleft - 0.1
                speedright = speedright + 0.1
        if speedleft < -1:
                speedleft = -1
        if speedright > 1:
                speedright = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        print ("move left")
        printspeed()
        return "left"

@app.route("/end")
def end():
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
        HBridge.exit()
        print ("stop")
        return "end"
if __name__ == '__main__':
    app.run(host='192.168.2.76')