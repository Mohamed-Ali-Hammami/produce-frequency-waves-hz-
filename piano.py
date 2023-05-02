import numpy as np
import pyaudio

# Define the notes of a C major scale
C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B = 493.88
C2 = 523.25
"violon G string: 196.00 D string: 293.66 A string: 440.00 E string: 659.26"

# Define the frequencies of the G, D, A, and E strings of a guitar
G_string = 196.00
D_string = 293.66
A_string = 440.00
E_string = 659.26

# Set parameters
duration = 0.5 # Duration of each note in seconds
sampling_freq = 195000 # Sampling frequency in Hz

# Define the amplitudes for each note
note_amp = 1


# Generate the sound
song = np.concatenate((
    note_amp * np.sin(2*np.pi*C*np.arange(0, duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*D*np.arange(duration, 2*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*E*np.arange(2*duration, 3*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*F*np.arange(3*duration, 4*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*G*np.arange(4*duration, 5*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*A*np.arange(5*duration, 6*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*B*np.arange(6*duration, 7*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*C2*np.arange(7*duration, 8*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*G_string*np.arange(0, duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*D_string*np.arange(duration, 2*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*A_string*np.arange(2*duration, 3*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*E_string*np.arange(3*duration, 4*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*E_string*np.arange(4*duration, 5*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*A_string*np.arange(5*duration, 6*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*D_string*np.arange(6*duration, 7*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*G_string*np.arange(7*duration, 8*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*G_string*np.arange(8*duration, 9*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*D_string*np.arange(9*duration, 10*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*A_string*np.arange(10*duration, 11*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*E_string*np.arange(11*duration, 12*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*E_string*np.arange(12*duration, 13*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*A_string*np.arange(13*duration, 14*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*D_string*np.arange(14*duration, 15*duration, 1/sampling_freq)),
    note_amp * np.sin(2*np.pi*G_string*np.arange(15*duration, 16*duration, 1/sampling_freq)),

))

# Normalize the sound
song = song / np.max(np.abs(song))

# Play the sound
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_freq, output=True)
stream.write(song.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()
