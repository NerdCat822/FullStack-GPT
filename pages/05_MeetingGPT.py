import subprocess


def extract_audio_from_video(video_path, audio_path):
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-vn",
        audio_path,
    ]
    subprocess.run(command)


extract_audio_from_video(
    "./files/podcast.mp4",
    "./files/podcast.mp3",
)