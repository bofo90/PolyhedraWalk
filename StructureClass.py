import numpy as np


class Structure:
    def __init__(self, folder_name, Arranged=False, Circle=False):
        self.folder = "Data/" + folder_name

        self.Ang, self.Len = self.readFileMat()
        self.initialState = self.getInitalState()

        if Arranged:
            self.orderData()
        else:
            self.Ang, self.Len = self.shuffleData()

        self.x, self.y = self.getXYPath(Circle)

    def readFileMat(self):
        file_name1 = "/Angles.csv"
        file_name2 = "/Edges.csv"

        dataAngles = np.loadtxt(
            self.folder + file_name1, skiprows=0, delimiter=",", dtype=np.float64
        )

        dataLen = np.loadtxt(
            self.folder + file_name2, skiprows=0, delimiter=",", dtype=np.float64
        )

        return dataAngles, dataLen

    def getInitalState(self):
        initialState = np.argmin(np.sum(np.abs(self.Len), axis=1))
        return initialState

    def shuffleData(self):
        ranLen = np.arange(np.size(self.Len, 1))
        np.random.shuffle(ranLen)
        self.Len = self.Len[:, ranLen]

        ranAng = np.random.randint(0, np.size(self.Ang, 1) - 1, np.size(self.Len, 1))
        self.Ang = self.Ang[:, ranAng]

        return

    def orderData(self):
        self.Len = np.sort(self.Len, axis=1)

        ranAng = np.arange(np.size(self.Len, 1)) % np.size(self.Ang, 1)
        self.Ang = self.Ang[:, ranAng]
        self.Ang = np.sort(self.Ang, axis=1)

        return

    def getXYPath(self, circle=False):
        if circle:
            self.Ang = np.abs(self.Ang)
            totRot = np.sum(self.Ang, 1) / 2.05 / np.pi
            for i in np.arange(np.size(self.Ang, 0)):
                self.Ang[i, :] = self.Ang[i, :] / totRot[i]

        Ang = self.runingSum(self.Ang)

        x = np.cos(Ang) * (self.Len + 1)
        y = np.sin(Ang) * (self.Len + 1)

        x = self.runingSum(x)
        y = self.runingSum(y)

        return x, y

    def runingSum(self, a):
        a_sum = np.zeros(np.shape(a))

        for i in np.arange(np.size(a, 0)):
            a_sum[i, :] = np.convolve(a[i, :], np.ones(np.shape(a[i, :])))[: np.size(a, 1)]

        return a_sum
