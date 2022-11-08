#import pyttsx3
from gtts import gTTS
from PyPDF2 import PdfFileReader


pdf = input("Please Enter a pdf file: ")
mp3Name = input("Please Enter a mp3 file name: ")
#engine = pyttsx3.init()

with open(pdf, mode='rb') as f:
    fullText = ""
    reader = PdfFileReader(f)
    for x in range(reader.getNumPages()):
        page = reader.getPage(x)
        text = page.extractText()
        fullText += text
        #engine.save_to_file(text, 'zedd.mp3')
        #engine.runAndWait()

mp3File = gTTS(text=fullText, lang='en', slow=False)

mp3File.save((mp3Name + ".mp3"))
#engine.stop()
