import sounddevice as sd 
import numpy as np

duration = 5  # seconds
sample_rate = 16000  # 16 kHz, common for ASR

print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
sd.wait()
print("Recording finished. Playing back...")
sd.play(audio, samplerate=sample_rate)
sd.wait()
print("Playback finished.")
