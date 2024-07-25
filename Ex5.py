#input
import time
from gtts import gTTS
from pygame import mixer
language = 'ar'
words={"door":"باب",
       "window":"شباك",
       "play":"يلعب"}
mixer.init()
while True:
    user_input=input("english word: ")
    #peocessing
    arabic_word=words[user_input]
    translation = gTTS(text=arabic_word, lang=language, slow=False)
    translation.save("translation.mp3")
    mixer.music.load("translation.mp3")
    mixer.music.set_volume(.7)
    #output
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
            
    mixer.music.stop()
    mixer.music.unload()