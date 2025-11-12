import numpy as np
import librosa
from pydub import AudioSegment

pcm_file = 'pcm_music.pcm'
mp3_file = 'test_music.mp3'
pcm_data = np.fromfile(pcm_file, dtype=np.int16)

audio = AudioSegment(
    data=pcm_data.tobytes(),
    sample_width=2,      # 2 байта = 16 бит
    frame_rate=44100,    # частота дискретизации
    channels=1           # моно
)

audio.export(mp3_file, format="mp3", bitrate="192k")