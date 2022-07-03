import speech_recognition as sr #For the robot to listen to our voice/speech 
import pyttsx3                  #To speak out, or text to speech 
import pywhatkit                #For advance control on browser
import wikipedia                #To get wikipedia data
import pyjokes                  #To get funny jokes
import datetime
import webbrowser
import os                       #acessing system files

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greetMe():
    hrs=int(datetime.datetime.now().hour) 
    if hrs>=0 and hrs<12:
        talk('Good Morning Pratik')
    elif hrs>=12 and hrs<18:
        talk('Good Afternoon Pratik')
    else:
        talk('Good Evening Pratik')

greetMe()
talk('I am your Lappy')
talk('What can I do for you')
my_mic =sr.Microphone(device_index=1)
def take_command():
    try:
        with my_mic as source:
            print('listening...')
            # listener.pause_threshold=1
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'lappy' in command:
                command = command.replace('lappy', '')
                print(command)
    except:
        pass
    return command


def runLappy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open sublime' in command:
        path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text.lnk"
        os.startfile(path)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'search' in command:
        query=command.replace('search','')
        pywhatkit.search(query)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk('According to wikipedia'+ info)

    elif 'what is' in command:
        about = command.replace('what is', '')
        info = wikipedia.summary(about, 1)
        print(info)
        talk('According to wikipedia'+ info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with your laptop')

    elif 'bye' in command:
        talk('good bye sir,Have a great day')
        exit()
    else:
        talk('Sorry sir I can not hear you can you please say again.')

while True:
    runLappy()