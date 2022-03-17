#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:26:07 2020

@author: QI
"""

import pyautogui
import time
#%%
screenWidth, screenHeight = pyautogui.size()

currentMouseX, currentMouseY = pyautogui.position()
# x, y = 1349, -827
#%%
x, y = 230, 10
for i in range(300):
    x, y = x+50, y+100
    pyautogui.moveTo(x,y)
    
    time.sleep(60)
    
    pyautogui.click()
    x, y = x-50, y-100
    pyautogui.moveTo(x,y)
    time.sleep(60)
    
