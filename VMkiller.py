#Yuchuan Tian 2020 Copyright
from pynput.keyboard import Key
import time
import win32gui,win32con

def keyInput(ch,keyboard):
    if ch==' ':
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif ch!='\n' and ch!='\r':
        keyboard.press(ch)
        keyboard.release(ch)

def keyEnter(keyboard):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def stringInput(string,keyboard):
    for char in string:
        keyInput(char,keyboard)

def fileInput(filename):
    from pynput.keyboard import Controller
    with open(filename,'r') as file:
        listing=file.readlines()

    keyboard=Controller()
    for string in listing:
        stringInput(string,keyboard)
        keyEnter(keyboard)




def windowOutshow(): # shift to the remote desktop  
    hwnd = win32gui.FindWindow(None, '10.119.3.80 - 远程桌面连接')
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hwnd)
    

if __name__=='__main__':
    windowOutshow()
    time.sleep(1)
    fileInput("ex3.cpp")


