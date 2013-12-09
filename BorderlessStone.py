from win32api import GetSystemMetrics
import win32gui
import win32con
import sys
import getopt

width = None
height = None
sWidth = GetSystemMetrics(0)
sHeight = GetSystemMetrics(1)


def main(argv):
    global width
    global height
    try:
        opts, args = getopt.getopt(argv, "w:h:", ["width=", "height="])
    except getopt.GetoptError:
        print 'test.py -w <width> -h <height>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-h", "--height"):
            height = int(arg)

if __name__ == "__main__":
    main(sys.argv[1:])


def enumHandler(hwnd, lParam):

    if 'Hearthstone' in win32gui.GetWindowText(hwnd):
        global width
        global height
        winWidth = win32gui.GetWindowRect(hwnd)[2]
        winHeight = win32gui.GetWindowRect(hwnd)[3]
        bResChanged = False

        if(width != winWidth or
           height != winHeight):

            bResChanged = True

        # If the user has windowed mode in full resolution, this script
        # will fail to make a borderless window due to the game making
        # a slightly higher resolution than the screen itself,
        # (GetWindowRect includes the borders and GetClientRect
        # makes it always change the resolution)
        # this is why these 2 if's are here

        if width is None:
            width = win32gui.GetWindowRect(hwnd)[2]

            if(width > sWidth):
                width = sWidth

        if height is None:
            height = win32gui.GetWindowRect(hwnd)[3]
            if(height+2 == sHeight):
                height = sHeight

        lStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        lStyle &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME |
                    win32con.WS_MINIMIZE | win32con.WS_MAXIMIZE |
                    win32con.WS_SYSMENU)

        # For some reason, if the resolution is changed from the current one
        #It adds the borders back and takes 3 times to make it borderless again

        if(bResChanged is False):
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, 0, 0, width, height, 1)
        else:
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, 0, 0, width, height, 1)
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, 0, 0, width, height, 1)
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, lStyle)
            win32gui.MoveWindow(hwnd, 0, 0, width, height, 1)

win32gui.EnumWindows(enumHandler, None)
