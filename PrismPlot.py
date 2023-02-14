import matplotlib.pyplot as plt
import numpy as np

import ReadAndAnalyze as raa


def cm2inch(value):
    return value / 2.54


folders_or = [
    "tetrahedron",
    "octahedron",
    "cube",
    "truncated tetrahedron",
    "cuboctahedron",
    "dodecahedron",
    "truncated cube",
    "truncated octahedron",
    "rhombicuboctahedron",
    "truncated cuboctahedron",
    "triangular prism",
    "hexagonal prism",
    # 'Bistable_4_0.785_0.00100', 'Bistable_4_0.785_0.01000',
    # 'Bistable_4_0.785_0.10000', 'Bistable_4_0.785_1.00000',
    # 'Bistable_4_2.356_0.00100', 'Bistable_4_2.356_0.01000',
    # 'Bistable_4_2.356_0.10000', 'Bistable_4_2.356_1.00000']
    "Bistable_8_0.785_0.00100",
    "Bistable_8_0.785_0.01000",
    "Bistable_8_0.785_0.10000",
    "Bistable_8_0.785_1.00000",
    "Bistable_8_2.356_0.00100",
    "Bistable_8_2.356_0.01000",
    "Bistable_8_2.356_0.10000",
    "Bistable_8_2.356_1.00000",
]

# if not os.path.isdir('CoverRandom/'):
#     os.mkdir('CoverRandom/')

# for seed in np.arange(30)+30:
#     np.random.seed(seed)
np.random.seed(41)  # 12 for circles #41 for lines
folders = np.random.permutation(folders_or)

# fig = plt.figure(figsize=(cm2inch(34), cm2inch(24)))
fig = plt.figure(figsize=(cm2inch(17), cm2inch(24)))
fig2 = plt.figure(figsize=(cm2inch(17), cm2inch(24)))

# shift_x = 1/3./2
shift_x = 1 / 3.0
shift_y = 0.25
size_incm = 3
# size_x = size_incm/17/2
size_x = size_incm / 17
size_y = size_incm / 24

numPlot = 1
k = 0
for i in np.arange(3):
    for j in np.arange(4):
        folder_name = folders[k]
        k += 1

        ax = fig.add_axes(
            (
                shift_x / 2 - size_x / 2 + shift_x * i,
                1 / 8 - size_y / 2 + shift_y * j,
                size_x,
                size_y,
            )
        )
        ax.axis("off")

        if folder_name[:3] == "Bis":
            raa.PlotOne(folder_name, ax, numPlot, InitSt=False)
        else:
            raa.PlotOne(folder_name, ax, numPlot)

        if j == 2 or (j == 0 and i == 2):
            continue
        folder_name = folders[k]
        k += 1

        # ax = fig.add_axes((shift_x/2-size_x/2+shift_x*i+0.5,1/8-size_y/2+shift_y*j,size_x,size_y))
        ax = fig2.add_axes(
            (
                shift_x / 2 - size_x / 2 + shift_x * i,
                1 / 8 - size_y / 2 + shift_y * j,
                size_x,
                size_y,
            )
        )
        ax.axis("off")

        if folder_name[:3] == "Bis":
            raa.PlotOne(folder_name, ax, numPlot, InitSt=False)
        else:
            raa.PlotOne(folder_name, ax, numPlot)


# fig.savefig('CoverRandom/%d_Cover_back.png' %seed, transparent = True)
# fig.savefig('Cover_back_2.pdf', transparent = True)
# fig2.savefig('Cover_front_2.pdf', transparent = True)
# plt.close('all')

plt.show()
