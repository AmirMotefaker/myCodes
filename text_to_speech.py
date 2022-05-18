# Code by amotef@gmail.com

# Convert Text to Speech

from gtts import gTTS
from playsound import playsound
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
# playsound: Pure Python, cross platform, single function module with no dependencies for playing sounds.

# in english
# tts = gTTS('hello world')
# tts.save('hello.mp3')
# playsound("hello.mp3")

# in spanish
tts = gTTS('Hola Mundo', lang='es')
tts.save('hola.mp3')
playsound("hola.mp3")
