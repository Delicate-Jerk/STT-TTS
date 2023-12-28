#using openai for Text to speech

from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = ""

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="tata ke product kaise khareed sakte hai ?",
)

response.stream_to_file("test-audio.mp3")

# हेलो वर्ल्ड आप कैसे हैं?