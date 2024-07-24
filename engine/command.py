# import pyttsx3
# import speech_recognition as sr
# def speak(text):
#     engine = pyttsx3.init('sapi5')
#     voices=engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 174)
#     print(voices)

#     engine.say(text)
#     engine.runAndWait()
# def takencommand():
#     r=sr.Recognizer
#     with sr.Microphone() as source:
#      print('listening . . .')
#      r.pause_threshold=1
#      r.adjust_for_ambient_noise(source)
#      audio=r.listen(source,10,6)
#     try:
#        print('recognizing')
#        query=r.recognize_google(audio,language="en-in")
#        print(f"user said:{query}")
#     except Exception as e:
#        return ""
#     return query.lower()
# text=takencommand()

# speak(text)
import pyttsx3

import speech_recognition as sr
import eel
import time



def speak(text):
    text=str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)  

    engine.say(text)
    # eel.recieverText(text)
    engine.runAndWait()


def takencommand():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        print('listening . . .')
        eel.DisplayMessage('listening . . .')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing')
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")
        eel.DisplayMessage(query)                                
        time.sleep(2)
        
    except Exception as e:
        return ""
    return query.lower()

# text = takencommand()
# speak(text)

@eel.expose
def allCommands(message=1):
    if message==1:
        query=takencommand()
        print(query)
        eel.senderText(query)
    else:
        query=message
        eel.senderText(query)


    try:
        
        
        if "open" in query:
            print("Command contains 'open': i-run")
            from engine.feature import openCommand 
            openCommand(query)
        elif "on youtube":
            from engine.feature import playYouTube
            playYouTube(query)
       
        
       
        else:
            
#            url = "http://huggingface.co"
#            cookies_json='''
#            [
#     {
#         "domain": ".huggingface.co",
#         "expirationDate": 1753339590,
#         "hostOnly": false,
#         "httpOnly": false,
#         "name": "__stripe_mid",
#         "path": "/",
#         "sameSite": "strict",
#         "secure": true,
#         "session": false,
#         "storeId": null,
#         "value": "77494a84-a09a-47b5-aa4b-3ee2dc2790e7d438de"
#     },
#     {
#         "domain": ".huggingface.co",
#         "expirationDate": 1753106596.930565,
#         "hostOnly": false,
#         "httpOnly": true,
#         "name": "token",
#         "path": "/",
#         "sameSite": "lax",
#         "secure": true,
#         "session": false,
#         "storeId": null,
#         "value": "HKUlgAdlZuGjErSsAozCvPpkPawmwYrOkEnLZtcauUBISZUIMUsaKrMrbQmLICRXgzxednihxZfqFpXPugqscTXrIAfFArkaXTvOwmzqtozdmEeMYtEsfgWpLzoAMGLu"
#     },
#     {
#         "domain": ".huggingface.co",
#         "expirationDate": 1722154404,
#         "hostOnly": false,
#         "httpOnly": false,
#         "name": "aws-waf-token",
#         "path": "/",
#         "sameSite": "lax",
#         "secure": true,
#         "session": false,
#         "storeId": null,
#         "value": "6caa7cbb-dc60-46e6-99f8-15cab94e0b38:BQoApms5R1RpAAAA:vda/qzPdqecjwAYhbnLGJws8al81tXbeEGWjYr7F39b7aJKXEQ19vScw8LfGqtEQcUQV3ewPEeEuNgThNJDOPd7EWkvMjAorP0OIlPAzFwkyhfXpbkorWFv0CkZbuobARx051NWLjzCxn0r5BXANzwCICbm0zvdfxKODdDmR+lRQBnY4Ld8CC9Eq2jbArUBXuog25JQRU8tiqxZLvHNNS4U2c1ZA20xwaSAq50YMD1+UQT1/sF1u8bqKL1xrYWREaEkQrrM="
#     },
#     {
#         "domain": "huggingface.co",
#         "expirationDate": 1723020598.580188,
#         "hostOnly": true,
#         "httpOnly": true,
#         "name": "hf-chat",
#         "path": "/",
#         "sameSite": "no_restriction",
#         "secure": true,
#         "session": false,
#         "storeId": null,
#         "value": "2de768ae-95a9-417b-b76b-aa4286778de5"
#     },
#     {
#         "domain": "huggingface.co",
#         "expirationDate": 1753106596.930297,
#         "hostOnly": true,
#         "httpOnly": true,
#         "name": "token",
#         "path": "/",
#         "sameSite": "no_restriction",
#         "secure": true,
#         "session": false,
#         "storeId": null,
#         "value": "HKUlgAdlZuGjErSsAozCvPpkPawmwYrOkEnLZtcauUBISZUIMUsaKrMrbQmLICRXgzxednihxZfqFpXPugqscTXrIAfFArkaXTvOwmzqtozdmEeMYtEsfgWpLzoAMGLu"
#     }
# ]'''


    
                
                from engine.feature import chatBot
                chatBot(query)
        
    except:
        print("error")


    eel.ShowHood()