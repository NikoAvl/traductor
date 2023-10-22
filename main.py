import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


r = sr.Recognizer()
narrador = pyttsx3.init()
traductor = GoogleTranslator(source='es', target='en')
r.pause_threshold = 4.0
narrador.setProperty('rate', 120)


with sr.Microphone() as source:

    print("Di algo: ")

    audio = r.listen(source)
    

try:
    texto = r.recognize_google(audio, language='es-ES')
    
    traduccion_texto = traductor.translate(texto)

    narrador.say(traduccion_texto)
    narrador.runAndWait()
except:
    print("Lo siento, no te he entendido")
  