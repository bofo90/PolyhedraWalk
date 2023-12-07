import matplotlib.pyplot as plt
import numpy as np

from Plotting import Plot_Struct
from StructureClass import StructurePolyCircle

SIZE = 2
SAVE = True

for i in range(100):
    file_name = f"Polycircle/test_angle_{i}"

    np.random.seed(i)
    structures = [StructurePolyCircle() for _ in range(SIZE**2)]

    plot_multi = Plot_Struct(SIZE, structures, "circle", scale=0.1)
    plot_multi.plot_alls_circle(save=SAVE, name=file_name)

if not SAVE:
    plt.show()
