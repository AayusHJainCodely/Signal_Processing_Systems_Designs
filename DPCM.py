import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
# Load grayscale image 
image = cv2.imread(r'C:\Users\satya\Downloads\krishna.png', cv2.IMREAD_GRAYSCALE) 
image = image.astype(np.float32) # Convert to float for processing 
# PCM Encoding 
def pcm_encode(image, bit_depth=8): 
max_val = 2**bit_depth - 1 
quantized = np.round(image * max_val / 255) # Normalize and quantize 
return quantized.astype(np.uint8) 
# PCM Decoding 
def pcm_decode(encoded_image, bit_depth=8): 
max_val = 2**bit_depth - 1 
return (encoded_image * 255 / max_val).astype(np.uint8) 
# DPCM Encoding with Linear Predictor 
def dpcm_encode(image, bit_depth=8): 
predictor = np.zeros_like(image) 
error_signal = np.zeros_like(image) 
for i in range(image.shape[0]): 
for j in range(image.shape[1]): 
predictor[i, j] = image[i, j-1] if j > 0 else image[i, j] # Predict from the left pixel 
error_signal[i, j] = image[i, j] - predictor[i, j] 
# Quantize error signal 
max_val = 2**bit_depth - 1 
quantized_error = np.round((error_signal + 255) * max_val / 510).astype(np.uint8) 
return quantized_error, predictor 
# DPCM Decoding 
def dpcm_decode(quantized_error, predictor, bit_depth=8): 
max_val = 2**bit_depth - 1 
decoded_error = (quantized_error * 510 / max_val) - 255 
decoded_image = predictor + decoded_error 
return np.clip(decoded_image, 0, 255).astype(np.uint8) 
# Compression Ratio Calculation 
def compression_ratio(original_bits, compressed_bits): 
return original_bits / compressed_bits 
# Quantization Error Calculation (Mean Squared Error) 
def quantization_error(original, reconstructed): 
return np.mean((original - reconstructed) ** 2) 
# Bandwidth Efficiency Calculation 
def bandwidth_efficiency(original_bits, compressed_bits): 
return (1 - compressed_bits / original_bits) * 100 # Percentage reduction 
# Bit depth for quantization 
bit_depth = 4 # Example: 4-bit quantization 
# PCM Processing 
pcm_encoded = pcm_encode(image, bit_depth) 
pcm_decoded = pcm_decode(pcm_encoded, bit_depth) 
# DPCM Processing 
dpcm_encoded, predictor = dpcm_encode(image, bit_depth) 
dpcm_decoded = dpcm_decode(dpcm_encoded, predictor, bit_depth) 
# Compute Performance Metrics 
orig_bits = image.size * 8 # Original image stored in 8-bit 
pcm_bits = pcm_encoded.size * bit_depth # PCM compressed size 
dpcm_bits = dpcm_encoded.size * bit_depth # DPCM compressed size 
# Compression ratio 
pcm_cr = compression_ratio(orig_bits, pcm_bits) 
dpcm_cr = compression_ratio(orig_bits, dpcm_bits) 
# Quantization error (MSE) 
pcm_qe = quantization_error(image, pcm_decoded) 
dpcm_qe = quantization_error(image, dpcm_decoded) 
 
  
Compression Ratio - PCM: 2.00, DPCM: 2.00 
Quantization Error - PCM: 10569.26, DPCM: 244.61 
Bandwidth Efficiency - PCM: 50.00%, DPCM: 50.00% 
 
# Bandwidth efficiency 
pcm_bw_eff = bandwidth_efficiency(orig_bits, pcm_bits) 
dpcm_bw_eff = bandwidth_efficiency(orig_bits, dpcm_bits) 
 
# Display Results 
plt.figure(figsize=(12, 6)) 
 
plt.subplot(1, 3, 1) 
plt.imshow(image, cmap='gray') 
plt.title("Original Image") 
 
plt.subplot(1, 3, 2) 
plt.imshow(pcm_decoded, cmap='gray') 
plt.title("PCM Reconstructed") 
 
plt.subplot(1, 3, 3) 
plt.imshow(dpcm_decoded, cmap='gray') 
plt.title("DPCM Reconstructed") 
 
plt.show() 
 
# Print Metrics 
print(f"Compression Ratio - PCM: {pcm_cr:.2f}, DPCM: {dpcm_cr:.2f}") 
print(f"Quantization Error - PCM: {pcm_qe:.2f}, DPCM: {dpcm_qe:.2f}") 
print(f"Bandwidth Efficiency - PCM: {pcm_bw_eff:.2f}%, DPCM: {dpcm_bw_eff:.2f}%
