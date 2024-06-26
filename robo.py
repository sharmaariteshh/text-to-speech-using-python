import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        a = input("Enter the text you want to hear (type 'q' to quit): ")
        if a.lower() == 'q':
            speak("Goodbye friend")
            break
        speak(a)
