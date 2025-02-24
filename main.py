import os
import pandas as pd
import matplotlib.pyplot as plt
"""
Here is the windows version
"""
directory = "C:\\Users\\thibault\\Documents\\LabVIEW Projects\\Labo1_2025\\Documentation"

print(os.listdir(directory))

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename), encoding='utf-8', skiprows=3)
        file.columns = ['X', 'Y']

        # Plotting
        plt.plot(file['X'], file['Y'])
        plt.title(f"Plot for {filename}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.tight_layout()  # Make sure the layout isn't clipped
        plt.show()


"""
Here is the MACos version

directory = "thibault\Documents\LabVIEW Projects\Labo1_2025\Documentation"

print(os.listdir(directory))

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename), encoding='utf-8', skiprows=3)
        file.columns = ['X', 'Y']

        # Plotting
        plt.plot(file['X'], file['Y'])
        plt.title(f"Plot for {filename}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.tight_layout()  # Make sure the layout isn't clipped
        plt.show()
"""