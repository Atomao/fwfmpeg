FROM python:3.12

RUN apt update && apt install ffmpeg -y
RUN apt install libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libavfilter-dev libswscale-dev libswresample-dev -y

WORKDIR /src

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt 

COPY ./main.py ./main.py

ENTRYPOINT [ "python", "main.py", "config.yaml"]


