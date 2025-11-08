🧠 AI Interview Coach

An intelligent desktop app built with Python + Tkinter + AI models that analyzes your speech, posture, eye contact, and sentiment in real-time or from recorded videos — helping you improve your interview performance.

🚀 Features

✅ 🎙 Live Interview Mode – Record via webcam + mic with real-time subtitles and live sentiment color feedback (green, red, white).
✅ 📂 Recorded Video Analysis – Upload any pre-recorded interview video to get a complete AI-generated report.
✅ 📊 Smart Report Dashboard – Displays:

Posture Score

Eye Contact Score

Speech Sentiment Score

Overall Interview Confidence
✅ 🧍 Posture & Eye Tracking – Uses MediaPipe to analyze body alignment and gaze direction.
✅ 💬 Speech Sentiment Analysis – Powered by Vosk ASR + HuggingFace Transformers to evaluate positivity and clarity in tone.
✅ 🎨 Beautiful Dynamic UI – Modern Tkinter interface with dark mode, smooth layout, and vivid live feedback colors.

🛠️ Tech Stack
Layer	Technologies Used
Frontend (GUI)	Tkinter, Pillow (PIL), Matplotlib
Speech Processing	Vosk (Offline ASR), SoundDevice
Sentiment Analysis	Transformers (BERT / RoBERTa), Torch
Posture Detection	OpenCV, MediaPipe
Video Handling	MoviePy
Backend Logic	Python 3.12, Threading, JSON
Visualization	Matplotlib (Pie Charts), Tkinter Canvas
Packaging	requirements.txt for reproducible setup
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/nihals007/AI-Interview-Coach.git
cd AI-Interview-Coach1

2️⃣ Create & Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
python app.py

🧩 Folder Structure
AI-Interview-Coach1/
│
├── app.py                      # Main Tkinter Application
├── models/
│   ├── posture_model.py        # Body posture and eye-contact analyzer
│   ├── speech_model.py         # Speech recording & transcription logic
│   └── sentiment_model.py      # Text sentiment analyzer (Transformers)
│
├── requirements.txt            # All dependencies
├── snapshot.jpg                # Auto-generated snapshot (from last test)
├── audio.wav                   # Temporary recorded audio file
└── .gitignore                  # Keeps venv and cache files out of Git

💡 How It Works

Live Mode:

Opens webcam & mic, records video and audio.

Uses Vosk for real-time speech recognition.

Runs live sentiment detection → subtitle colors:
🟢 Positive | ⚪ Neutral | 🔴 Negative

Analyzes facial alignment (eye contact) and posture with MediaPipe.

On stop → generates detailed report with pie chart + transcript.

Recorded Video Mode:

Upload any .mp4 / .avi / .mov file.

Extracts audio, runs transcription + sentiment + posture frame sampling.

Creates a full AI feedback report with realistic scoring.

📊 Example Report
Metric	Score	Description
🧍 Posture	82%	Slight slouch but stable presence
👀 Eye Contact	88%	Mostly maintained eye contact
💬 Speech	79%	Positive and articulate tone
🎯 Overall	83%	Great confidence! Minor posture improvement needed
📸 Screenshots

(Add your screenshots here once you present)

🟢 Live Mode with subtitles

📂 Recorded video upload screen

📊 AI-generated report window

👩‍💻 Contributors

Team Interview Architects

AI Models by Open Source Communities (HuggingFace, Vosk, MediaPipe)

🧰 Future Enhancements

Browser-based version using Flask + React

Emotion recognition via facial analysis

Voice modulation + clarity score

Resume-based question simulation
