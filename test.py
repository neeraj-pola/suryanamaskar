import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 145)  

engine.say('great job! move on to next pose now. ')

engine.runAndWait()