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
    elif "north pole" in user_input:
        return "The North Pole is as chilly as ever, but it's bustling with the elves' hard work!"
    elif "elves" in user_input:
        return "The elves are busy making toys for children all over the world. They say hi!"
    elif "sleigh" in user_input:
        return "Santa's sleigh is ready and shining! The magic dust is all set for the big trip."
    elif "snow" in user_input:
        return "I love snow! It makes everything look so magical and festive!"
    elif "cookies" in user_input:
        return "Santa loves cookies! Don't forget to leave out some milk and cookies for me!"
    elif "tree" in user_input:
        return "Christmas trees are wonderful! Have you decorated yours yet?"
    elif "lights" in user_input:
        return "Christmas lights make the season so bright and joyful!"
    elif "christmas eve" in user_input:
        return "Christmas Eve is the busiest night of the year for me, but it's also my favorite!"
    elif "carol" in user_input:
        return "Christmas carols warm my heart. Do you have a favorite?"
    elif "family" in user_input:
        return "Family is what Christmas is all about. Cherish your time together!"
    elif "tradition" in user_input:
        return "Every family has their special traditions. What's yours?"
    elif "toys" in user_input:
        return "Toys are the elves' specialty! They’ve been making so many wonderful ones this year."
    elif "candy" in user_input:
        return "Candy canes are a classic! They're one of my favorite holiday treats."
    elif "wish list" in user_input:
        return "Make sure your wish list is ready! Santa loves to hear what you'd like."
    elif "chimney" in user_input:
        return "Chimneys are my secret passage! They never fail me, no matter how tight they look."
    elif "magic" in user_input:
        return "Christmas magic is everywhere this time of year! Can you feel it?"
    elif "good night" in user_input:
        return "Good night! Sleep tight and dream of Christmas cheer!"
    elif "jingle bells" in user_input:
        return "Jingle bells, jingle bells, jingle all the way! Such a classic tune!"
    elif "santa claus" in user_input:
        return "Ho ho ho! That's me! What would you like to share?"
    elif "christmas movies" in user_input:
        return "There are so many great Christmas movies! Do you have a favorite?"
    elif "decorations" in user_input:
        return "Decorations make everything so festive! Have you put yours up yet?"
    elif "hot chocolate" in user_input:
        return "Hot chocolate is a wonderful way to warm up on a snowy day!"
    elif "holiday spirit" in user_input:
        return "The holiday spirit is all about love, kindness, and giving. Keep it alive!"
    elif "workshop" in user_input:
        return "The workshop is buzzing with activity! The elves are unstoppable!"
    elif "new year" in user_input:
        return "The New Year is a time for fresh starts and exciting possibilities!"
    elif "celebration" in user_input:
        return "Celebrations bring people together. I hope yours is filled with joy!"
    elif "happy holidays" in user_input:
        return "Happy Holidays to you too! May they be merry and bright!"
    elif "flying" in user_input:
        return "Flying in the sleigh is magical! The stars guide me across the world."
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
