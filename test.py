import speech_recognition as sr

def main_background():
    # wątek działający w tle
    def callback(recognizer, audio):
        global stop
        global trigger
        global notunderstand
        global licznik
        # jeśli pozyskał dane to rozpoznawanie
        try:
            # instead of `r.recognize_google(audio)`
            text =recognizer.recognize_google(audio,language="pl")
            text =  " " + text
            print("You said: " + text)

m = sr.Microphone()
r = sr.Recognizer()
r.energy_threshold=600
r.pause_threshold= 0.3
r.non_speaking_duration=0.3

with m as source:
    print("listening to ambient")
    r.adjust_for_ambient_noise(source)  # call  jeden raz
    print("end of listening to ambient")

# start słuchania w tle
rint("odpalenie listening in background")
stop_listening = r.listen_in_background(m, callback)
print("listening in the background")