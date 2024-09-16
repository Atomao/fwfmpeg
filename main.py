

from faster_whisper import WhisperModel
import os
from pathlib import Path
from omegaconf import OmegaConf
import sys
# from rich import print
from pprint import pprint as print
from tqdm import tqdm


class Video2Text:
    @staticmethod
    def extract_audio(video_path, audio_path):
        os.system(f"ffmpeg -i {video_path} -vn -acodec libmp3lame -q:a 2 {audio_path}")


    @staticmethod
    def transcribe_audio(audio_path, text_path, model_config):
        model = WhisperModel(model_config["model_size"], download_root=model_config['download_root'])
        segments, info = model.transcribe(audio_path,
                                          beam_size = model_config["beam_size"],
                                          language = model_config["language"],
                                          condition_on_previous_text = model_config["condition_on_previous_text"])

        with open(text_path, "w") as file:
            for segment in tqdm(segments):
                segment_info = "%im  %s\n" % (segment.start // 60, segment.text)
                file.write(segment_info)
        
    @staticmethod   
    def run(config):
        model_config, video_path, audio_path, text_path = Video2Text.prepare(config)

        Video2Text.extract_audio(video_path,  audio_path)
        Video2Text.transcribe_audio(audio_path, text_path, model_config=model_config)
        print("Finished")

    
    @staticmethod   
    def prepare(config):
        print("-------------------------------------------")
        print(config)
        print("-------------------------------------------")
        model_config = config['model_config']

        video_path   = Path(config['video_path'])
        text_path    = Path(config['text_path'])


        if text_path.is_dir():
            text_path = text_path / video_path.with_suffix(".txt").name
            counter = 0
            while text_path.exists():
                text_path =  text_path.parent / (f"{counter}_" + video_path.with_suffix(".txt").name)
                counter += 1
            
        audio_path = Path("/tmp") / video_path.with_suffix(".mp3").name

        return model_config, video_path, audio_path, text_path

if __name__ == "__main__":
    print(sys.argv[1])
    config = OmegaConf.load(sys.argv[1])
    Video2Text.run(OmegaConf.to_object(config))