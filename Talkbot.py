# %%
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer as cbct
import speech_recognition as spr
import pyttsx3

# %%
bot=ChatBot('Jinosh Mon')
bot.set_trainer(cbct)

talk = pyttsx3.init()#initializing text to speech

# %%
bot.train('chatterbot.corpus.english')

# %%
while True:
    speech = spr.Recognizer() #create object for recognizer to take voice input
    mic = spr.Microphone()
    with mic as source:
        print('{} listening...'.format(bot.name))
        audio = speech.listen(source)
    try:
        message = speech.recognize_google(audio)
        print('You : {} '.format(message))
        if(message == 'Bye see you later'):
            reply = 'It was nice talking to you... See you soon...'
            print('{} : {}'.format(bot.name,reply))
            break
        else:
            reply = bot.get_response(message)
            print('{} : {}'.format(bot.name,reply))
    except:
        reply = 'Pardon, Can you repeat?'
        print('{} : {}'.format(bot.name,reply))
    

# %%
