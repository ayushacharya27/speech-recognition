import speech_recognition as sr

def Speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something....")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's Speech Recognition API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("Sorry, there was an issue with the API.")


