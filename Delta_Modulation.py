import numpy as np 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wav 
` 
# Delta Modulation Encoder 
def delta_modulation(signal, step_size): 
dm_signal = np.zeros(len(signal)) 
quantized = np.zeros(len(signal)) 
previous = 0 
for i in range(len(signal)): 
if signal[i] >= previous: 
dm_signal[i] = 1 
previous += step_size 
else: 
dm_signal[i] = 0 
previous -= step_size 
quantized[i] = previous 
return dm_signal, quantized 
# Adaptive Delta Modulation Encoder 
def adaptive_delta_modulation(signal, initial_step, alpha=1.5): 
adm_signal = np.zeros(len(signal)) 
quantized = np.zeros(len(signal)) 
previous = 0 
step_size = initial_step 
for i in range(len(signal)): 
if signal[i] >= previous: 
adm_signal[i] = 1 
previous += step_size 
else: 
adm_signal[i] = 0 
previous -= step_size 
quantized[i] = previous 
# Adaptive step size adjustment 
if i > 0 and adm_signal[i] == adm_signal[i-1]: 
step_size *= alpha # Increase step size if same direction 
else: 
step_size /= alpha # Decrease step size if direction changes 
return adm_signal, quantized 
# Signal Reconstruction 
def reconstruct_signal(dm_signal, step_size): 
reconstructed = np.zeros(len(dm_signal)) 
previous = 0 
for i in range(len(dm_signal)): 
if dm_signal[i] == 1: 
previous += step_size 
else: 
previous -= step_size 
reconstructed[i] = previous 
return reconstructed 
# Performance Metrics 
def mean_square_error(original, reconstructed): 
return np.mean((original - reconstructed) ** 2) 
def bit_error_rate(original, reconstructed): 
return np.sum(original != reconstructed) / len(original) 
# Generate Sinusoidal Signal 
fs = 8000 # Sampling frequency 
T = 1 
# Duration in seconds 
t = np.linspace(0, T, fs) 
freq = 5 # Frequency of sinusoid 
sin_wave = np.sin(2 * np.pi * freq * t) 
