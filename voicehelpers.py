"""
Implements helpers regarding text to speech and speech to text.
"""
import speech_recognition as sr
from gtts import gTTS

from io import BytesIO

from pydub import AudioSegment
from pydub.playback import play

_r = sr.Recognizer()

def get(indefinite = False, online = True) -> str:
    """
    Gets the line of voice said into the microphone.
    :param arg1: Specify whether the function should recursively call if
                no audio was captured.
    :param arg2: Specify whether Google's speech recogntion API will be used. If set
                to false, will use Sphinx offline speech recognition
    """

    assert online, "Currently, only Google's API is working. Please set to online mode."

    with sr.Microphone() as source:
        print("Listening...")
        
        audio = _r.listen(source)
    
    text = ""
    try:
        if online:
            text = _r.recognize_google(audio)
        else:
            text = _r.recognize_sphinx(audio)
        
        if not text and indefinite:
            return get(indefinite, online)

        return text
    except Exception as e:
        # We assume that this exception occurred because no text was recognised.
        if indefinite:
            return get(indefinite, online)
        return ""

def say(text: str) -> None:
    if not text: return
    tts = gTTS(text=text, lang="en")
    f = BytesIO()
    tts.write_to_fp(f)
    f.seek(0)
    sound = AudioSegment.from_file(f, format="mp3")
    play(sound)