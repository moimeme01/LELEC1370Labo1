import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
#Here is the windows version

directory = "C:\\Users\\thibault\\Documents\\LabVIEW Projects\\Labo1_2025\\Documentation"

print(os.listdir(directory))

for filename in os.listdir(directory):

    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename), encoding='utf-8', skiprows=3)

        if "X-Y" in filename:
            print("X-Y File is " + filename)

            xy_files = filename.split(".csv")[0].split(" ")
            x_filename = xy_files[0] + ".csv"
            x_file = pd.read_csv(os.path.join(directory, x_filename), skiprows=4, names=["Time", x_filename], encoding='utf-8')
            y_filename = xy_files[1] + ".csv"
            y_file = pd.read_csv(os.path.join(directory, y_filename), encoding='utf-8', skiprows=4, names=["Time", y_filename])

            plt.plot(x_file[x_filename], y_file[y_filename], color="g", alpha=0.7)
            plt.title(f"Plot for {filename}")
            plt.xlabel(x_filename)
            plt.ylabel(y_filename)
            plt.tight_layout()  # Make sure the layout isn't clipped
            name = " ".join([xy_files[0], xy_files[1]]) + ".pdf"
            plt.savefig(os.path.join(directory, name), format="pdf")
            plt.show()

        elif "FFT" in filename:
            pass
        else:
            print("Other filename are: ", filename)
            pass
            #file.columns = ['X', 'Y']

            # Plotting
            #plt.plot(file['X'], file['Y'])
            #plt.title(f"Plot for {filename}")
            #plt.xlabel("X")
            #plt.ylabel("Y")
            #plt.tight_layout()  # Make sure the layout isn't clipped
            #plt.show()

"""

#"""
#Here is the MACos version

directory = "/Users/thibaultvanni/Documents/UCL/LELEC1360 - Télécommunications/Labo 1"

print(os.listdir(directory))

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename), encoding='utf-8', skiprows=3)

        if "X-Y" in filename:
            print("X-Y File is " + filename)

            xy_files = filename.split(".csv")[0].split(" ")
            x_filename = xy_files[0] + ".csv"
            x_file = pd.read_csv(os.path.join(directory, x_filename), skiprows=4, names=["Time", x_filename],
                                 encoding='utf-8')
            y_filename = xy_files[1] + ".csv"
            y_file = pd.read_csv(os.path.join(directory, y_filename), encoding='utf-8', skiprows=4,
                                 names=["Time", y_filename])

            plt.plot(x_file[x_filename], y_file[y_filename], color="g", alpha=0.7)
            plt.title(f"Plot for {filename}")
            plt.xlabel(x_filename)
            plt.ylabel(y_filename)
            plt.tight_layout()  # Make sure the layout isn't clipped
            name = " ".join([xy_files[0], xy_files[1]]) + ".pdf"
            plt.savefig(os.path.join(directory, name), format="pdf")
            plt.show()


        elif "FFT" in filename:
            fft_files = filename.split(".csv")[0].split(" FFT")
            fft_filename = fft_files[0] + ".csv"
            file = pd.read_csv(os.path.join(directory, fft_filename), skiprows=4, names=["Time", fft_filename],
                                 encoding='utf-8')
            # Extract time and signal values
            time = file["Time"].values
            signal = file["Modulant"].values
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
        else:
            print("Other filename are: ", filename)
            #file.columns = ['X', 'Y']

            # Plotting
            #plt.plot(file['X'], file['Y'])
            #plt.title(f"Plot for {filename}")
            #plt.xlabel("X")
            #plt.ylabel("Y")
            #plt.tight_layout()  # Make sure the layout isn't clipped
            #plt.show()

#"""