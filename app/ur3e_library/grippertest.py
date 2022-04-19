import sys
import urx
from urx.gripper import OnRobotGripperRG2

if __name__ == '__main__':
    rob = urx.Robot("192.168.2.190")
    gripper = OnRobotGripperRG2(rob)

    if len(sys.argv) != 2:
        print ("false")
        sys.exit()

    if sys.argv[1] == "close":
        gripper.close_gripper(0)
    if sys.argv[1] == "open":
        gripper.open_gripper()
        print("open done")

    rob.close()
    print("true")
    sys.exit()