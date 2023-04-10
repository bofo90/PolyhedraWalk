from StructureClass import Structure
from Plotting import Plot_Struct

import os


SIZE = 5
TYPE_DATA = 'arranged'
SAVE = True

folders_or = [file for file in os.listdir('Data/')]

structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder[:3] != 'Bis']

plot_lin = Plot_Struct(SIZE, structures, 'line')
for i in range(100):
    plot_lin.plot_singles(SAVE, f'LineArr/{i}')
