import matplotlib.pyplot as plt
import numpy as np


class Plot_Struct:
    def __init__(self, size, structures, plot_type, seed=0) -> None:

        np.random.seed(seed)

        self.size = size
        self.structures = structures

        self.plot_type = plot_type
        if plot_type == 'circle':
            self.do_circles()
        elif plot_type == 'line':
            pass
        else:
            raise Exception("Plot type not recognized. Please select 'line' or 'circle'")

        self.getXYPaths()

    def create_fig(self):
        self.fig, self.axes = plt.subplots(self.size, self.size, figsize=(5.4, 5.4), facecolor='#21201F')
        self.fig.subplots_adjust(left=0.,
                                 bottom=0.,
                                 right=1.,
                                 top=1.,
                                 wspace=0.,
                                 hspace=0.)
        if self.size == 1:
            self.axes = np.array(self.axes)
            self.special = []
        else:
            self.axes = self.axes.flatten()
            self.special = np.random.choice(self.size**2, int(np.ceil((self.size**2)*0.1)))
        [ax.axis("off") for ax in self.axes]

        self.plot_structs = np.random.choice(len(self.structures), self.size**2, 
                                             replace=len(self.structures) < self.size**2)

    def plot_alls(self, save=False, name=''):
        self.create_fig()

        for i, struct in enumerate(self.plot_structs):
            if i in self.special:
                self.plot_single_strcut(self.axes[i], self.structures[struct], "initial")
            self.plot_single_strcut(self.axes[i], self.structures[struct], "all")

        if save:
            plt.savefig(f'{name}.png', dpi=300)
            plt.close(self.fig)

    def plot_singles(self, save=False, name=''):
        self.create_fig()

        for i, struct in enumerate(self.plot_structs):
            if i in self.special:
                self.plot_single_strcut(self.axes[i], self.structures[struct], "initial")
            else:
                self.plot_single_strcut(self.axes[i], self.structures[struct], "one")

        if save:
            plt.savefig(f'{name}.png', dpi=300)
            plt.close(self.fig)

    def do_circles(self):

        for struct in self.structures:
            struct.Ang = np.abs(struct.Ang)
            totRot = np.sum(struct.Ang, 1) / np.random.uniform(1.9, 2.1) / np.pi
            for i in np.arange(np.size(struct.Ang, 0)):
                struct.Ang[i, :] = struct.Ang[i, :] / totRot[i]

        return

    def plot_single_strcut(self, ax, struct, amount):

        if amount == "initial" and len(struct.initialState) > 0:
            iterArray = struct.initialState
            color = "#E6A800"
            alpha = 1
            linewidth = 1
        elif amount == "one" or (amount == "initial" and len(struct.initialState) == 0):
            iterArray = np.random.choice(np.size(struct.Ang, 0), 1)
            color = "#E3E2E1"
            alpha = 0.8
            linewidth = 0.7
        elif amount == "all":
            iterArray = np.arange(np.size(struct.Ang, 0))
            color = "#E3E2E1"
            alpha = 0.2
            linewidth = 0.7
        else:
            raise Exception("Wrong type of plotting, choose between 'initial', 'one' or 'all'")

        maxX, minX, maxY, minY = self.getRange(struct, iterArray)

        for i in iterArray:
            ax.plot(
                struct.x[i, :],
                struct.y[i, :],
                c=color,
                alpha=alpha,
                linewidth=linewidth,
            )
            ax.set_xlim([minX, maxX])
            ax.set_ylim([minY, maxY])
            # c = '#21201F' black
            # c = '#E8D6BA' crema
            # c = '#E6258D' pink
            # c = '#CC0003' red
            # c = '#FFA826' yellow/orange
            # c = '#CC4229' complementary green (red-orange)
            # c = '#29cc42' green

    def getXYPaths(self):

        for struct in self.structures:
            Ang = self.runingSum(struct.Ang)

            x = np.cos(Ang) * (struct.Len + 1)
            y = np.sin(Ang) * (struct.Len + 1)

            struct.x = self.runingSum(x)
            struct.y = self.runingSum(y)

        return

    def runingSum(self, a):
        a_sum = np.zeros(np.shape(a))

        for i in np.arange(np.size(a, 0)):
            a_sum[i, :] = np.convolve(a[i, :], np.ones(np.shape(a[i, :])))[: np.size(a, 1)]

        return a_sum

    def getRange(self, struct, iterArray):

        maxX, minX, maxY, minY = 0, 0, 0, 0
        scale = 1.4

        for i in iterArray:
            maxX = max(maxX, np.max(struct.x[i, :]))
            minX = min(minX, np.min(struct.x[i, :]))
            maxY = max(maxY, np.max(struct.y[i, :]))
            minY = min(minY, np.min(struct.y[i, :]))

        xrange = (maxX-minX)*scale/2
        yrange = (maxY-minY)*scale/2

        return maxX+xrange, minX-xrange, maxY+yrange, minY-yrange
