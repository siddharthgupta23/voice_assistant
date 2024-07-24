# import json
# import os
# import struct
# import time
# from playsound import playsound
# import eel
# import pyaudio
# # import requests
# from hugchat import hugchat
# import pywhatkit as kit

# from engine.command import speak
# from engine.config import ASSISTANT_NAME
# # from requests.cookies import RequestsCookieJar


# import sqlite3
# import webbrowser


# import pvporcupine

# from engine.helper import extract_yt_term;
# # from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
# # import torch

# con = sqlite3.connect("jarvis.db")
# cursor = con.cursor()


# @eel.expose

# def playAssistantSound():
#     music_dir="www\\assets\\audio\\www_assets_audio_start_sound.mp3"
#     playsound(music_dir)

# def openCommand(query):
#     query=query.replace(ASSISTANT_NAME,"")
#     query=query.replace("open","")
#     query=query.lower()
    
#     app_name = query.strip()

#     if app_name != "":

#         try:
#             cursor.execute(
#                 'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#             results = cursor.fetchall()

#             if len(results) != 0:
#                 speak("Opening "+query)
#                 os.startfile(results[0][0])

#             elif len(results) == 0: 
#                 cursor.execute(
#                 'SELECT url FROM web_content WHERE name IN (?)', (app_name,))
#                 results = cursor.fetchall()
                
#                 if len(results) != 0:
#                     speak("Opening "+query)
#                     webbrowser.open(results[0][0])

#                 else:
#                     speak("Opening "+query)
#                     try:
#                         os.system('start '+str(query))
#                     except:
#                         speak("not found")
#         except:
#             speak("some thing went wrong")
# def playYouTube(query):
#     search_term= extract_yt_term(query)
#     speak("Playing "+search_term+" on YouTube ")
#     kit.playonyt(search_term)

# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()
# # class HuggingFaceChatBot:
# #     def __init__(self, tokenizer, model, conversation_id):
# #         self.tokenizer = tokenizer
# #         self.model = model
# #         self.conversation_id = conversation_id

# #     def change_conversation(self, conversation_id):
# #         self.conversation_id = conversation_id

# #     def new_conversation(self):
# #         self.conversation_id = str(hash(int(time.time()))).split('x')[-1][:-1]  # Generate a random conversation ID





# # Load cookies from JSON




# # def load_model():
# #     tokenizer = AutoTokenizer.from_pretrained("T5_Base")
# #     model = TFAutoModelForSeq2SeqLM.from_pretrained("T5_Base")
# #     return tokenizer, model

# # def save_cookies(cookie_path, conversation_id, session_id, conversation_data):
# #     data = {
# #         "conversation_id": conversation_id,
# #         "session_id": session_id,
# #         "conversation_data": conversation_data
# #     }
# #     with open(cookie_path, 'w') as f:
# #         json.dump(data, f)

# # def chatot(query, conversation_id):
# #     user_input = query.lower()

# #     # Load the model and tokenizer
# #     tokenizer, model = load_model()

# #     # Check if we should load an existing conversation or start a new one
# #     if conversation_id is None:
# #         # Create a new conversation if no conversation ID was provided
# #         if not os.path.exists("engine/cookies.json"):
# #             chatbot = HuggingFaceChatBot(tokenizer, model)
# #             id = chatbot.new_conversation()
# #             save_cookies("engine/cookies.json", id, "", {})
# #             conversation_id = id

# #         # Load the conversation from cookies
# #         with open("engine/cookies.json", 'r') as f:
# #             data = json.load(f)
# #             conversation_id = data["conversation_id"]

# #     # Change the conversation in the chatbot
# #     chatbot = HuggingFaceChatBot(tokenizer, model)
# #     chatbot.change_conversation(conversation_id)

# #     # Generate a response from the chatbot
# #     inputs = tokenizer([user_input], padding=True, truncation=True)
# #     input_ids = torch.tensor(inputs['input_ids'][0]).unsqueeze(0)
# #     outputs = model.generate(input_ids, max_length=100, num_beams=4, early_stopping=True)
# #     output = tokenizer.decode(outputs[0])

# #     # Print and speak the response
# #     print(output)
# #     speak(output)

# #     # Update the conversation data in cookies
# #     with open("engine/cookies.json", 'r') as f:
# #         data = json.load(f)
# #         data["last_message"] = output
# #         save_cookies("engine/cookies.json", conversation_id, "", data)

