FROM python

RUN apt update && apt install ffmpeg -y
RUN pip install faster_whisper omegaconf rich tqdm

WORKDIR /src
COPY ./main.py ./main.py

ENTRYPOINT [ "python", "main.py", "config.yaml"]


