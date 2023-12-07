import os

import matplotlib.pyplot as plt

from Plotting import Plot_Struct
from StructureClass import Structure

SIZE = 2
TYPE_DATA = "random"
SAVE = False

folders_or = [file for file in os.listdir("Data/")]

cool_fig = ["hexagonal prism", "rhombicuboctahedron", "truncated tetrahedron", "truncated cuboctahedron"]

# structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != "Bis"]
structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder in cool_fig]

plot_multi = Plot_Struct(SIZE, structures, "circle")
plot_multi.plot_alls_w_initial()


plt.show()
