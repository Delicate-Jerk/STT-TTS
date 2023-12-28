from openai import OpenAI
client = OpenAI(api_key="")

audio_file = open("output.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
  )

print(transcript)