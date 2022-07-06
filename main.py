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
keyboard = Controller()

def main():
    #for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    
    # variables defined
    #trigger = False
    once = 0
    #stop = 0
    global stop
    global trigger

    #listening = 0
    licznik = 0
    notunderstand = 0
    
    #r1 = sr.Recognizer()  
    #r2 = sr.Recognizer()
    #r1.energy_threshold=2000
    #r1.pause_threshold= 0.5
    #r1.non_speaking_duration=0.5
    r = sr.Recognizer() 
    r.energy_threshold=600
    r.pause_threshold= 0.5
    r.non_speaking_duration=0.5

    with sr.Microphone(device_index=1) as source:
        while stop == 0:
            #if(listening==0):
            #    r=r1
            #    listening=1
            #else:
            #    r=r2
            #    listening=0
            
            if(once ==0):
                once=1
                print("listening to ambient")
                r.adjust_for_ambient_noise(source,duration=3)
                print("end of listening to ambient")
                ps.playsound("gotowy.mp3")
                
            print("listening:")
            audio = r.listen(source)
            print("after listen")
            #audio = reco.listen_in_background(source,callback)
            
            try:
                #text = r.recognize_google(audio)
                text = r.recognize_google(audio,language="pl")
                print("you said: {}".format(text))
                
                if("Jan" in text or "0" in text or "Janie" in text or "zero" in text):
                    trigger = True
                    licznik = 0
                print("trigger: "+str(trigger))
                # testing part
                if("trigger" in text  or "Trigger" in text):
                    ps.playsound("triggerto.mp3")
                    if(trigger==True):
                        ps.playsound("True.mp3")
                    elif(trigger==False):
                        ps.playsound("False.mp3")
                    else:
                        print("problem")
                # end of testing part

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
            
            except:
                print("didn't hear it (or error accured), Trigger= {}".format(trigger))
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
            print(" --- ")
        
def stopProgram():
    global stop
    stop = 1

if __name__ == "__main__":
    com.main()