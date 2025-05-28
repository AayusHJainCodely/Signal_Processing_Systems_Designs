import numpy as np 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wav 
# Small epsilon to avoid log(0) errors 
EPSILON = 1e-12 
# Mu-law companding 
def mu_law_companding(signal, mu=255): 
abs_signal = np.abs(signal) 
abs_signal = np.where(abs_signal == 0, EPSILON, abs_signal) # Avoid log(0) 
compressed = np.sign(signal) * np.log1p(mu * abs_signal) / np.log1p(mu) 
return compressed 
def mu_law_expanding(compressed, mu=255): 
expanded = np.sign(compressed) * (np.expm1(np.abs(compressed) * np.log1p(mu)) / mu) 
return expanded 
# A-law companding 
def a_law_companding(signal, A=87.6): 
abs_signal = np.abs(signal) 
abs_signal = np.where(abs_signal == 0, EPSILON, abs_signal) # Avoid log(0) 
compressed = np.where(abs_signal < 1 / A, 
(A * abs_signal) / (1 + np.log(A)), 
np.sign(signal) * (1 + np.log(A * abs_signal)) / (1 + np.log(A))) 
return compressed 
def a_law_expanding(compressed, A=87.6): 
abs_compressed = np.abs(compressed) 
expanded = np.where(abs_compressed < 1 / (1 + np.log(A)), 
(abs_compressed * (1 + np.log(A))) / A, 
np.sign(compressed) * (np.exp(abs_compressed * (1 + np.log(A))) - 1) / A) 
return expanded 
# SNR Calculation 
def calculate_snr(original, quantized): 
noise = original - quantized 
signal_power = np.mean(original ** 2) 
noise_power = np.mean(noise ** 2) 
return 10 * np.log10(signal_power / noise_power) 
# Read and normalize speech signal 
fs, speech_signal = wav.read('Sample-1.wav') 
speech_signal = speech_signal[:fs] # Take 1 second of speech 
speech_signal = speech_signal.astype(np.float32) # Ensure float type for normalization 
speech_signal = speech_signal / np.max(np.abs(speech_signal)) # Normalize to [-1,1] 
# Apply companding 
mu_compressed = mu_law_companding(speech_signal) 
mu_expanded = mu_law_expanding(mu_compressed) 
a_compressed = a_law_companding(speech_signal) 
a_expanded = a_law_expanding(a_compressed) 
# Compute SNR 
snr_uniform = calculate_snr(speech_signal, np.round(speech_signal * 127) / 127) 
snr_mu = calculate_snr(speech_signal, mu_expanded) 
snr_a = calculate_snr(speech_signal, a_expanded) 
# Plot original vs. companded 
plt.figure(figsize=(12, 6)) 
plt.subplot(2, 1, 1) 
plt.plot(speech_signal, label='Original Signal') 
plt.plot(mu_compressed, label='Mu-law Compressed', linestyle='dashed') 
plt.plot(a_compressed, label='A-law Compressed', linestyle='dotted') 
plt.legend() 
plt.title("Original vs. Companded Signal") 
plt.subplot(2, 1, 2) 
plt.plot(speech_signal, label='Original Signal') 
plt.plot(mu_expanded, label='Mu-law Expanded', linestyle='dashed') 
plt.plot(a_expanded, label='A-law Expanded', linestyle='dotted') 
plt.legend() 
plt.title("Original vs. Expanded Signal") 
plt.show() 
 
 
 
SNR (Uniform Quantization): 43.44 dB 
SNR (Mu-law Companding): 136.93 dB 
SNR (A-law Companding): -4.58 dB 
 
# Print SNR values 
print(f"SNR (Uniform Quantization): {snr_uniform:.2f} dB") 
print(f"SNR (Mu-law Companding): {snr_mu:.2f} dB") 
print(f"SNR (A-law Companding): {snr_a:.2f} dB")
