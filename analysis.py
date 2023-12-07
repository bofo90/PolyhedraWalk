import os

import matplotlib.pyplot as plt
import numpy as np

from StructureClass import Structure

SIZE = 2
TYPE_DATA = "original"
SAVE = True
NUM_PLOTS = 25

folders_or = [file for file in os.listdir("Data/")]

structures = [
    Structure(folder, TYPE_DATA) for folder in folders_or if folder.endswith("1000") or folder.endswith("100")
]

for struct in structures:
    fig, axes = plt.subplots(1, 2)
    angles = struct.AngOr / np.pi
    lengths = struct.Len
    print("angles", np.max(angles), np.min(angles), np.shape(angles))
    print("lengths", np.max(lengths), np.min(lengths), np.shape(lengths))
    angles, lengths = np.round((angles, lengths), 2)
    axes[0].hist(angles.flatten(), bins=100, range=(-1, 1))
    axes[1].hist(lengths.flatten(), bins=100, range=(-0.1, 0.1))

    fig2, axes2 = plt.subplots(1, 2)
    _, count_angles = np.unique(angles, axis=0, return_counts=True)
    _, count_lengths = np.unique(lengths, axis=0, return_counts=True)
    count_angles_low = count_angles[count_angles <= 50]
    count_angles_high = count_angles[count_angles > 50]
    print("angles low:", len(count_angles_low), min(count_angles_low), max(count_angles_low))
    print("angles high:", len(count_angles_high), min(count_angles_high), max(count_angles_high))
    axes2[0].hist(count_angles, bins=100)
    axes2[1].hist(count_lengths, bins=100)

    # Conclusion:
    # - Angles can be either zero or +- a specific value (0.75pi or 0.25pi).
    #   This is with probability 50% zero, 25% -angle, 25% +angle.
    #   For small angles maybe we can skip the zero angle.
    # - Lengths are zero (no stretch).
    #   Optionally we can get stretch from a normal distribution around zero
    # - There around 30 unique arrays with counts below 25,
    #   but there are 4 arrays with counts around 150

plt.show()

# ToDo:
# - create arrays with +-angle and zero (optional, no zero)
# - normal disrtibution of lengths around 0 (optional, play with std_dev, or non existant)
# - length of array is 150 (optional, smaller and bigger)
# - have around 35 different arrays
# - check how many same arrays to make it thick or just play with the alpha when plotting
