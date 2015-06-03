import pygame
#from sys import argv
from gtts import gTTS
from enchant import request_dict
try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract
#from tesseract import image_to_string
sentence=pytesseract.image_to_string(Image.open('saying.jpg'))
gb_dict = request_dict('en_gb')
us_dict = request_dict('en_us')
new=''.join(sentence)
sen=new.split()

for word in sen:
     if gb_dict.check(word) or us_dict.check(word):
        print word, " "
	tts=gTTS(text=word,lang='en')
	tts.save("result.mp3")
	file='result.mp3'
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
    		pygame.time.Clock().tick(10)

     else:
        print  " %s " % \
            (gb_dict.suggest(word)[0])
	tts=gTTS(text=word,lang='en')
        tts.save("result.mp3")
	file='result.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

#print(pytesseract.image_to_string(Image.open('para.jpg')))
