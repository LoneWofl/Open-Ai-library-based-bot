import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai
from apikey import apikey
import datetime
import random
import numpy as np

engine = pyttsx3.init()

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Yash: {query}\n Bot: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-16k-0613",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-16k-0613",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred."

if __name__ == '__main__':
    print('Bot is active')
    say("Bot is active")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} and {min} minutes")

        elif "open chrome".lower() in query.lower():
            os.system(f"start C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif "open vpn".lower() in query.lower():
            os.system(f"start \Program Files (x86)\Kaspersky Lab\Kaspersky VPN 5.15")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Bot Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





while 1:
    print("Enter statement ")
    s=input()
    speaker.Speak(s)
    print("listening.....")
    query= takeCommand()
    sites=[["youtube","https://www.youtube.com/"], ["wikipedia","https://www.wikipedia.com"], ["google","https://www.google.com"]]
    for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
             say(f"Opening {site[0]} sir...")
             webbrowser.open(site[1])



    if "the time" in query:
        hour= datetime.datetime.now().strftime("%H")
        min= datetime.datetime.now().strftime("%M")
        say(f"The time is {hour} hours and {min} minutes")