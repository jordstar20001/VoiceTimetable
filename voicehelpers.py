"""
Implements helpers regarding text to speech and speech to text.
"""
import speech_recognition as sr
from gtts import gTTS

from io import BytesIO

from pydub import AudioSegment
from pydub.playback import play

import pyttsx3

import random

_r = sr.Recognizer()

engine = pyttsx3.init()

def get(prompt = "", indefinite = False, online = True, vocal = False) -> str:
    """
    Gets the line of voice said into the microphone.
    :param arg1: Specify whether the function should recursively call if
                no audio was captured.
    :param arg2: Specify whether Google's speech recogntion API will be used. If set
                to false, will use Sphinx offline speech recognition
    """

    assert online, "Currently, only Google's API is working. Please set to online mode."

    with sr.Microphone() as source:
        if prompt:
            print(prompt)
        
        audio = _r.listen(source)
    
    text = ""
    try:
        if online:
            text = _r.recognize_google(audio)
        else:
            text = _r.recognize_sphinx(audio)

        return text

    except Exception as e:
        # We assume that this exception occurred because no text was recognised.
        if indefinite:
            if vocal:
                say(random.choice(["I didn't catch that", "You there?", "Hello?", "Are you stupid? Talk already!"]))
            return get("Sorry, I didn't catch that...", indefinite, online, vocal=vocal)
        return ""

def say_google(text: str) -> None:
    if not text: return
    tts = gTTS(text=text, lang="en-nz")
    f = BytesIO()
    tts.write_to_fp(f)
    f.seek(0)
    sound = AudioSegment.from_file(f, format="mp3")
    play(sound)

def say(text: str, rate = 150, female = True) -> None:
    if not text: return
    engine.setProperty("rate", rate)
    if female:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
    engine.say(text)
    engine.runAndWait()