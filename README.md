# fwfmpeg

## How to run
1. Clone and build
```
git clone https://github.com/Atomao/fwfmpeg.git
cd fwfmpeg

docker build -t fwfmpeg .
```
2. You need to create `data/input` and `data/output` folders (everything else will be created automatically).
3. Then place your video of interest into `data/input` folder.
4. Then configure `video_path` in `config.yaml`.
5. Run 
```
docker run  -v $(pwd)/data:/src/data -v $(pwd)/config.yaml:/src/config.yaml fwfmpeg
```

**Note:** that `docker run` command use volume folder data. Detailed folder structure described below
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
