from gtts import gTTS
import os
f=open('audio.txt')
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge,slow=False)
audio.save("audio.wav")
os.system("audio.wav")