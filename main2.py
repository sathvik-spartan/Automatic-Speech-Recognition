import speech_recognition as sr  

recognizer = sr.Recognizer()  
mic = sr.Microphone()  

def real_time_speech_recognition():  
    with mic as source:  
        recognizer.adjust_for_ambient_noise(source)  
        print("Listening for speech... (Press Ctrl+C to stop)")  
        
        while True:  
            try:  
                audio = recognizer.listen(source, timeout=5)  # Capture speech  
                text = recognizer.recognize_google(audio)  
                print("You said:", text)  
            except sr.UnknownValueError:  
                print("Sorry, could not understand the audio.")  
            except sr.RequestError:  
                print("API request error.")  
            except KeyboardInterrupt:  
                print("\nStopping real-time speech recognition.")  
                break  

real_time_speech_recognition()

#How it works :

''' 
1. Continuously listens for speech.
2. Transcribes speech in real time.
3. Stops when you press.

'''
