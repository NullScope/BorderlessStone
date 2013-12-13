from win32api import GetSystemMetrics
from win32com.client import GetObject
import os
import win32gui
import win32con
import win32process
import sys
import getopt
import signal

width = None
height = None

offsetx = 0
offsety = 0
border = False

winWidth = None
winHeight = None
cWidth = None
cHeight = None

hPID = None

bFound = False
bBorderless = True

hearthwnd = None
fwnd = None

sWidth = GetSystemMetrics(0)
sHeight = GetSystemMetrics(1)


WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')
process_list = [(p.Properties_("ProcessID").Value, p.Properties_("Name").Value)
                for p in processes]
for p in process_list:
    if(p[1] == "Hearthstone.exe"):
        hPID = p[0]
    if(p[1] == "Agent.exe"):
        fPID = p[0]
if(hPID is None):
    print "Please run Hearthstone first"


def main(argv):
    global width
    global height
    global offsetx
    global offsety
    global bBorderless
    try:
        opts, args = getopt.getopt(argv, "w:h:b:x:y:", ["width=", "height=",
                                                        "border=", "offsetx=",
                                                        "offsety="])
    except getopt.GetoptError:
        print "BorderlessStone.py -w <width> -h <height> -b <border>"
        print "-x <offsetx> -y <offsety>"
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-h", "--height"):
            height = int(arg)
        elif opt in ("-x", "--offsetx"):
            offsetx = int(arg)
        elif opt in ("-y", "--offsety"):
            offsety = int(arg)
        elif opt in ("-b", "--border"):
            bBorderless = bool(arg)

if __name__ == "__main__":
    main(sys.argv[1:])


def enumHandler(hwnd, lParam):
    global bFound
    global hearthwnd
    global fwnd

    if (win32process.GetWindowThreadProcessId(hwnd)[1] == hPID and
            bFound is False):

        bFound = True
        hearthwnd = hwnd
    if(win32process.GetWindowThreadProcessId(hwnd)[1] == fPID):
        fwnd = hwnd


def removeBorders(hwnd):
    global width
    global height
    global bBorderless
    global winWidth
    global winHeight
    global cWidth
    global cHeight
    global offsetx
    global offsety

    win32gui.SetParent(hwnd, fwnd)

    winWidth = win32gui.GetWindowRect(hwnd)[2]
    winHeight = win32gui.GetWindowRect(hwnd)[3]
    cWidth = win32gui.GetClientRect(hwnd)[2]
    cHeight = win32gui.GetClientRect(hwnd)[3]

    if(width != winWidth or
       height != winHeight):

        bResChanged = True

    lStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)

    lStyle &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME |
                win32con.WS_MINIMIZE | win32con.WS_MAXIMIZE |
                win32con.WS_SYSMENU)
    if(not lStyle != win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)):
        bBorderless = True

    # If the user has windowed mode in full resolution, this script
    # will fail to make a borderless window due to the game making
    # a slightly higher resolution than the screen itself,
    # (GetWindowRect includes the borders and GetClientRect
    # makes it always change the resolution)
    # this is why these 2 if's are here

    if width is None:
        width = cWidth

        if(width > sWidth):
            width = sWidth

    if height is None:
        if(bBorderless):
            height = cHeight
        else:
            height = cHeight + (winHeight - cHeight)

        if(height+2 == sHeight):
            height = sHeight

    # Center the window if no command specified

    if(offsetx == 0):
        offsetx = sWidth/2-width/2
    if(offsety == 0):
        offsety = sHeight/2-height/2

    # For some reason, if the resolution is changed from the current one
    #It adds the borders back and takes 3 times to make it borderless again

    if(bResChanged is False):
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
        win32gui.MoveWindow(hwnd, offsetx, offsety,
                            width, height, 1)
    else:
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
        win32gui.MoveWindow(hwnd, offsetx, offsety,
                            width, height, 1)
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
        win32gui.MoveWindow(hwnd, offsetx, offsety,
                            width, height, 1)
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
        win32gui.MoveWindow(hwnd, offsetx, offsety,
                            width, height, 1)

win32gui.EnumWindows(enumHandler, None)

if bFound and bBorderless:
    removeBorders(hearthwnd)
