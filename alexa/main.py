import speech_recognition as sr
import pyttsx3
import pywhatkit as kit




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('what can i do for you')

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            print(source)
            voice = listener.listen(source)
            print(voice)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if "play" in command:
                print(command)
                song =  command.replace('play', '')
                print(song)
                kit.playonyt(song)
            if "search" in command:
                print(command)
                find =  command.replace('search', '')
                print(find)
                kit.search(find)
    except Exception as e:
        print(e)
        talk(e)
    
takeCommand()
# def run_alexa():
#     command = takeCommand()
#     if 'play' in command:
#         talk('song playing')
#         song = command.replace('play','')
#         print(f'playin {song}')

# run_alexa()