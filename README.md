# Automatic-Speech-Recognition

# Real-Time Speech Recognition App

This project demonstrates real-time speech-to-text transcription using Python, integrated with a GUI, waveform visualization, and pause/resume functionality.

## Prominent Features

- Live Speech Recognition using Google Speech API (no API key needed)
- Real-time waveform visualization
- Dark mode GUI with PyQt6
- Pause/Resume/Stop controls
- Transcription updates in real-time

## Files Overview

| File       | Description |
|------------|-------------|
| `main.py`  | Basic speech-to-text using Google API (one-time input). |
| `main2.py` | Real-time continuous transcription from the microphone. |
| `main3.py` | PyQt6 GUI app with waveform, dark mode, controls, and transcription box. |
| `test.py`  | Audio recording and playback test script using `sounddevice`. |

## Requirements

Install dependencies using pip:

```bash
pip install sounddevice numpy speechrecognition pyqt6 pyqtgraph
```

### Choose your own ways to run the files:

1. GUI App (main3.py)
```bash
python main3.py
```

2. Test Audio Input/Output (test.py)
```bash
python test.py
```

3. Continuous CLI-based Recognition (main2.py)
```bash
python main2.py
```

4.. One-shot Recognition (main.py)
```
python main.py
```
---

Notes:
Uses Google Web Speech API (internet required).

No API key needed.

Dark mode is pre-applied for better visual aesthetics.

---


## Future Improvements

- Add support for offline recognition (e.g., Whisper).

- Integrate with other speech APIs.

- Enhance GUI with recording levels, export options.

---

## Contribution

Contributions are most welcome! 

If you'd like to improve this project, feel free to:

- Fork the repository
- Create a new branch
- Make your changes
- Commit your updates
- Submit a pull request

> Please make sure your code follows clean coding practices and includes proper documentation where necessary.

> For major changes, open an issue first to discuss what you would like to change.

Thank you for contributing to this Automatic Speech Recognition project!
