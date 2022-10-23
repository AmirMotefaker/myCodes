# Code by @AmirMotefaker

# Convert Text to Speech

# Solution 1
from gtts import gTTS
from playsound import playsound
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
# playsound: Pure Python, cross platform, single function module with no dependencies for playing sounds.

# in english
tts = gTTS('hello world')
tts.save('hello.mp3')
playsound("hello.mp3")

# in spanish
tts = gTTS('Hola Mundo', lang='es')
tts.save('hola.mp3')
playsound("hola.mp3")



# Solution 2
from gtts import gTTS
import os   # os: play the converted audio
  
text = 'Welcome to Visual Studio Code!'
  
language = 'en'

my_object = gTTS(text=text, lang=language, slow=False)
my_object.save("welcome.mp3")
  
os.system("welcome.mp3")
