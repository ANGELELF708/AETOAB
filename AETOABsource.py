from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import AETOABChatDatasetList
from AETOABChatDatasetList import datasetList
import re

#--CHATBOT STUFF--
chatbot = ChatBot("AETOAB-Chan") #creates the bot object and names it (and yes this does need to be called twice because im a terribe programmer)


def setup():
    chatbot = ChatBot("AETOAB-Chan") #creates the bot object and names it (and yes this does need to be called twice because im a terribe programmer)
    trainer = ListTrainer(chatbot)
    for index in datasetList:
        trainer.train([
            index.query, index.response
        ])
#set-up
exit_conditions = (":q", "quit", "exit")
contentFilter = ["nigger", "nigga", "fuck", "shit", "bitch", "motherfucker", "ass", "asshole", "dick", "pussy", "faggot", "fag", "nazi", "nager", "osama", "laden", "hitler", "twin towers", "osama bin laden", "fa.g", "monkey", "meth"]

def respond(input):
    query = input
    response = chatbot.get_response(query)
    #for word in contentFilter:
        #response = response.lower()
        #response = response.sub('***', response)
    return response

AETOABChan = ["i-80 john", "youtube", "80's song", "i-80", "dub john", "tub john", "a chong", "age of john", "280 john", "8010", "hey john", "uh-oh john"] #use this list for voice recognition correction later