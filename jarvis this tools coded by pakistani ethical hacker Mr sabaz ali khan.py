import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate', 150)  # Speech speed

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Greet the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    speak(f"{greeting}, Sir! I am JARVIS, created by the ethical hacker Mr. Sabaz Ali Khan. How may I assist you today?")

def take_command():
    """Take voice input from the user and return it as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again, please...")
            speak("Sorry, I didn't catch that. Please say again.")
            return "None"
        return query.lower()

def main():
    """Main function to run JARVIS"""
    wish_me()
    
    while True:
        query = take_command()
        
        if query == "none":
            continue
        
        # Exit command
        if 'exit' in query or 'stop' in query:
            speak("Goodbye, Sir. Have a great day!")
            break
        
        # Wikipedia search
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find that on Wikipedia.")
        
        # Open websites
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com") 
        
        # Tell time
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        
        # Play music (assumes a local music directory)
        elif 'play music' in query:
            music_dir = "C:\\Users\\Public\\Music"  # Update this path as needed
            try:
                songs = os.listdir(music_dir)
                if songs:
                    speak("Playing music")
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No music files found in the directory.")
            except Exception as e:
                speak("Sorry, I couldn't play music.")
        
        # Fallback for unrecognized commands
        else:
            speak("I'm not sure how to help with that. Please try another command.")

if __name__ == "__main__":
    # Print attribution
    print("JARVIS - Virtual Assistant")
    print("Coded by: Mr. Sabaz Ali Khan, Pakistani Ethical Hacker")
    print("Email: Sabazali236@gmail.com")
    
    # Run the assistant
    main()