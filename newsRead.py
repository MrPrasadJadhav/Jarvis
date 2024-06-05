import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3f9e23bc98424fc0b78504b3396cf1a5",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3f9e23bc98424fc0b78504b3396cf1a5",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3f9e23bc98424fc0b78504b3396cf1a5",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3f9e23bc98424fc0b78504b3396cf1a5",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3f9e23bc98424fc0b78504b3396cf1a5",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3f9e23bc98424fc0b78504b3396cf1a5"
               } 
    
    content = None
    url = None
    speak("Which field news do you want, [business],[entertainment],[health],[science],[sports],[technology]")
    field = input("Type of field newsthat you want :")
    for key,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("here is the first news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit : {news_url}")

        a= input("[press 1 to count] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

        speak("Thats all")