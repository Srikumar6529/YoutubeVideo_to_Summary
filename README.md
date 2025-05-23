🎙️ YouTube Video Summarizer
This project extracts audio from a YouTube video, transcribes the speech using OpenAI's Whisper model, and then summarizes the transcription using a Transformer model. It’s designed to help you quickly understand the key points from long videos, especially meetings, lectures, or podcasts.

✅ Features
Download audio from YouTube using yt-dlp

Transcribe with openai-whisper

Summarize using Hugging Face Transformers (e.g., BART, T5)

Clean CLI-based modular structure
▶️ Usage
Simply run the main.py script and paste the YouTube video link when prompted:

The script will:

Download the audio

Transcribe it

Summarize the transcription

Print the summary

🧠 Models Used
Transcription: Whisper

Summarization: HuggingFace Transformers

💡 Notes
Some YouTube videos may block downloads or require a login (e.g., YouTube Shorts or age-restricted videos).

Audio is saved as audio.mp3.

Works best with English speech; accuracy depends on audio quality and speaker clarity.

🧑‍💻 Author
Built with ❤️ by Sri Kumar Sanka. This is part of my 50 AI project challenge to master tools before diving into deep research.
