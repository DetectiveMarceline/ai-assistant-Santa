import tkinter as tk
import speech_recognition as sr
import elevenlabs
import pywhatkit
import datetime
import wikipedia
import pyjokes
from PIL import ImageTk, Image  

API_KEY = "09a99ff8df8cbb75892d115b0adad3ea"
listener = sr.Recognizer()
elevenlabs.set_api_key(API_KEY)

def talk(greet):
    elevenlabs_audio = elevenlabs.generate(text=greet, voice="🎅 Santa Claus")
    elevenlabs.play(elevenlabs_audio)


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'santa' in command:
                command = command.replace('santa', '')
    except Exception as e:
        print("Error during speech recognition:", e)
        return ""

    return command

def process_command(command):
    if 'hi' in command or 'hello' in command:
        talk('Ho ho ho! Hello there! How can I help you?')
    elif 'how are you' in command:
        talk('I\'m feeling jolly, thank you for asking! How are you?')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing a merry tune for you: ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('The time is now ' + time)
    elif 'who' in command or 'what' in command:
        thing = command.replace('who', '').replace('what', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk('Here\'s a joke to make you chuckle:')
        talk(pyjokes.get_joke())
    elif 'goodbye' in command or 'bye' in command:
        talk('Merry Christmas and farewell!')
        return False  
    else:
        talk('I didn\'t catch that. Could you please try again?')
    return True

def run_santa():
    while True:
        command = take_command()
        print(command)
        if not process_command(command):
            break

root = tk.Tk()
root.title("Santa's Workshop")

santa_image = Image.open("C:\\Users\\marce\\Desktop\\ai assistant proj\\Untitled.png")

resized_image = santa_image.resize((200, 200)) 
santa_photo = ImageTk.PhotoImage(resized_image)
santa_label = tk.Label(root, image=santa_photo)
santa_label.pack()

listen_button = tk.Button(root, text="Listen to Santa", command=run_santa)
listen_button.pack()

response_label = tk.Label(root, text="Santa is waiting for your command...")
response_label.pack()

root.mainloop()
