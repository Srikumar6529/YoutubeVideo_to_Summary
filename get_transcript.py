# get_transcript.py
import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    text = result['text']
    
    # Chunking (you can improve this)
    max_chunk_length = 1000
    chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    return chunks
