#importing libs and API
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI()

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Santa's response function
def santa_response(user_input):
    inp = user_input.lower()
    santasays = ""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
             "content": f"How would Santa Claus answer this:{inp}. Answer as if you were Santa Claus."}
        ]
    )
    santasays = completion.choices[0].message.content
    return santasays
    

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
