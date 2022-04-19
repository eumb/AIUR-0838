import sys
import urx
import time
#import file
from urx import RG2Gripper as GripClass
rob = urx.Robot("192.168.1.190")
#instantiate object
gripperInstance = GripClass.RG2(rob)
#basic delay for script(to complete action, RG2 approximatly takes 1.3 seconds to close from completely open)
time.sleep(2)
#set distance between pincers apart, in this case closing
gripperInstance.setWidth(0)
time.sleep(2)
#open the gripper completly
gripperInstance.setWidth(110)
time.sleep(2)
#returns the current width of the robot
gripperInstance.getWidth()