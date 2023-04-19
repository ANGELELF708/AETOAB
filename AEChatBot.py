from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition
import pyttsx3
import engineio
import AETOABChatDatasetList
from AETOABChatDatasetList import datasetList, datasetListUnchecked
import time
time.clock = time.time 

#USE TKINTER FOR GUI IN FUTURE

#--CHATBOT STUFF--
chatbot = ChatBot("AETOAB-Chan") #creates the bot object and names it

#Training: 
trainer = ListTrainer(chatbot)
for index in datasetList:
    trainer.train([
        index.query, index.response
    ])

#set-up
exit_conditions = (":q", "quit", "exit")

AETOABChan = ["i-80 john", "youtube", "80's song", "i-80", "dub john", "tub john", "a chong", "age of john", "280 john", "8010", "hey john", "uh-oh john"] #use this list for voice recognition correction later
contentFilter = ["nigger", "nigga", "fuck", "shit", "bitch", "motherfucker", "ass", "asshole", "dick", "pussy"] #ONLY HERE TO STOP IT FROM USING AND LEARNING BAD WORDS!!!!!!!
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
while True: #replace while true with function
#if get speech recognition
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
    query = textCorrected
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        for index in contentFilter:
            responseFiltered = str(response.replace(index, "*"))
        print(str(responseFiltered))
        speak(str(responseFiltered))
        newData = AETOABChatDatasetList.ChatDataset(query, response)
        datasetListUnchecked.append(newData) #update in future to save this dataset for review and possible inclusion in datasetList
        #recur function
    #else check twitch/discord 
        #recur function
#--Save File--
with open ('chatbotDatasetListUnchecked.txt', 'w') as f:
    for index in datasetListUnchecked:
        f.write(index.query)
        f.write(', ')
        f.write(str(index.response))
        f.write("\n")
 
  