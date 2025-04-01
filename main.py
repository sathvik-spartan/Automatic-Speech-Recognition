import speech_recognition as sr  

# Initialize recognizer  
recognizer = sr.Recognizer()  

# Capture real-time audio  
with sr.Microphone() as source:  
    print("Speak something...")  
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise  
    audio = recognizer.listen(source)  

# Convert speech to text  
try:  
    text = recognizer.recognize_google(audio)  # Using Google Speech Recognition API  
    print("You said:", text)  
except sr.UnknownValueError:  
    print("Sorry, could not understand the audio.")  
except sr.RequestError:  
    print("Could not request results from Google API.")  
