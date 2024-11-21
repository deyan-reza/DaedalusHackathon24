import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Santa's response function
def santa_response(user_input):
    user_input = user_input.lower()
    if "merry christmas" in user_input:
        return "Ho ho ho! Merry Christmas to you too!"
    elif "gift" in user_input:
        return "Have you been good this year? Santa only brings gifts to the nice ones!"
    elif "reindeer" in user_input:
        return "Oh, Rudolph and the gang are doing great! They're resting for the big night."
    elif "thank you" in user_input:
        return "You're welcome! Keep spreading the holiday cheer!"
    elif "bye" in user_input:
        return "Goodbye! Have a merry Christmas!"
    else:
        return "Ho ho ho! Santa's listening! What else do you want to share?"

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Main interaction loop
def main():
    print("Santa is ready to chat! Speak into the microphone.")
    speak("Ho ho ho! Santa is ready to chat! Speak into the microphone.")
    while True:
        try:
            # Capture input from the microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                print("Processing...")

                # Recognize the speech using Google Web Speech API
                user_input = recognizer.recognize_google(audio)
                print(f"You said: {user_input}")

                # Get Santa's response
                response = santa_response(user_input)
                print(f"Santa says: {response}")

                # Speak the response
                speak(response)

                # End the chat if the user says "bye"
                if "bye" in user_input.lower():
                    print("Santa says: Goodbye! Have a merry Christmas!")
                    break
        except sr.UnknownValueError:
            print("Sorry, Santa didn't catch that. Can you say it again?")
            speak("Sorry, Santa didn't catch that. Can you say it again?")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Sorry, there seems to be an issue. Please try again later.")
            break

if __name__ == "__main__":
    main()
