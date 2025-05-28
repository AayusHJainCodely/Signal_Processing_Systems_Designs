import numpy as np 
import scipy.signal as signal 
import scipy.interpolate as interpolate 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
# Function for uniform quantization 
def uniform_quantize(signal, num_levels): 
max_val = np.max(np.abs(signal)) 
step_size = 2 * max_val / num_levels 
quantized = np.round((signal + max_val) / step_size) * step_size - max_val 
return quantized 
# Function for non-uniform quantization (companding using μ-law) 
def non_uniform_quantize(signal, num_levels, mu=255): 
signal_norm = signal / np.max(np.abs(signal)) 
compressed = np.sign(signal_norm) * np.log1p(mu * np.abs(signal_norm)) / np.log1p(mu) 
quantized = uniform_quantize(compressed, num_levels) 
expanded = np.sign(quantized) * (np.expm1(np.abs(quantized) * np.log1p(mu)) / mu) 
return expanded * np.max(np.abs(signal)) 
# Function to add AWGN noise 
def add_awgn(signal, snr_db): 
power_signal = np.mean(signal**2) 
power_noise = power_signal / (10**(snr_db / 10)) 
noise = np.sqrt(power_noise) * np.random.normal(0, 1, signal.shape) 
return signal + noise 
# Read an audio signal 
fs, audio = wavfile.read("Sample-4.wav") # Replace with your audio file 
audio = audio.astype(np.float32) 
audio /= np.max(np.abs(audio)) # Normalize between -1 and 1 
# Define quantization levels and SNR values 
quant_levels = [4, 8, 16, 32] # Different quantization levels 
snr_values = [10, 20, 30] # Different SNR values 
# Loop through different quantization levels and plot results 
for ql in quant_levels: 
plt.figure(figsize=(12, 8)) 
# Apply Uniform and Non-Uniform Quantization 
uniform_pcm = uniform_quantize(audio, ql) 
non_uniform_pcm = non_uniform_quantize(audio, ql) 
for snr in snr_values: 
# Add Noise 
noisy_uniform = add_awgn(uniform_pcm, snr) 
# Compute SNR 
computed_snr = 10 * np.log10(np.mean(audio**2) / np.mean((audio - noisy_uniform) ** 2)) 
print(f"Quantization Level: {ql}, SNR: {snr} dB → Computed SNR: {computed_snr:.2f} dB") 
# Plot results 
plt.subplot(3, 1, 1) 
plt.plot(audio[:300], label="Original Signal", linestyle='dashed', color='green', linewidth=1.5) 
plt.title(f"Original Signal (Quantization Level: {ql})") 
plt.xlabel("Sample Index") 
plt.ylabel("Amplitude") 
plt.legend() 
plt.grid(True) 
plt.subplot(3, 1, 2) 
plt.plot(uniform_pcm[:300], label="Quantized Signal", color='red', linewidth=1.2) 
plt.title(f"Uniform Quantized Signal (Levels: {ql})") 
plt.xlabel("Sample Index") 
plt.ylabel("Amplitude") 
plt.legend() 
plt.grid(True) 
