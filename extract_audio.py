from moviepy.editor import VideoFileClip
from gtts import gTTS
import os

def generate_speech(text, output_path, lang="en"):
    """
    Generate speech audio from text and save it as an mp3 file.
    
    :param text: str, the text to be converted into speech.
    :param output_path: str, the path to save the generated audio file.
    :param lang: str, the language of the speech (default is English).
    """
    tts = gTTS(text=text, lang=lang, slow=False)
    
    tts.save(output_path)
    print(f"Audio saved at {output_path}")

def extract_audio(video_path, audio_path) -> None:
    """
    Extract audio from video and save it as a .wav file.
    
    :param `video_path`: str, path to the input video file
    :param `audio_path`: str, path to save the output audio file.
    
    :return: None
    """
    # try catch to check if the video file exists
    try:
        with open(video_path) as f:
            pass
    except FileNotFoundError:
        print(f"Video file not found at {video_path}")
        return

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    file_name = video_path.split("/")[-1].split(".")[0]
    audio_path = f"{audio_path}/{file_name}.wav"
    
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    audio.close()
    video.close()
    print(f"Audio saved at {audio_path}")