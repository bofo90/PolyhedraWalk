from Plotting import Plot_Struct
from StructureClass import Structure

import os
import matplotlib.pyplot as plt


SIZE = 2
TYPE_DATA = 'random'
SAVE = False

folders_or = [file for file in os.listdir('Data/')]

structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder.endswith('1000') or folder.endswith('100')]


for i in range(3):
    [structure.shuffleData() for structure in structures]
    plot_multi = Plot_Struct(SIZE, structures, 'line', scale=0.5)
    plot_multi.plot_alls()
    # Error: it stops shuffling the Data. Use new method with random generator


plt.show()
# TO DO:
# Fix shuffling data
# Choose nice color for "insect"
# generate images and choose the best
