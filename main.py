import sounddevice as sd

duration = 10
sample_rate = 44100

print("recording has started...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate = sample_rate,
    channels= 1

)

sd.wait()
print("Recording has finished.")
