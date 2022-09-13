import speech_recognition as sr
import pyttsx3

name = 'monday'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            print('Escucha esto: ' + rec)
            if name in rec:
                rec = rec.replace(name, '')
                print('Haz dicho:' + rec)
    except: 
        pass
    return rec
    
 
def play():
    rec = listen()
    if 'play' in rec:
        num = rec.replace('play', '')
        talk('jugando' + num)
        print(num)
        if num == '  uno' or num == ' 1':
            return 1
        elif num == '  dos' or num == ' 2':
            return 2
        elif num == '  tres' or num == ' 3':
            return 3
        elif num == '  cuatro' or num == ' 4':
            return 4
        elif num == '  cinco' or num == ' 5':
            return 5
        elif num == '  six' or num == '  6':
            return 6
        elif num == '  siete' or num == ' 7':
            return 7
        elif num == '  ocho' or num == ' 8':
            return 8
        elif num == '  nine' or num == ' 9':
            return 9
        else:
            return 0
    else:
        return 0
