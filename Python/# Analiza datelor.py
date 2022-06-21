# Analiza/Vizualizarea datelor în timp real
import pandas as pd
from matplotlib import pyplot as plt

plt.ion(), plt.show(), plt.cla()
persoana  = 99
actiune   = 2       # 0->STAT ; 1->MERS ; 2->ALERGAT ; 3->CAZATURA
incercare = 0      # Numaratoarea începe de la 1
format = 1
vizualizare = 0     # Asta e doar pentru vizualizarea datelor


if vizualizare == 1:
    ID = "%s_%s_%s" % (persoana, actiune, incercare)
    denumire = 'D:/LICENTA/Date_test/' + ID +'.csv'
else: denumire = 'D:/LICENTA/Date_test/0_0_0.csv'

if format == 1:
    Accel_X = pd.read_csv(denumire, sep= ";" , engine="python", skipfooter=1 ,usecols=['Accel_X'])
    Accel_Y = pd.read_csv(denumire, sep= ";" , engine="python", skipfooter=1 ,usecols=['Accel_Y'])
    Gyro_X = pd.read_csv(denumire, sep= ";" , engine="python", skipfooter=1 ,usecols=['Gyro_X'])
    Gyro_Y = pd.read_csv(denumire, sep= ";" , engine="python", skipfooter=1 ,usecols=['Gyro_Y'])
else:
    Accel_X = pd.read_csv(denumire, usecols=['Accel_X'])
    Accel_Y = pd.read_csv(denumire, usecols=['Accel_Y'])
    Gyro_X = pd.read_csv(denumire, usecols=['Gyro_X'])
    Gyro_Y = pd.read_csv(denumire, usecols=['Gyro_Y'])

x = range(len(Gyro_X))
plt.plot(x,Gyro_X,Accel_X)
plt.draw()

if vizualizare == 1:    plt.pause(10)
else:                   plt.pause(2)

if vizualizare == 0:
    exec(open("Trial.py").read())
    exec(open("Data_processing.py").read())
    exec(open("# Analiza datelor.py").read())

