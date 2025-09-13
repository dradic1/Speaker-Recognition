import sounddevice as sd
from scipy.io.wavfile import write
import predict as pd
import os
import datetime
from soundcut import SoundCut

fs = 44100  # Sample rate
seconds = 10  # Duration of recording

i = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
path = os.path.join("./dataset/predict")
os.makedirs(path, exist_ok=True)
print("Speak")
sd.wait()  # Wait until recording is finished
audio_filename = f"{i}.wav"
audio_path = os.path.join(path, audio_filename)
write(audio_path, fs, myrecording)  # Save as WAV file
print("Recorded")

# Process the recorded audio file with SoundCut
SoundCut(audio_path)

# Predict using the processed audio
predict_dir_path = './dataset/predict/'
dir_list = os.listdir(predict_dir_path)
length = len(dir_list)
for i in range (length):
    predicted = pd.predict(predict_dir_path+dir_list[i])
    print(f'{i+1}. {predicted}')

