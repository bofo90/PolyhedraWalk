from Plotting import Plot_Struct
from StructureClass import Structure

import os
import matplotlib.pyplot as plt


SIZE = 2
TYPE_DATA = 'random'
SAVE = True
NUM_PLOTS = 25

folders_or = [file for file in os.listdir('Data/')]

structures = [Structure(folder, TYPE_DATA) for folder in folders_or if folder.endswith('1000') or folder.endswith('100')]


# # Plot with 4 structures
# for i in range(NUM_PLOTS):
#     [structure.shuffleData() for structure in structures]
#     plot_multi = Plot_Struct(SIZE, structures, 'line', scale=0.5)
#     plot_multi.plot_alls(SAVE, f'Polyinsects/tog_test{i}')
#     # plot_multi.plot_alls_alpha_variable(SAVE, f'Polyinsects/alpha_test{i}')

# # Plot one single structure with defined alpha
# for i in range(NUM_PLOTS):
#     for j, structure in enumerate(structures):
#         structure.shuffleData(seed=i)
#         plot_multi = Plot_Struct(1, [structure], 'line', scale=0.1)
#         plot_multi.plot_alls(SAVE, f'Polyinsects/test_{i}_{j}')

# Plot for different alphas
i, j = 13, 3
structure = structures[j]
structure.shuffleData(seed=i)
plot_multi = Plot_Struct(1, [structure], 'line', scale=0.1)
# plot_multi.plot_alls(SAVE, f'Polyinsects/test_{i}_{j}')
plot_multi.plot_alls_alpha_variable(SAVE, f'Polyinsects/alpha_{i}_{j}')


if not SAVE:
    plt.show()

# TO DO:
# create aplha variable
#   check how many images are needed for the gif (frames per second for how many seconds ~3/4)
#   check software to create gif from images, check if instagram supports gif
