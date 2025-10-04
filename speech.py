import speech_recognition as sr

def rcp():
    recognizer = sr.Recognizer()

    #capturar audio desde el microfono
    with sr.Microphone() as f:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(f, duration=1)
        audio = recognizer.listen(f, phrase_time_limit=10)
        print ("reconociendo")


    try:
        #reconocimiento de voz utilizando la API de google
        texto = recognizer.recognize_google(audio, language="es-ES")
        return (f"Has dicho:",texto)


    except ValueError as e:
        return (f"Error de valo:",str(e))


resultado = rcp()
print(resultado)