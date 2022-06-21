import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


persoana  = 5

actiune   = 2       # 0->STAT ; 1->MERS ; 2->ALERGAT ; 3->CAZATURA
incercare = 1

ID = "%s_%s_%s" % (persoana, actiune, incercare)
denumire = 'D:/LICENTA/OwnDatabase/' + ID +'.csv'

Accel_X = pd.read_csv(denumire, usecols=['Accel_X'])
Accel_Y = pd.read_csv(denumire, usecols=['Accel_Y'])
Gyro_X = pd.read_csv(denumire, usecols=['Gyro_X'])
Gyro_Y = pd.read_csv(denumire, usecols=['Gyro_Y'])

accel_x = Accel_X[200:700].squeeze()
time = np.linspace(0,10,500)
accel_x_fft = np.abs((np.fft.fft(accel_x, 1024)))
freqs = np.fft.rfftfreq(1024) * 50
# plt.figure(),plt.xlabel('Timp [s]'),plt.ylabel('Accelerație [$m/{s^2}$]'), plt.plot(time,accel_x), plt.show()
plt.figure(),plt.xlabel('Frecvență [$Hz$]'),plt.ylabel('|X(k)|') ,plt.plot(freqs, accel_x_fft[:int(1024/2) + 1]), plt.show()
# print(freqs.shape)

# gyro_x = Gyro_X[200:700].squeeze()
# gyro_x_fft = np.abs((np.fft.fft(gyro_x, 1024)))
# freqs = np.fft.rfftfreq(1024) * 50
# plt.figure(), plt.plot(gyro_x), plt.show()
# plt.figure(), plt.plot(freqs, gyro_x_fft[:int(1024/2) + 1]), plt.show()
# print(freqs.shape)
