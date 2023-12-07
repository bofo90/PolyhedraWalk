import numpy as np


class Structure:
    def __init__(self, folder_name, data_process, seed=1):
        np.random.seed(seed)
        self.folder = folder_name

        self.AngOr, self.Len = self._readFileMat()
        self.initialState = self._getInitalState()
        self.plot_type = data_process

        if self.plot_type == "original":
            pass
        elif self.plot_type == "arranged":
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


class StructurePolyCircle:
    def __init__(self, num_lines=250, length_lines=150):
        angle = np.random.uniform(0, np.pi / 2)
        self.Ang, self.Len = self._getAngLen(num_lines=num_lines, length_lines=length_lines, angle=angle)
        self.initialState = self._getInitalState()

        rot_ang = np.random.uniform(-2 * np.pi, 2 * np.pi)
        self._getCircle()
        self._rotateStructure(rot_ang=rot_ang)

    def _getAngLen(self, num_lines, length_lines, angle):
        std_dev_stretch = 0.2
        std_dev_angle = 0.25
        angles1 = np.random.normal(loc=angle, scale=std_dev_angle, size=(int(2 * num_lines / 5), length_lines))
        angles2 = np.random.normal(loc=-angle, scale=std_dev_angle, size=(int(2 * num_lines / 5), length_lines))
        angles3 = np.random.normal(loc=0, scale=std_dev_angle, size=(int(num_lines / 5), length_lines))
        angles = np.concatenate([angles1, angles2, angles3], axis=0)

        noise = std_dev_angle
        angles = angles + np.random.uniform(low=-noise, high=noise, size=(num_lines, length_lines))

        lengths = np.random.normal(loc=0.0, scale=std_dev_stretch, size=(num_lines, length_lines))

        return angles, lengths

    def _getInitalState(self):
        initialState = [np.argmin(np.sum(np.abs(self.Len), axis=1))]
        return initialState

    def _getCircle(self):
        self.Ang = np.abs(self.Ang)
        totRot = np.sum(self.Ang, 1) / np.pi / np.random.normal(2, 0.25)
        for i in np.arange(np.size(self.Ang, 0)):
            self.Ang[i, :] = self.Ang[i, :] / totRot[i]

    def _rotateStructure(self, rot_ang):
        self.Ang[:, 0] = self.Ang[:, 0] + rot_ang
