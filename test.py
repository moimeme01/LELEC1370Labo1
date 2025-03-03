import pandas as pd
import matplotlib.pyplot as plt

# Load data
modulant_file = "/Users/thibaultvanni/Documents/UCL/LELEC1360 - Télécommunications/Labo 1/modulant time with default value.csv"
modulated_file = "/Users/thibaultvanni/Documents/UCL/LELEC1360 - Télécommunications/Labo 1/modulated time with default value.csv"

# Read CSV files (skip metadata rows)
modulant_df = pd.read_csv(modulant_file, skiprows=4, names=["Time", "Modulant"])
modulated_df = pd.read_csv(modulated_file, skiprows=4, names=["Time", "Modulated"])


# Plot the signals
plt.figure(figsize=(12, 6))
plt.plot(modulant_df["Modulant"], modulated_df["Modulated"], label="Modulated (Y)", color="g", alpha=0.7)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Modulant and Modulated Signals Over Time")
plt.legend()
plt.grid()
plt.show()