import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Please speak... Press 'q' and Enter to quit.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        
        # Continuously listen for speech input
        while True:
            audio = recognizer.listen(source)  # Listen for audio input

            try:
                text = recognizer.recognize_sphinx(audio)  # Use CMU Sphinx for speech recognition
                print("You said:", text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")
            except sr.RequestError as e:
                print("Error with the speech recognition service; {0}".format(e))
            
            # Check for user input in the terminal
            user_input = input()
            if user_input.lower() == 'q':
                break  # Exit loop if 'q' is input

# Call the function to convert speech to text
speech_to_text()