import speech_recognition as sr

from tempfile import TemporaryFile as tempf

from pydub import AudioSegment

from pydub.playback import play

from io import BytesIO

from gtts import gTTS

import os

path_to_ffmpeg = os.getcwd() + "\\bin\\ffmpeg.exe"
print(path_to_ffmpeg)
#AudioSegment.converter = path_to_ffmpeg
r = sr.Recognizer()
i=0
while True:
    i+= 1
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    text = r.recognize_google(audio)
    print(f"You said {text}")

    
    tts = gTTS(text=text, lang="en")
    f = BytesIO()
    tts.write_to_fp(f)
    f.seek(0)

    sound = AudioSegment.from_file(f, format="mp3")
    play(sound)