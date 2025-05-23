# main.py
from get_audio import download_audio
from get_transcript import transcribe_audio
from get_summary import summarize_chunks

def normalize_url(url):
    if "youtube.com/shorts/" in url:
        video_id = url.split("/")[-1]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

def main():
    url = input("Enter YouTube video URL: ").strip()
    url = normalize_url(url)

    print("Downloading audio...")
    audio_path = download_audio(url)

    print("Transcribing audio...")
    chunks = transcribe_audio(audio_path)

    print("Generating summary...")
    summaries = summarize_chunks(chunks)

    print("\n=== Summary ===")
    for i, s in enumerate(summaries, 1):
        print(f"\nChunk {i}:")
        print(s)

if __name__ == "__main__":
    main()
