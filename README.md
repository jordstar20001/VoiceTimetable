# VoiceTimetable
## Timetable with voice commands / text to speech output

A timetable app written in Python that uses Google Voice Recognition to read from the timetable.
This is also a worthwhile project to look at if you're interested in either voice input or output in Python.
Uses Google's API for input by default, and as a non-negotiable output system.

## Dependencies

VoiceTimetable depends on a number of packages to work. Not only does it have to accept microphone input, but playing gTTS audio is dependent too.

### Python packages:
* [pydub](https://github.com/jiaaro/pydub) - **REQUIRES FFMPEG to play MP3 files**, see below!
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - uses [Google's Speech API](https://cloud.google.com/speech-to-text/) by default.
  * Option to use offline speech recognition with [Sphinx](https://cmusphinx.github.io/) *which is included with this library, I think...* It should be noted that this will increase the speed of the program, but may be less reliable.
* [gtts](https://pypi.org/project/gTTS/) - Google Text To Speech using Google Translate Engine. Of course, this requires an internet connection.
### System packages:
* [FFMPEG](https://ffmpeg.org/) (for audio playback)
  * Requires ffmpeg and ffprobe executeables. For some reason, ffplay is not required for pydub
  * Can be found currently under test/ffmpeg
* [PYAUDIO](https://pypi.org/project/PyAudio/) ("provides Python bindings for [PortAudio](http://www.portaudio.com/)")
  * It is recommended that you use conda to install PyAudio, as it requires certain C++ headers from portaudiolib, and this can be a hassle to install manually.
  Installation via conda is simple: `conda install pyaudio`

Please note, for GIT reasons, no venv is provided, but feel free to fork and use your own venv :) 
