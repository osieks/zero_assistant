#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
# outside imports
import speech_recognition as sr
import time
import playsound as ps
import os
import sys
import pygetwindow as getwindow
import tkinter as Tk
import random
from googletrans import Translator

# keyboard imports
import pynput
from pynput.keyboard import Key, Controller
#import keyboard as kb
import pyautogui as pg

# my project imports
import command as com

stop = 0
trigger = False
notunderstand = 0
licznik = 0

def main_background():
    # this is called from the background thread
    def callback(recognizer, audio):
        global stop
        global trigger
        global notunderstand
        global licznik
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            text =recognizer.recognize_google(audio,language="pl")
            text =  " " + text
            print("You said: " + text)
            #if("Jan" in text or " 0" in text or "Janie" in text or "zero" in text):
            if(" 0" in text or "zero" in text or "delta" in text or "Delta" in text):
                trigger = True
            print("Trigger: "+str(trigger))
            if("trigger" in text  or "Trigger" in text):
                ps.playsound("triggerto.mp3")
                if(trigger==True):
                    ps.playsound("True.mp3")
                elif(trigger==False):
                    ps.playsound("False.mp3")
                else:
                    print("problem")
            if(trigger==True):
                check = com.command(text.lower())
                licznik = 0
                if(check==0):
                    print("command returned: "+str(check))
                    trigger = False
                if(licznik>5): 
                    trigger = False
                else:
                    licznik= licznik+1

        except sr.UnknownValueError:
            print("Could not understand audio. Trigger = "+str(trigger))
            if(trigger==True and notunderstand == 0):
                ps.playsound("niezrozumialem.mp3")
                notunderstand = 1
            else:
                notunderstand == 0
            if(trigger==True):
                licznik=licznik+1
                print("licznik: "+str(licznik))
                if(licznik>4):
                    trigger=False
                    licznik=0

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    m = sr.Microphone()
    r = sr.Recognizer()
    r.energy_threshold=600
    r.pause_threshold= 0.3
    r.non_speaking_duration=0.3

    with m as source:
        print("listening to ambient")
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
        print("end of listening to ambient")

    # start listening in the background (note that we don't have to do this inside a `with` statement)
    print("odpalenie listening in background")
    stop_listening = r.listen_in_background(m, callback)
    print("listening in the background")
    ps.playsound("gotowy.mp3")

    # infinite loop for program to run in the background
    while True: time.sleep(0.1)

    # `stop_listening` is now a function that, when called, stops background listening

    # do some unrelated computations for 5 seconds
    #for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

    # calling this function requests that the background listener stop listening
    #stop_listening(wait_for_stop=False)

    # do some more unrelated things
    #while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

if __name__ == "__main__":
    com.main()