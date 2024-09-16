FROM python

RUN apt update && apt install ffmpeg -y

WORKDIR /src

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY ./main.py ./main.py

ENTRYPOINT [ "python", "main.py", "config.yaml"]


