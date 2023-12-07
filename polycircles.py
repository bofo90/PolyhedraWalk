import os

import matplotlib.pyplot as plt
import numpy as np

from Plotting import Plot_Struct
from StructureClass import Structure, StructurePolyCircle

SIZE = 2
TYPE_DATA = "random"
SAVE = False
file_name = "Polycircle/test_seed"

# folders_or = [file for file in os.listdir("Data/")]
# cool_fig = ["hexagonal prism", "rhombicuboctahedron", "truncated tetrahedron", "truncated cuboctahedron"]
# structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder in cool_fig]

# structures = [StructurePolyCircle(std_dev_angle=i) for i in np.arange(0, 0.54, 0.06)]
# structures = [StructurePolyCircle(std_dev_stretch=i) for i in np.arange(0, 0.9, 0.1)]
# structures = [StructurePolyCircle(num_lines=i) for i in np.arange(100, 400, 50)]
# structures = [StructurePolyCircle(length_lines=i) for i in np.arange(50, 500, 50)]
# structures = [StructurePolyCircle(seed=i) for i in range(1, 10)]

structures = [StructurePolyCircle(seed=i) for i in range(9)]


plot_multi = Plot_Struct(SIZE, structures, "line", scale=0.1)
plot_multi.plot_alls_w_initial(save=SAVE, name=file_name)


plt.show()
