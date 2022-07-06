# outside imports
import speech_recognition as sr
import time
import playsound as ps
import os
import sys
import pygetwindow as getwindow

# keyboard imports
import pynput
from pynput.keyboard import Key, Controller
#import keyboard as kb
import pyautogui as pg

# my project imports
from create_audio_file import create_audio_file

################################################################################################
import googletrans
from googletrans import Translator

dataToRead="example"

translator = Translator()
dt1 = translator.detect(dataToRead)
print(dt1)
translated = translator.translate(dataToRead,src='en',dest='pl')

dataToRead = translated.text
print(dataToRead)
#print(googletrans.LANGUAGES)