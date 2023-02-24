from StructureClass import Structure
from Plotting import Plot_Struct

import os
import matplotlib.pyplot as plt


SIZE = 5
TYPE_DATA = 'arranged'

folders_or = [file for file in os.listdir('Data/')]

# structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] == 'Bis']
structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != 'Bis']
# structures = [Structure(folder, TYPE_DATA) for folder in folders_or]

# plot_multi = Plot_Struct(SIZE, structures, 'line')
# plot_multi.plot_alls()

plot_lin = Plot_Struct(SIZE, structures, 'line')
plot_lin.plot_singles()


# plot_circ = Plot_Struct(SIZE, structures, 'circle')
# plot_circ.plot_alls(True, f'all_{TYPE_DATA}_bis')


plt.show()
# TO DO: 
# line-arranged-nobis
# line-random-all also create own dataset
# multicircle-random-nobis change that random finishes (maybe even create different dataset)
# multiline-random-bis(some) there are only 4 good ones, reshuffle to get weird creatures
