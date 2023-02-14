import numpy as np


def PlotOne(folder_name, ax, numPlot, Circle=False, InitSt=True, Arranged=False):
    Ang, Len = ReadFileMat("Data/" + folder_name)

    initialState = np.argmin(np.sum(np.abs(Len), axis=1))
    if Arranged:
        Ang, Len = OrderData(Ang, Len)
    else:
        Ang, Len = ShuffleData(Ang, Len)
    x, y = getXYPath(Ang, Len, Circle)

    if np.size(Ang, 0) > numPlot:
        iterArray = np.random.choice(np.size(Ang, 0), numPlot, replace=False)
    else:
        iterArray = np.arange(np.size(Ang, 0))

    for i in iterArray:
        ax.plot(x[i, :], y[i, :], c="#E3E2E1", alpha=0.8, linewidth=0.7)
        # ax.plot(x[i,:],y[i,:], c = '#E8D6BA', alpha = 0.2, linewidth = 0.7)
        # ax.plot(x[i,:],y[i,:], c = '#21201F', alpha = 0.7, linewidth = 0.7)

    if InitSt:
        ax.plot(x[initialState, :], y[initialState, :], c="#CC0003", linewidth=1)

    return


def PlotOne2(
    struct, ax, numPlot, shiftx, shifty, Circle=False, InitSt=True, Arranged=False
):
    if np.size(struct.Ang, 0) > numPlot:
        iterArray = np.random.choice(np.size(struct.Ang, 0), numPlot, replace=False)
    else:
        iterArray = np.arange(np.size(struct.Ang, 0))

    for i in iterArray:
        ax.plot(
            struct.x[i, :] + shiftx,
            struct.y[i, :] + shifty,
            c="#E3E2E1",
            alpha=0.8,
            linewidth=0.7,
        )
        # c = '#21201F', alpha = 0.8, linewidth = 0.7)
        # ax.plot(x[i,:],y[i,:], c = '#E8D6BA', alpha = 0.2, linewidth = 0.7)
        # ax.plot(x[i,:],y[i,:], c = '#21201F', alpha = 0.7, linewidth = 0.7)

    if InitSt:
        ax.plot(
            struct.x[struct.initialState, :] + shiftx,
            struct.y[struct.initialState, :] + shifty,
            # c = '#E6258D', linewidth = 1) #red
            # c = '#CC0003', linewidth = 1) #pink
            # c = '#FFA826', linewidth = 1) #yellow
            c="#E6A800",
            linewidth=1,
        )  # gold
        # c = '#CC4229', linewidth = 1) #complementary green

    return
