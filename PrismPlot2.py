import os.path

import matplotlib.pyplot as plt
import numpy as np

import ReadAndAnalyze as raa
import StructureClass as sc


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

if not os.path.isdir("CoverRandom2/"):
    os.mkdir("CoverRandom2/")

structures = []
for i in folders_or:
    structures.append(sc.Structure(i, Arranged=True))


x_div = 12
y_div = 17

# for seed in np.arange(30):
#     np.random.seed(seed)
np.random.seed(6)  # 12 for circles #41 for lines
perm_fol = np.random.permutation(np.arange(x_div * y_div * 2))

initFolders = np.zeros(np.shape(perm_fol))
initFolders[:12] = 1
initFolders = initFolders[perm_fol]

perm_fol = perm_fol % np.size(folders_or)


# fig = plt.figure(figsize=(cm2inch(34), cm2inch(24)))
fig = plt.figure(figsize=(cm2inch(17), cm2inch(24)))
# ax = plt.subplot(111)
# ax.axis('off')
# fig.subplots_adjust(top=1, bottom=0, left=0, right=1)

fig2 = plt.figure(figsize=(cm2inch(17), cm2inch(24)))
# ax2 = plt.subplot(111)
# ax2.axis('off')
# fig2.subplots_adjust(top=1, bottom=0, left=0, right=1)


# shift_x = 1/x_div/2
shift_x = 1 / x_div
shift_y = 1 / y_div
size_incm = 0.5
# size_x = size_incm/17/2
size_x = size_incm / 17
size_y = size_incm / 24

numPlot = 1
k = 0
for i in np.arange(x_div):
    for j in np.arange(y_div):
        ax = fig.add_axes(
            (
                shift_x / 2 - size_x / 2 + shift_x * i,
                shift_y / 2 - size_y / 2 + shift_y * j,
                size_x,
                size_y,
            )
        )
        ax.axis("off")

        if initFolders[k]:
            raa.PlotOne2(
                structures[perm_fol[k]], ax, 0, shift_x * i, shift_y * j, Arranged=True
            )
        else:
            raa.PlotOne2(
                structures[perm_fol[k]],
                ax,
                numPlot,
                shift_x * i,
                shift_y * j,
                InitSt=False,
                Arranged=True,
            )

        k += 1

        # ax = fig.add_axes((shift_x/2-size_x/2+shift_x*i+0.5,shift_y/2-size_y/2+shift_y*j,size_x,size_y))
        ax = fig2.add_axes(
            (
                shift_x / 2 - size_x / 2 + shift_x * i,
                shift_y / 2 - size_y / 2 + shift_y * j,
                size_x,
                size_y,
            )
        )
        ax.axis("off")

        if initFolders[k]:
            raa.PlotOne2(
                structures[perm_fol[k]], ax, 0, shift_x * i, shift_y * j, Arranged=True
            )
        else:
            raa.PlotOne2(
                structures[perm_fol[k]],
                ax,
                numPlot,
                shift_x * i,
                shift_y * j,
                InitSt=False,
                Arranged=True,
            )

        k += 1


# fig.savefig('CoverRandom2/%d_Cover.png' %seed, transparent = True)
# fig.savefig('Cover_back_4.pdf', transparent = True)
# fig2.savefig('Cover_front_4.pdf', transparent = True)
# plt.close('all')
plt.show()
