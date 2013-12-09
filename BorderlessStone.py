from win32api import GetSystemMetrics
from win32com.client import GetObject
import win32gui
import win32con
import win32process
import sys
import getopt

width = None
height = None
hPID = None

winWidth = None
winHeight = None
cWidth = None
cHeight = None

bFound = False
bBorderless = False

sWidth = GetSystemMetrics(0)
sHeight = GetSystemMetrics(1)


WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')
process_list = [(p.Properties_("ProcessID").Value, p.Properties_("Name").Value)
                for p in processes]
for p in process_list:
    if(p[1] == "Hearthstone.exe"):
        hPID = p[0]
if(hPID is None):
    print "Please run Hearthstone first"
    sys.exit(2)


def main(argv):
    global width
    global height
    try:
        opts, args = getopt.getopt(argv, "w:h:", ["width=", "height="])
    except getopt.GetoptError:
        print 'BorderlessStone.py -w <width> -h <height>'
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-h", "--height"):
            height = int(arg)

if __name__ == "__main__":
    main(sys.argv[1:])


def enumHandler(hwnd, lParam):
    global bFound
    global width
    global height
    global bBorderless
    global winWidth
    global winHeight
    global cWidth
    global cHeight

    if (win32process.GetWindowThreadProcessId(hwnd)[1] == hPID and
            bFound is False):

        bFound = True
        bResChanged = False

        winWidth = win32gui.GetWindowRect(hwnd)[2]
        winHeight = win32gui.GetWindowRect(hwnd)[3]
        cWidth = win32gui.GetClientRect(hwnd)[2]
        cHeight = win32gui.GetClientRect(hwnd)[3]
        print win32gui.GetWindowRect(hwnd), win32gui.GetClientRect(hwnd)

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

        # Center the window
        centerWidth = sWidth/2-width/2
        centerHeight = sHeight/2-height/2

        print width, height, bBorderless

        # For some reason, if the resolution is changed from the current one
        #It adds the borders back and takes 3 times to make it borderless again

        if(bResChanged is False):
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, centerWidth, centerHeight,
                                width, height, 1)
        else:
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, centerWidth, centerHeight,
                                width, height, 1)
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, centerWidth, centerHeight,
                                width, height, 1)
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, centerWidth, centerHeight,
                                width, height, 1)

win32gui.EnumWindows(enumHandler, None)
