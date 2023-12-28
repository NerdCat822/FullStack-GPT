import subprocess
from pydub import AudioSegment
import math
import openai
import glob


def extract_audio_from_video(video_path, audio_path):
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-vn",
        audio_path,
    ]
    subprocess.run(command)


def cut_audio_in_chunks(audio_path, chunk_size, chunks_folder):
    track = AudioSegment.from_mp3(audio_path)
    chunk_len = chunk_size * 60 * 1000
    chunks = math.ceil(len(track) / chunk_len)
    for i in range(chunks):
        start_time = i * chunk_len
        end_time = (i + 1) * chunk_len
        chunk = track[start_time:end_time]
        chunk.export(
            f"./{chunks_folder}/chunk_{i}.mp3",
            format="mp3",
        )


def transcribe_chunks(chunk_folder, destination):
    files = glob.glob(f"{chunk_folder}/*.mp3")
    for file in files:
        with open(file, "rb") as audio_file, open(destination, "a") as text_file:
            transcript = openai.Audio.transcribe(
                "whisper-1",
                audio_file,
            )
            text_file.write(transcript["text"])