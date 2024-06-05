import subprocess
import time
import pyttsx3
engine = pyttsx3.init()
if __name__=='__main__':
    while True:
        def sendmessage(message):
            subprocess.Popen(['notify-send', message])
            return         
        engine.say('Drik water')
        engine.runAndWait()
        sendmessage('Time to drink water.\U0001F609\nIt is healthy for yoy to dirnk water regularly')
        time.sleep(5)
       