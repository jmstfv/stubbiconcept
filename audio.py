
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# TODO(developer): Update and un-comment below lines
vertexai.init(project="stubbi", location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

prompt = """You're a world-class translator for the United Nations. Your assignment is to translate between languages seamlessly and precisely, helping important people communicate in their native language. Translate flawlessly, and think step-by-step. Detect the language and translate it to English."""

audio_file_uri = "gs://vertexsampledata/rumu.mp3"
audio_file = Part.from_uri(audio_file_uri, mime_type="audio/mpeg")

contents = [audio_file, prompt]

response = model.generate_content(contents)

print(response.text)
