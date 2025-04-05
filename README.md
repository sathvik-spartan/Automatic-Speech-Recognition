# Automatic-Speech-Recognition

# 🎙️ Real-Time Speech Recognition App

This project demonstrates real-time speech-to-text transcription using Python, integrated with a GUI, waveform visualization, and pause/resume functionality.

## 🧠 Features

- 🎤 Live Speech Recognition using Google Speech API (no API key needed)
- 📊 Real-time waveform visualization
- 🌓 Dark mode GUI with PyQt6
- ⏸️ Pause/Resume/Stop controls
- 📜 Transcription updates in real-time

## 📁 Files Overview

| File       | Description |
|------------|-------------|
| `main.py`  | Basic speech-to-text using Google API (one-time input). |
| `main2.py` | Real-time continuous transcription from the microphone. |
| `main3.py` | PyQt6 GUI app with waveform, dark mode, controls, and transcription box. |
| `test.py`  | Audio recording and playback test script using `sounddevice`. |

## 📦 Requirements

Install dependencies using pip:

```bash
pip install sounddevice numpy speechrecognition pyqt6 pyqtgraph

🚀 How to Run

🖥️ GUI App (main3.py)
- python main3.py

🧪 Test Audio Input/Output (test.py)
- python test.py

🔁 Continuous CLI-based Recognition (main2.py)
- python main2.py

🎙️ One-shot Recognition (main.py)
- python main.py

📌 Notes
Uses Google Web Speech API (internet required).

No API key needed.

Dark mode is pre-applied for better visual aesthetics.

🛠️ Future Improvements
Add support for offline recognition (e.g., Whisper).

Integrate with other speech APIs.

Enhance GUI with recording levels, export options.
