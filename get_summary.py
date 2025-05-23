# get_summary.py
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_chunks(chunks):
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return summaries
