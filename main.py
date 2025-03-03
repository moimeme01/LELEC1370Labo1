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

        if "X-Y" in filename:
            print("X-Y File is " + filename)
            xy_files = filename.split(".csv")[0].split(" ")
            x_filename = xy_files[0] + ".csv"
            x_file = pd.read_csv(os.path.join(directory, x_filename), encoding='utf-8', skiprows=3)
            y_filename = xy_files[1] + ".csv"
            y_file = pd.read_csv(os.path.join(directory, y_filename), encoding='utf-8', skiprows=3)


            x_file.columns = ['X', 'Y']
            y_file.columns = ['X', 'Y']

            plt.plot(x_file['X'], y_file['Y'])
            plt.title(f"Plot for {filename}")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.tight_layout()  # Make sure the layout isn't clipped
            plt.show()

        elif "FFT" in filename:
            pass
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