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
    print("angles", np.max(angles), np.min(angles), "\nlengths", np.max(lengths), np.min(lengths))
    angles, lengths = np.round((angles, lengths), 2)
    axes[0].hist(angles.flatten(), bins=100, range=(-1, 1))
    axes[1].hist(lengths.flatten(), bins=100, range=(-0.1, 0.1))

    # Conclusion:
    # - Angles can be either zero or +- a specific value (0.75pi or 0.25pi).
    #   This is with probability 50% zero, 25% -angle, 25% +angle.
    #   For small angles maybe we can skip the zero angle.
    # - Lengths are zero (no stretch).
    #   Optionally we can get stretch from a normal distribution around zero
    # Still to do:
    # Analysis of how many different arrays there are.

plt.show()
