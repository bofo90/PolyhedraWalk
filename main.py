from StructureClass import Structure
from Plotting import Plot_Struct

import os


SIZE = 5

folders_or = [file for file in os.listdir('Data/')]

# structures = [Structure(folder, 'random') for folder in folders_or if folder[:3] == 'Bis']
structures = [Structure(folder, 'random') for folder in folders_or if folder[:3] != 'Bis']
# structures = [Structure(folder, 'random') for folder in folders_or]

plot = Plot_Struct(SIZE, structures, 'circle')

plot.plot_alls()
# plot.plot_singles()

# TO DO: 
# 

