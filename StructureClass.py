import numpy as np


class Structure:
    def __init__(self, folder_name, data_process):
        self.folder = folder_name

        self.Ang, self.Len = self.readFileMat()
        self.initialState = self.getInitalState()
        self.plot_type = data_process

        if self.plot_type == 'arranged':
            self.orderData()
        elif self.plot_type == 'random':
            self.shuffleData()
        else:
            raise Exception("Data process not recognized. Please select 'arranged' or 'random'")

        self.x, self.y = self.getXYPath()

    def readFileMat(self):
        file_name1 = "/Angles.csv"
        file_name2 = "/Edges.csv"

        dataAngles = np.loadtxt(
            "Data/" + self.folder + file_name1, skiprows=0, delimiter=",", dtype=np.float64
        )

        dataLen = np.loadtxt(
            "Data/" + self.folder + file_name2, skiprows=0, delimiter=",", dtype=np.float64
        )

        return dataAngles, dataLen

    def getInitalState(self):
        if self.folder[:3] == "Bis":
            initialState = []
        else:
            initialState = [np.argmin(np.sum(np.abs(self.Len), axis=1))]
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
