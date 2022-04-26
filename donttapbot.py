from time import sleep
from pyautogui import pixel
import keyboard
import win32api, win32con

x = (520, 620, 760, 890)
y = (260, 410, 530, 650)

print('Press E to start')
keyboard.wait('e')
sleep(1)

while keyboard.is_pressed('q') == False:
    for i in x:
        for j in y:
            if pixel(i, j) [0] == 0:
                win32api.SetCursorPos((i,j))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)