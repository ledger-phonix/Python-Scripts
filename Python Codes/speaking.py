
import pyttsx3
engine=pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
names = ['Usama', 'Shehroz','Talha','Faseeh','Shozab','khubaib']
for name in names:
    engine.say(f'Hello dude! {name}')
engine.runAndWait()


# import pyttsx3    
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', 140)
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
# engine.say("what you want to say goes here")
    
# engine.runAndWait()




