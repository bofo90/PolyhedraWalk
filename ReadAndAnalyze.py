import numpy as np


def ReadFileMat(folder_name):
    file_name1 = "/Angles.csv"
    file_name2 = "/Edges.csv"

    dataAngles = np.loadtxt(
        folder_name + file_name1, skiprows=0, delimiter=",", dtype=np.float64
    )

    dataLen = np.loadtxt(
        folder_name + file_name2, skiprows=0, delimiter=",", dtype=np.float64
    )

    return dataAngles, dataLen


def getInitalState(Ang, Len):
    initialState = np.argmin(np.sum(np.abs(Len), axis=1))
    iniAng = Ang[initialState, :]
    iniLen = Len[initialState, :]
    Ang = np.delete(Ang, initialState, 0)
    Len = np.delete(Len, initialState, 0)

    return Ang, Len, iniAng, iniLen


def ShuffleData(Ang, Len):
    ranLen = np.arange(np.size(Len, 1))
    np.random.shuffle(ranLen)
    Len = Len[:, ranLen]

    ranAng = np.random.randint(0, np.size(Ang, 1) - 1, np.size(Len, 1))
    Ang = Ang[:, ranAng]

    return Ang, Len


def OrderData(Ang, Len):
    Len = np.sort(Len, axis=1)

    ranAng = np.arange(np.size(Len, 1)) % np.size(Ang, 1)
    Ang = Ang[:, ranAng]
    Ang = np.sort(Ang, axis=1)

    return Ang, Len


def getXYPath(Ang, Len, circle=False):
    if circle:
        Ang = np.abs(Ang)
        totRot = np.sum(Ang, 1) / 2.05 / np.pi
        for i in np.arange(np.size(Ang, 0)):
            Ang[i, :] = Ang[i, :] / totRot[i]

    Ang = runingSum(Ang)

    x = np.cos(Ang) * (Len + 1)
    y = np.sin(Ang) * (Len + 1)

    x = runingSum(x)
    y = runingSum(y)

    return x, y


def runingSum(a):
    a_sum = np.zeros(np.shape(a))

    for i in np.arange(np.size(a, 0)):
        a_sum[i, :] = np.convolve(a[i, :], np.ones(np.shape(a[i, :])))[: np.size(a, 1)]

    return a_sum


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
