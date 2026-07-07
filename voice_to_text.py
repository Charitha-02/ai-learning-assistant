import whisper
import tempfile
from pydub import AudioSegment

model = whisper.load_model("medium")

def speech_to_text(audio_bytes):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".webm"
    ) as temp_webm:

        temp_webm.write(audio_bytes)

        webm_path = temp_webm.name

    wav_path = webm_path.replace(
        ".webm",
        ".wav"
    )
    print("Step 1")

    audio = AudioSegment.from_file(webm_path)
    print("Step 2")

    audio.export(
    wav_path,
    format="wav"
)

    print("Transcribing audio...")
    print("Step 3")
    result = model.transcribe(
    wav_path,
    language="en"
)

    print("WHISPER RESULT:")
    print(result)

    return result["text"]