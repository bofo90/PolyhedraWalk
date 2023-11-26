import numpy as np

spot = [
    "autotune",
    "out of tune",
    "key change (modulation)",
    "fire",
    "verka serduchka",
    "germany 0 points",
    "uk 0 points",
    " disco ball",
    " rainbow flag",
    "presenter error",
    "camera error",
    "lyrics on screen",
    "political statement",
    "flute",
    "singer forgets song",
    "italy-malta douze points",
    "greece-cyprus douze point",
    "violin",
    "saxophone",
    "war in ukraine",
    "someone high",
    "fall",
    "fake rain",
    "barefoot",
    "wind machine",
]

print(np.random.choice(spot, 16, replace=False))
