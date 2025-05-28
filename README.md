![image](https://github.com/user-attachments/assets/78a0bbec-734e-4871-9d7e-c9821da1982c)
This repository contains Python implementations of various digital signal processing tasks including PCM, delta modulation, companding, DPCM for images, and a speech-to-text system using MFCC and SVM.

## 📌 Contents

### ✅ Q1: PCM Simulation with Quantization and Interpolation

- **Objective:** Simulate Pulse Code Modulation (PCM) using different quantization levels and analyze the impact of Additive White Gaussian Noise (AWGN) on SNR.
- **Signal Processing Techniques:**
  - Uniform and Non-Uniform Quantization (μ-law)
  - AWGN modeling
  - SNR computation
  - Interpolation: linear, spline, cubic
- **Plots:**
  - Original vs. Quantized vs. Noisy signals
  - Quantization error visualization
  - SNR trends with varying quantization levels

> **Key Insight:** SNR improves with higher quantization levels. Noise effects are more prominent at lower levels. μ-law companding helps preserve low-amplitude signals better.
![image](https://github.com/user-attachments/assets/2eb36507-3a3f-4d26-85a9-5f289e538d4e)

---

### ✅ Q2: Delta Modulation vs. Adaptive Delta Modulation

- **Objective:** Compare standard DM and ADM using sinusoidal and speech signals.
- **Signal Processing Techniques:**
  - Bit-wise encoding
  - Adaptive step size control based on signal derivative
  - BER and MSE calculations
- **Plots:**
  - Original signal vs. DM and ADM reconstructions
  - Step-size variation in ADM
- **Results:**
  - ADM shows better reconstruction for speech signals.
  - BER and MSE comparisons highlight ADM’s adaptability.

> **Key Insight:** Adaptive modulation improves tracking performance on signals with varying slopes, especially speech.
![image](https://github.com/user-attachments/assets/748bdadf-da9b-43d5-8d32-23293bb729ce)

---

### ✅ Q3: μ-law and A-law Companding

- **Objective:** Implement and compare μ-law and A-law companding against uniform quantization.
- **Signal Processing Techniques:**
  - Logarithmic companding (encoding/decoding)
  - SNR comparison
- **Plots:**
  - Original vs. Compressed and Expanded signal
- **Results:**
  - **μ-law SNR:** 136.93 dB (best)
  - **A-law SNR:** -4.58 dB (poor implementation noted)
  - **Uniform SNR:** 43.44 dB

> **Key Insight:** μ-law greatly improves SNR by compressing dynamic range before quantization. A-law requires review for correctness.
> ![image](https://github.com/user-attachments/assets/d866753e-12dc-4952-a6a1-4f90bd9451e7)


---

### ✅ Q4: Differential PCM (DPCM) for Image Compression

- **Objective:** Compare DPCM and standard PCM in image compression.
- **Signal Processing Techniques:**
  - Linear prediction
  - Differential quantization
  - MSE and bandwidth efficiency computation
- **Plots:**
  - Original vs. PCM-decoded vs. DPCM-decoded image
- **Results:**
  - DPCM has significantly lower quantization error.
  - Compression ratios are identical (bit-depth controlled).
  - DPCM offers better visual quality with the same bit-rate.

> **Key Insight:** DPCM leverages signal redundancy, offering better performance at fixed bit depth compared to PCM.
![image](https://github.com/user-attachments/assets/1840083f-9ed6-4024-bdc6-3a4bbb60cf49)

---

### ✅ Q5: Speech-to-Text using DM and MFCC + SVM

- **Objective:** Recognize spoken digits using a machine learning model trained on MFCC features from DM-encoded audio.
- **Signal Processing Techniques:**
  - Delta modulation preprocessing
  - MFCC feature extraction
  - SVM classification
- **Results:**
  - **Dataset:** Free Spoken Digit Dataset (~3,000 files)
  - **Classifier Accuracy:** 96.00%
  - **Confusion Matrix:** High accuracy across all digits

> **Key Insight:** Even with low-bitrate encoding like delta modulation, robust classification is possible with MFCC + SVM.
![image](https://github.com/user-attachments/assets/ec238544-66de-4621-8e81-34f28068e8f3)

---

## 📊 Summary of Results

| Task                  | Metric          | PCM    | DPCM   | DM     | ADM    | μ-law | A-law | SVM Classifier |
|-----------------------|------------------|--------|--------|--------|--------|--------|--------|----------------|
| Audio SNR             | —                | ~43 dB | —      | —      | —      | 136.9  | -4.6   | —              |
| Image MSE             | Mean Sq. Error   | 10569  | 244    | —      | —      | —      | —      | —              |
| BER (Speech)          | Bit Error Rate   | —      | —      | 0.483  | 0.395  | —      | —      | —              |
| Speech Recognition    | Accuracy         | —      | —      | —      | —      | —      | —      | 96.00%         |

---


