import numpy as np
import librosa
from pydub import AudioSegment


My_File = 'my_music.mp3'
pcm_file = 'pcm_music.pcm'
y, sr = librosa.load(My_File, sr=44100, mono=True)

pcm_data = (y * 32767).astype(np.int16)

pcm_data.tofile(pcm_file)
