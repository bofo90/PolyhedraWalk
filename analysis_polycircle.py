import os

import matplotlib.pyplot as plt
import numpy as np

from StructureClass import Structure

SIZE = 2
TYPE_DATA = "random"
SAVE = False

folders_or = [file for file in os.listdir("Data/")]

cool_fig = ["hexagonal prism", "rhombicuboctahedron", "truncated tetrahedron", "truncated cuboctahedron"]

# structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != "Bis"]
structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder in cool_fig]

for struct in structures:
    fig, axes = plt.subplots(1, 2)
    angles = struct.AngOr / np.pi
    lengths = struct.Len
    print("angles", np.max(angles), np.min(angles), np.shape(angles))
    print("lengths", np.max(lengths), np.min(lengths), np.shape(lengths))
    # angles, lengths = np.round(angles, 2), np.round(lengths, 2)
    axes[0].hist(angles.flatten(), bins=100, range=(-1, 1))
    axes[1].hist(lengths.flatten(), bins=100, range=(-0.5, 0.5))


plt.show()

# Conclusion (few polyhedra):
# - Angles follow a uniform distribution with a few peaks around specific angles
# - Lengths follow a normal distribution around 0.


# ToDo:
# - create arrays with +-angle and zero (optional, no zero)
# - normal disrtibution of lengths around 0 (optional, play with std_dev, or non existant)
# - length of array is 150 (optional, smaller and bigger)
# - have around 35 different arrays
# - check how many same arrays to make it thick or just play with the alpha when plotting
