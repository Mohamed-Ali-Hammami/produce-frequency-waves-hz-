import pyaudio
import numpy as np

# Parameters
frequency1 = 432 # Hz


duration = 30 # seconds



# Generate time array
time = np.arange(int(duration * 44100)) / 44100

# Generate sine wave
signal1 = np.sin(2 * np.pi * frequency1 * time)



# Create composite signal
composite_signal = signal1

# Multiply frequency signals by instrument sounds
signal1_with_piano = signal1


# Create audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)

# Play audio
stream.write(composite_signal.astype(np.float32).tobytes())

# Stop audio stream
stream.stop_stream()
stream.close()
p.terminate()