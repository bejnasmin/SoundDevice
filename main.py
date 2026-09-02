import sounddevice as sd
from scipy.io.wavfile import write

duration = 10
sample_rate = 44100

print("recording has started...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate = sample_rate,
    channels= 1

)

sd.wait()
write("recording.wav", sample_rate, recording)

print("Recording has finished.")
