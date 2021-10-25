from ctypes import WinDLL
from time import sleep
import sys

if len(sys.argv) == 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) > 0:
    MOVE_INTERVAL = int(sys.argv[1])
else:
    MOVE_INTERVAL = 10

user32 = WinDLL('user32', use_last_error=True)

MOUSE_INCREMENT = 1  # to make program practically always runnable, increment should be kept at minimum
# 0x0001 is dword of MOUSEEVENTF_MOVE,
# see https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
MOUSEEVENTF_MOVE = 0x0001


def move_mouse(x, y):
    """
    x, y are relative to current position and in pixels
    """
    user32.mouse_event(MOUSEEVENTF_MOVE, int(x), int(y), 0, 0)


def run():
    print('Press Ctrl-C to quit.')
    try:
        forward = True
        while True:
            if forward:
                move_mouse(MOUSE_INCREMENT, MOUSE_INCREMENT)
            else:
                move_mouse(-MOUSE_INCREMENT, -MOUSE_INCREMENT)
            forward = not forward
            sleep(MOVE_INTERVAL)
    except KeyboardInterrupt:
        print('')


if __name__ == "__main__":
    run()
