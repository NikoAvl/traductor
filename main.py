import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

#Se crea y configura el traductor
traductor = GoogleTranslator(source="auto", target="en") 

#Se crea y configura el oyente 
oyente = sr.Recognizer() 
oyente.pause_threshold = 2.0 #Intervalo de silencio antes de que se corte el audio 

#Se crea y configura el narrador 
narrador = pyttsx3.init()
narrador.setProperty("rate", 110)
narrador.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0") #SE ESTABLECE LA VOZ DEL NARRADOR EN INGLES

with sr.Microphone() as source:
    print("Di algo: ")
    audio = oyente.listen(source)
    

try:
    texto = oyente.recognize_google(audio, language="es-ES")
    
    traduccion_texto = traductor.translate(texto)

    narrador.say(traduccion_texto)
    narrador.runAndWait()
except:
    print("Lo siento, no te he entendido")
  