# get_audio.py
from yt_dlp import YoutubeDL

def download_audio(url, output_path="audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_path
