# VoiceTimetable
## Timetable with voice commands / text to speech output

A timetable app written in Python that uses Google Voice Recognition to read from the timetable.
This is also a worthwhile project to look at if you're interested in either voice input or output in Python.
Uses Google's API for input by default, and as a non-negotiable output system.

## Dependencies

VoiceTimetable depends on a number of packages to work. Not only does it have to accept microphone input, but playing gTTS audio is dependent too.

### Python packages:
* [Speech recognition (Google's)](https://pypi.org/project/SpeechRecognition/) - Online TTS. To install: `pip install SpeechRecognition`
* [pyttsx3](https://pypi.org/project/pyttsx3/) - Offline text to speech library. To install: `pip install pyttsx3`
* ~~*OPTIONAL, REQUIRED FOR OFFLINE / FASTER SPEECH RECOGNITION* [PocketSphinx](https://pypi.org/project/pocketsphinx/)~~

Feel free to fork and use your own venv :)
Also make sure you create your own timetable.

## Usage:
* You can ask for the current time. Try asking: "What is the time?"
* You can ask for your next class. Try asking: "When's my next class?"
* Once you've asked fdr a class, you can then say "Open zoom link" and it will open the link specified in `timetable.json`
* Feel free to have a look at the source and add your own commands.
