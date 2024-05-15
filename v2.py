import sys
import time
import cv2
import numpy as np
import mss
import pyautogui

from pynput.mouse import Button, Controller

import threading


mouse = Controller()

def Screen_Shot(left=0, top=0, width=1920, height=1080):
    stc = mss.mss()
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img



while True:
    stc = mss.mss()
    scr = stc.grab(
        {
            "left": 800,
            "top": 250,
            "width": 500,
            "height": 470,
        }
    )
    frame = np.array(scr)
    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_lower = np.array([110, 185, 240], np.uint8)
    green_upper = np.array([120, 220, 245], np.uint8)
    green_mask = cv2.inRange(hsvframe, green_lower, green_upper)

    kernal = np.ones((5, 5), "uint8")

    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(frame, frame, mask=green_mask)


    # Check if green mask is present
    if np.any(green_mask > 0):
        print("buldum")
        pyautogui.click(1650,850)
        time.sleep(.5)
        while True:
            stc = mss.mss()
            scr = stc.grab(
                {
                    "left": 800,
                    "top": 250,
                    "width": 500,
                    "height": 470,
                }
            )
            frame = np.array(scr)
            hsvframex = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            green_lowerx = np.array([10, 135, 255], np.uint8)
            green_upperx = np.array([13, 140, 255], np.uint8)
            green_maskx = cv2.inRange(hsvframex, green_lowerx, green_upperx)

            getxx_lowerx = np.array([101, 235, 255], np.uint8)
            getxx_upperx = np.array([104, 237, 255], np.uint8)
            getxx_maskx = cv2.inRange(hsvframex, getxx_lowerx, getxx_upperx)

            kernal = np.ones((5, 5), "uint8")

            green_maskx = cv2.dilate(green_maskx, kernal)
            res_greenx = cv2.bitwise_and(frame, frame, mask=green_maskx)


            # Check if green mask is present
            if np.any(green_maskx > 0):
                print("catch")
                time.sleep(.021)
                pyautogui.click(1650, 850) #button
                time.sleep(.55)

            if np.any(getxx_maskx > 0):
                time.sleep(1)
                print("get")
                pyautogui.click(1640, 835)  #button
                time.sleep(3)
                pyautogui.click(1580, 720) #button
                break

    # Press q to quit program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        sys.exit()
