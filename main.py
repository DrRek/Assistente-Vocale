import speech_recognition
import pyttsx # offline recognizer
import sys
import subprocess

speech_engine = pyttsx.init('espeak') # espeak per Linux, altre su http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 180)

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

def listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Got it! Now to recognize it...")
    
    try:
        value = recognizer.recognize_google(audio)
        return value
    except speech_recognition.UnknownValueError:
        value = recognizer.recognize_sphinx(audio)   # offline
            return value
        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        except speech_recognition.RequestError as e:
            print("Recognizer By pyttsx Error: {0}".format(e))
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        try:
        value = recognizer.recognize_sphinx(audio)   # offline
            return value
        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        except speech_recognition.RequestError as e:
            print("Recognizer By pyttsx Error: {0}".format(e))
        print("Recognizer By Google Error: {0}".format(e))
    return ""

def sorter(said):
    if said == "TeamSpeak":    # Comando eseguito per Teamspeak
        print "Starting TeamSpeak..."
        subprocess.Popen([sys.executable, 'teamspeak/teamspeak.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # subprocess
    elif said == "Minecraft":
        print "Starting official Minecraft..."
        subprocess.Popen([sys.executable, 'minecraft/minecraft.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elif said == "launcher":
        print "Starting cracked Minecraft..."
        subprocess.Popen([sys.executable, 'launcher/launcher.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()
    return

def quit(text):
    if text=="bye bye" or text=="close": # Lista di parole per bloccare l'ascolto e terminare
         return False
    else:
         return True

# speech_engine.say('Say something!')     # Trovarne un sostituto per la sinstesi vocale
# speech_engine.runAndWait()
said = "null"
while quit(said):
     said = listen()
     print(said)
     sorter(said)
print "Bye!"   
