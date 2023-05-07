from chatterbot import ChatBot
import speech_recognition
import pyttsx3
import engineio
from chatterbot.trainers import ListTrainer
import AETOABChatDatasetList
from AETOABChatDatasetList import datasetList, datasetListUnchecked

import time
time.clock = time.time
from AETOABsource import respond, setup
#--CHATBOT STUFF--
setup
#set-up
exit_conditions = (":q", "quit", "exit")

AETOABChan = ["i-80 john", "youtube", "80's song", "i-80", "dub john", "tub john", "a chong", "age of john", "280 john"] #use this list for voice recognition correction later

recognizer = speech_recognition.Recognizer()

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('voice', voices[0].id)
engineio.setProperty('rate', 150)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

speak("Booting up...")

#Session loop
while True:
    
    try:
        with speech_recognition.Microphone() as mic:
  
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            for index in AETOABChan:
                textCorrected = text.replace(index, "AETAOB-Chan")
            
    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue
    print(textCorrected)
    response = respond(textCorrected)
    print(response)
    speak(response)

#--Save File saving--
with open ('chatbotDatasetListUnchecked.txt', 'w') as f:
    for index in datasetListUnchecked:
        f.write(index.query)
        f.write(', ')
        f.write(str(index.response))
        f.write("\n")
 
  
    
