import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
modulant_file = "/Users/thibaultvanni/Documents/UCL/LELEC1360 - Télécommunications/Labo 1/modulant time with default value.csv"
modulated_file = "/Users/thibaultvanni/Documents/UCL/LELEC1360 - Télécommunications/Labo 1/modulated time with default value.csv"

# Read CSV files (skip metadata rows)
modulant_df = pd.read_csv(modulant_file, skiprows=4, names=["Time", "Modulant"])
modulated_df = pd.read_csv(modulated_file, skiprows=4, names=["Time", "Modulated"])

# Extract time and signal values
time = modulant_df["Time"].values
signal = modulant_df["Modulant"].values
# Compute time step (assuming uniform sampling)
dt = np.mean(np.diff(time))  # Sampling interval
fs = 1 / dt  # Sampling frequency

# Compute FFT
n = len(signal)  # Number of samples
frequencies = np.fft.fftfreq(n, d=dt)  # Frequency axis
fft_values = np.fft.fft(signal)  # FFT computation


# Find zero crossings
zero_crossings = np.where(np.diff(np.sign(signal)))[0]

# Get first and last zero crossing indices
first_zero_idx = zero_crossings[0]
last_zero_idx = zero_crossings[-1]

# Plot FFT result
plt.figure(figsize=(10, 5))
plt.plot(frequencies, fft_values, color="b")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT of the Modulant Signal")
plt.grid()
plt.show()


# Get the magnitude of the FFT (absolute value of the complex numbers)
fft_magnitude = np.abs(fft_values)

# Find local maxima in the magnitude of the FFT
peaks = []
for i in range(1, len(fft_magnitude) - 1):
    # Check if current value is a peak and at least 1000 greater than its neighbors
    if fft_magnitude[i - 1] < fft_magnitude[i] > fft_magnitude[i + 1] and \
       fft_magnitude[i] > 1000:  # Add the threshold condition here
        peaks.append(i)
print(peaks)

# Find the frequencies and magnitudes of the peaks
peak_frequencies = frequencies[peaks]
print(peak_frequencies)
peak_magnitudes = fft_magnitude[peaks]
print(peak_magnitudes)

# Sort peaks by frequency (ascending) to ensure we find the first and last peak
sorted_peaks = sorted(zip(peak_magnitudes, peak_frequencies), key=lambda x: x[1])
print(sorted_peaks)
# Select the portion of the FFT data between the first and last peaks
first_peak_idx = sorted_peaks[0][1]  # Index of the first peak
last_peak_idx = sorted_peaks[-1][1]  # Index of the last peak

end_index = np.where(frequencies== first_peak_idx)[0][0]
print("========", end_index)
start_index = np.where(frequencies== last_peak_idx)[0][0]

# Extract the frequencies and magnitudes for the zoomed-in range
zoomed_frequencies = frequencies[start_index:end_index+1]
zoomed_fft_magnitude = fft_magnitude[start_index:end_index+1]

# Plot the zoomed-in FFT between the first and last peaks
plt.figure(figsize=(10, 5))
plt.plot(zoomed_frequencies, zoomed_fft_magnitude, color="b", label="FFT Magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title(f"Zoomed-in FFT from {frequencies[peaks[0]]:.2f} Hz to {frequencies[peaks[-1]]:.2f} Hz")
plt.grid(True)
plt.legend()
plt.show()