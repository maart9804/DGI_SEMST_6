import matplotlib.pyplot as plt
import numpy as np

fileobj= open("1kHz_44100Hz_16bit_05sec.wav", mode='rb')
data = fileobj.read()

file_size_inbytes = data[4:8]
file_size = int.from_bytes(file_size_inbytes, byteorder = "little")
print(file_size)

num_of_channels_in_byte = data[22:24]
num_of_channels = int.from_bytes(num_of_channels_in_byte, byteorder = "little")

audio_data_size_inbytes = data[40:44]
audio_data_size = int.from_bytes(audio_data_size_inbytes, byteorder = "little")

sample_rate_in_bytes = data[24:28]
sample_rate = int.from_bytes(sample_rate_in_bytes, byteorder = "little")


music_amps = []
audio_data_in_byte = data[44:]
for i in range(44,audio_data_size,2):
    amp_in_byte = data[44+i:44+i+2]
    amp = int.from_bytes(amp_in_byte, byteorder = "little", signed = True)
    music_amps.append(amp)

xdata_time = np.linspace(0, len(music_amps)/sample_rate, len(music_amps))
xdata_freqs = 1/xdata_time
spectr = np.fft.fft(music_amps)
abs_specrte = abs(spectr)
plt.plot(xdata_freqs, abs_specrte)
plt.show()
print(music_amps)
