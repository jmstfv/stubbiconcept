
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# TODO(developer): Update and un-comment below lines
vertexai.init(project="stubbi", location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

prompt = """You're a world-class translator for the United Nations. Your assignment is to translate between languages seamlessly and precisely, helping important people communicate in their native language. Translate flawlessly, and think step-by-step. Speed is important, so translate it sentence by sentence and return the output. Detect the language and translate it to English."""


import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 4
filename = "output2.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()


with open("output2.wav", "rb") as f:
  bytes_audio = f.read()

audio_file = Part.from_data(bytes_audio, mime_type="audio/mpeg")

contents = [audio_file, prompt]

response = model.generate_content(contents, stream=True)

for chunk in response:
  print(chunk.text)
