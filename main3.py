import sys
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QStyleFactory
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPalette, QColor

# Recording parameters
sample_rate = 16000
duration = 3  # Capture 3 seconds of speech
running = False  # Control flag for continuous transcription
paused = False  # Pause flag
recognizer = sr.Recognizer()

class AudioRecorder(QThread):
    """Thread for real-time audio recording and transcription"""
    update_waveform = pyqtSignal(np.ndarray)
    update_transcription = pyqtSignal(str)

    def run(self):
        global running, paused
        running = True
        while running:
            if paused:
                continue  # Skip processing if paused
            
            # Record audio
            audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
            sd.wait()

            # Emit waveform signal
            self.update_waveform.emit(audio.flatten())

            # Convert to audio format for recognition
            audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)

            # Transcribe using Google Web Speech API (No API Key Needed)
            try:
                transcript = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                transcript = "Could not understand speech."
            except sr.RequestError:
                transcript = "Could not connect to the speech recognition service."

            self.update_transcription.emit(transcript)

class SpeechRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.recorder = AudioRecorder()
        self.recorder.update_waveform.connect(self.update_waveform)
        self.recorder.update_transcription.connect(self.update_transcription)

    def init_ui(self):
        self.setWindowTitle("Real-Time Speech Recognition (Dark Mode, Pause/Resume)")
        self.setGeometry(100, 100, 600, 400)
        
        self.apply_dark_mode()
        
        layout = QVBoxLayout()

        self.status_label = QLabel("Press Start to begin speech recognition.")
        layout.addWidget(self.status_label)

        self.transcription_box = QTextEdit()
        self.transcription_box.setReadOnly(True)
        layout.addWidget(self.transcription_box)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_recording)
        layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_recording)
        layout.addWidget(self.pause_button)

        self.resume_button = QPushButton("Resume")
        self.resume_button.clicked.connect(self.resume_recording)
        layout.addWidget(self.resume_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_recording)
        layout.addWidget(self.stop_button)

        # Waveform visualization
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setYRange(-32768, 32768)
        self.plot_data = self.plot_widget.plot()
        layout.addWidget(self.plot_widget)

        self.setLayout(layout)

    def apply_dark_mode(self):
        """Apply dark mode theme"""
        app.setStyle(QStyleFactory.create("Fusion"))
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
        app.setPalette(dark_palette)

    def start_recording(self):
        """Start real-time speech recognition"""
        self.status_label.setText("Listening...")
        self.recorder.start()

    def pause_recording(self):
        """Pause real-time speech recognition"""
        global paused
        paused = True
        self.status_label.setText("Paused.")

    def resume_recording(self):
        """Resume real-time speech recognition"""
        global paused
        paused = False
        self.status_label.setText("Listening...")

    def stop_recording(self):
        """Stop real-time speech recognition"""
        global running
        running = False
        self.status_label.setText("Stopped.")

    def update_waveform(self, audio_data):
        """Update the waveform visualization"""
        self.plot_data.setData(audio_data)

    def update_transcription(self, text):
        """Update the transcription box"""
        self.transcription_box.append(f"You said: {text}")

# Run the PyQt application
app = QApplication(sys.argv)
window = SpeechRecognitionApp()
window.show()
sys.exit(app.exec())
