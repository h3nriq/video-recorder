# Video Recorder
Recording Video with Python

## Video-Only Recorder
### Libraries:
- opencv
- keyboard
- pyautogui
- numpy
- os

### To Start Recording:
Run the recorder file.

### To Stop Recording:
Press the "esc" key.

### Output File:
- video.avi

## Video Recorder with Microphone
### Libraries:
- opencv
- numpy
- pyautogui
- pyaudio
- wave
- threading
- os
### To Start Recording:
Run the recorder_with_microphone file.

### To Stop Recording:
Press the "q" key and then hit Enter.

### Output Files:
- video.avi
- audio.wav

### Tip:
You can use FFmpeg to merge video and audio.
``` ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4 ```
