import os

import matplotlib.pyplot as plt

from Plotting import Plot_Struct
from StructureClass import Structure

SIZE = 2
TYPE_DATA = "random"
SAVE = False

folders_or = [file for file in os.listdir("Data/")]

structures = [
    Structure(folder, TYPE_DATA)
    for folder in folders_or
    if folder.endswith("1000") or folder.endswith("100")
]
# structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != 'Bis']
# structures = [Structure(folder, TYPE_DATA) for folder in folders_or]

# plot_lin = Plot_Struct(SIZE, structures, 'line')
# for i in range(100):
#     plot_lin.plot_singles(SAVE, f'LineArr/{i}')
# plot_lin.plot_singles()

# plot_circ = Plot_Struct(SIZE, structures, 'circle')
# plot_circ.plot_alls(SAVE, f'all_{TYPE_DATA}_bis')

plot_multi = Plot_Struct(SIZE, structures, "line")
plot_multi.plot_alls()


plt.show()
# TO DO:
# line-arranged-nobis
# line-random-all also create own dataset
# multicircle-random-nobis change that random finishes (maybe even create different dataset)
# multiline-random-bis(some) there are only 4 good ones, reshuffle to get weird creatures
