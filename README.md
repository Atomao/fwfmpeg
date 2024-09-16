# fwfmpeg

## How to run
```
git clone https://github.com/Atomao/fwfmpeg.git
cd fwfmpeg

docker build -t fwfmpeg .
docker run  -v $(pwd)/data:/src/data -v $(pwd)/config.yaml:/src/config.yaml fwfmpeg
```
## Data folder structure
```
├── data
│   ├── input                                                      #input folder contains videos to transcribe
│   │   └── video.mp4
│   ├── models                                                     #models folder contains weights for models(will be automatically created and filled with model on your first run)
│   │   ├── models--Systran--faster-distil-whisper-large-v3        #will be automatically saved here if you specify model in config.yaml (distil-large-v3)
│   │   └── models--Systran--faster-distil-whisper-small.en        #(distil-small.en)
│   └── output                                                     #output folder where to save txt transcriptions
│       └── video.txt
```
## Parameters
For parameters go to `config.yaml` file
