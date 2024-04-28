from transformers import pipeline, AutoTokenizer
import json


summarizer = pipeline(task='summarization', model="facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

transcript_file = './captions/transcript_2022-04-21T14:22:39-07:00_HaUzUwNBFcc.txt'

with open(transcript_file, 'r') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit()

text = ""
for event in data['events']:
    if 'segs' in event:
        for seg in event['segs']:
            if 'utf8' in seg:
                text += seg['utf8']


if text.strip():
    max_input_length = 512
    truncated_text = text[:max_input_length]
    max_length = min(len(tokenizer(truncated_text)['input_ids']) + 50, 132)  

    summary = summarizer(truncated_text, max_length=max_length)
    summary_text = summary[0]['summary_text']
    summary_text = summary_text.replace('\xa0', ' ')
    with open("summary.txt", 'w') as output:
        output.write(summary_text)
else:
    print("No text found for summarization.")
