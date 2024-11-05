# 1. convert text to audio using gTTS
# 2. use dummy video and the new audio as input for Wav2Lip
# 3. save the output video

# import argparse
from pydub import AudioSegment
from extract_audio import generate_speech
import subprocess


def narrative_to_video(video_output_path): #, text):
    # read from txt file for now
    with open("./analysis_from_llm/analysis.txt", "r") as file:
        text = file.read()

    # generate speech from text
    audio_output_path = "./audio_output/weather_details.mp3"
    generate_speech(text, audio_output_path)

    # speed up the audio speech
    audio = AudioSegment.from_file(audio_output_path)
    audio.speedup(playback_speed=1.2).export(audio_output_path, format="mp3")

    # run inference.py to generate video
    subprocess.run([
        "python", "./inference.py", 
        "--checkpoint_path", 
        "./checkpoints/wav2lip.pth", 
        "--face",
        "../test/AI head.mp4", 
        "--audio", 
        audio_output_path, 
        "--outfile",
        video_output_path,
        "--resize_factor", "1"])

if __name__ == "__main__":
    narrative_to_video()