# #     return output
# # url="http://huggingface.co"
# # # Example usage
# # cookies_json='''
# #            [
# #     {
# #         "domain": ".huggingface.co",
# #         "expirationDate": 1753339590,
# #         "hostOnly": false,
# #         "httpOnly": false,
# #         "name": "__stripe_mid",
# #         "path": "/",
# #         "sameSite": "strict",
# #         "secure": true,
# #         "session": false,
# #         "storeId": null,
# #         "value": "77494a84-a09a-47b5-aa4b-3ee2dc2790e7d438de"
# #     },
# #     {
# #         "domain": ".huggingface.co",
# #         "expirationDate": 1753106596.930565,
# #         "hostOnly": false,
# #         "httpOnly": true,
# #         "name": "token",
# #         "path": "/",
# #         "sameSite": "lax",
# #         "secure": true,
# #         "session": false,
# #         "storeId": null,
# #         "value": "HKUlgAdlZuGjErSsAozCvPpkPawmwYrOkEnLZtcauUBISZUIMUsaKrMrbQmLICRXgzxednihxZfqFpXPugqscTXrIAfFArkaXTvOwmzqtozdmEeMYtEsfgWpLzoAMGLu"
# #     },
# #     {
# #         "domain": ".huggingface.co",
# #         "expirationDate": 1722154404,
# #         "hostOnly": false,
# #         "httpOnly": false,
# #         "name": "aws-waf-token",
# #         "path": "/",
# #         "sameSite": "lax",
# #         "secure": true,
# #         "session": false,
# #         "storeId": null,
# #         "value": "6caa7cbb-dc60-46e6-99f8-15cab94e0b38:BQoApms5R1RpAAAA:vda/qzPdqecjwAYhbnLGJws8al81tXbeEGWjYr7F39b7aJKXEQ19vScw8LfGqtEQcUQV3ewPEeEuNgThNJDOPd7EWkvMjAorP0OIlPAzFwkyhfXpbkorWFv0CkZbuobARx051NWLjzCxn0r5BXANzwCICbm0zvdfxKODdDmR+lRQBnY4Ld8CC9Eq2jbArUBXuog25JQRU8tiqxZLvHNNS4U2c1ZA20xwaSAq50YMD1+UQT1/sF1u8bqKL1xrYWREaEkQrrM="
# #     },
# #     {
# #         "domain": "huggingface.co",
# #         "expirationDate": 1723020598.580188,
# #         "hostOnly": true,
# #         "httpOnly": true,
# #         "name": "hf-chat",
# #         "path": "/",
# #         "sameSite": "no_restriction",
# #         "secure": true,
# #         "session": false,
# #         "storeId": null,
# #         "value": "2de768ae-95a9-417b-b76b-aa4286778de5"
# #     },
# #     {
# #         "domain": "huggingface.co",
# #         "expirationDate": 1753106596.930297,
# #         "hostOnly": true,
# #         "httpOnly": true,
# #         "name": "token",
# #         "path": "/",
# #         "sameSite": "no_restriction",
# #         "secure": true,
# #         "session": false,
# #         "storeId": null,
# #         "value": "HKUlgAdlZuGjErSsAozCvPpkPawmwYrOkEnLZtcauUBISZUIMUsaKrMrbQmLICRXgzxednihxZfqFpXPugqscTXrIAfFArkaXTvOwmzqtozdmEeMYtEsfgWpLzoAMGLu"
# #     }
# # ]'''

# # def load_cookies_from_json(cookies_json):
# #     cookies_list = json.loads(cookies_json)
# #     jar = RequestsCookieJar()
    
# #     for cookie in cookies_list:
# #         jar.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'], secure=cookie['secure'])
    
# #     return jar

# # def make_request_with_cookies(url, cookies_json):
# #     jar = load_cookies_from_json(cookies_json)
# #     response = requests.get(url, cookies=jar)
# #     return response

# # response = make_request_with_cookies(url, cookies_json)
# # print(response.status_code)

# # print(response.content)


# import hugchat

# def chatBot(query):
#     user_input = query.lower()
#     a = str(user_input)
#     chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response = chatbot.chat(a)
#     print(response)
#     # speak(response)  # Uncomment if you have a speak function implemented
#     return response


import json
import os
import struct
import time
from playsound import playsound
import eel
import pyaudio
from hugchat import hugchat
import pywhatkit as kit

from engine.command import speak
from engine.config import ASSISTANT_NAME
import sqlite3
import webbrowser
import pvporcupine

from engine.helper import extract_yt_term

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)
  

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()
    
    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + app_name)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_content WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening " + app_name)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + app_name)
                    try:
                        os.system('start ' + str(app_name))
                    except:
                        speak("not found")
        except:
            speak("something went wrong")

def playYouTube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"]) 
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)
        
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("hotword detected")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# def chatBot(query):
#     speak("I am Listening")
#     user_input = str(query.lower())
#     chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response = chatbot.chat(user_input)
    
#     speak(response)
#     print(response)# Uncomment if you have a speak function implemented

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
            
            
            
     
response=chatBot("Introduce yourself in about 100 words")
print(response)
speak(response) 

