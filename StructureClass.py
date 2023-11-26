import numpy as np


class Structure:
    def __init__(self, folder_name, data_process, seed=1):
        np.random.seed(seed)
        self.folder = folder_name

        self.AngOr, self.Len = self._readFileMat()
        self.initialState = self._getInitalState()
        self.plot_type = data_process

        if self.plot_type == "arranged":
            self.orderData()
        elif self.plot_type == "random":
            self.shuffleData()
        else:
            raise Exception("Data process not recognized. Please select 'arranged' or 'random'")

    def _readFileMat(self):
        file_name1 = "/Angles.csv"
        file_name2 = "/Edges.csv"

        dataAngles = np.loadtxt(
            "Data/" + self.folder + file_name1,
            skiprows=0,
            delimiter=",",
            dtype=np.float64,
        )

        dataLen = np.loadtxt(
            "Data/" + self.folder + file_name2,
            skiprows=0,
            delimiter=",",
            dtype=np.float64,
        )

        return dataAngles, dataLen

    def _getInitalState(self):
        if self.folder[:3] == "Bis":
            initialState = []
        else:
            initialState = [np.argmin(np.sum(np.abs(self.Len), axis=1))]
        return initialState

    def shuffleData(self, seed=None):
        if seed is not None:
            np.random.seed(seed)
        ranLen = np.arange(np.size(self.Len, 1))
        np.random.shuffle(ranLen)
        self.Len = self.Len[:, ranLen]

        ranAng = np.random.randint(0, np.size(self.AngOr, 1) - 1, np.size(self.Len, 1))
        self.Ang = self.AngOr[:, ranAng]

    def orderData(self):
        self.Len = np.sort(self.Len, axis=1)

        ranAng = np.arange(np.size(self.Len, 1)) % np.size(self.AngOr, 1)
        self.Ang = self.AngOr[:, ranAng]
        self.Ang = np.sort(self.Ang, axis=1)
