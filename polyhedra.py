import os

import matplotlib.pyplot as plt

from Plotting import Plot_Struct
from StructureClass import Structure

SIZE = 5
TYPE_DATA = "arranged"
SAVE = False
NUM_PLOTS = 2

folders_or = [file for file in os.listdir("Data/")]

structures = [
    Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != "Bis"
]

plot_lin = Plot_Struct(SIZE, structures, "line")
for i in range(NUM_PLOTS):
    plot_lin.plot_singles(SAVE, f"Polyhedra/{i}")

if not SAVE:
    plt.show()
