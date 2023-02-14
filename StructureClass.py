import numpy as np

import ReadAndAnalyze as raa


class Structure:
    def __init__(self, folder_name, Arranged=False, Circle=False):
        self.folder = folder_name

        self.Ang, self.Len = raa.ReadFileMat("Data/" + folder_name)

        self.initialState = np.argmin(np.sum(np.abs(self.Len), axis=1))

        if Arranged:
            self.Ang, self.Len = raa.OrderData(self.Ang, self.Len)
        else:
            self.Ang, self.Len = raa.ShuffleData(self.Ang, self.Len)

        self.x, self.y = raa.getXYPath(self.Ang, self.Len, Circle)
