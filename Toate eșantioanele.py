import os
import pandas as pd
import numpy as np

files = os.listdir('D:/LICENTA/OwnDatabase/')
files.sort()
total = np.zeros(4)


for Fisier in files:
    result = result1 = result2 = result3 = []
    denumire = 'D:/LICENTA/Owndatabase/' +str(Fisier)
    df = pd.read_csv(denumire, usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
    total = np.vstack([total,df])

print(total)