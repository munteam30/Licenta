
# from Trial import *
import numpy as np
import pandas as pd
import Windower as fct
from sklearn.preprocessing import StandardScaler
import os
from matplotlib import pyplot as plt
def Save_mean_and_varaince(scaler, ID):
    mean = scaler.mean_
    np.savetxt('D:/LICENTA/py/Medie/medie'+ ID+'.txt', mean)

    std = scaler.var_
    np.savetxt('D:/LICENTA/py/Varianta/std'+ ID+'.txt', std)

# Denumire model pentru antrenare:

# denumire = "Models/12s-200-160.h5"    #Modelul 12s-200-100 merge ok pentru 550 esantioane
# model = tf.keras.models.load_model(denumire)
formatare = 1
if formatare == 1:
    format = 0
    files = os.listdir('D:/LICENTA/Date_test/')
    files.sort()
    flagF = 0
    for Fisier in files:
        result = result1 = result2 = result3 = []
        denumire = 'D:/LICENTA/Date_test/' + str(Fisier)
        Label = str(Fisier)[2]
        if len(str(Fisier)) == 10:
            Label = str(Fisier)[3]
        if format == 0:
            df = pd.read_csv(denumire, sep=";", engine="python", usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
        else:
            df = pd.read_csv(denumire, usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
        for epsilon in range(4):
            flag = 0
            ferestre = fct.Windower(np.asarray(df.values[:, epsilon]), 200, 160)  # inainte folosisem 200-50
            for i in ferestre:
                if epsilon == 0:
                    AX = np.array(
                        [Label, fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
                         fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                    if flag == 0: result = AX
                    if flag > 0: result = np.vstack((result, AX))
                elif epsilon == 1:
                    AY = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
                                   fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                    if flag > 0:
                        result1 = np.vstack((result1, AY))
                    else:
                        result1 = AY

                elif epsilon == 2:
                    GX = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
                                   fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                    if flag > 0:
                        result2 = np.vstack((result2, GX))
                    else:
                        result2 = GX

                elif epsilon == 3:
                    GY = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
                                   fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                    if flag > 0:
                        result3 = np.vstack((result3, GY))
                    else:
                        result3 = GY
                flag += 1

        for i in range(3):
            if i == 0: denumire = result1
            if i == 1: denumire = result2
            if i == 2: denumire = result3
            result = np.column_stack((result, denumire))
        if flagF == 0:
            FINAL = result
            flagF += 1
        else:
            FINAL = np.vstack((FINAL, result))
        print(FINAL.shape)
    for i in range(24):
        coloana = np.asarray(FINAL[:, i + 1])
        FINAL[:, i + 1] = fct.Normalizare(coloana)


    np.save('D:/LICENTA/Features/date_test.npy', np.asarray(FINAL), allow_pickle=True)
    print('Done Date_test.npy!!')

Data = np.load('D:/LICENTA/Features/Date_test.npy',allow_pickle=True)
Labels = Data[:,0]
Features = Data[:, 1:]

class0 = []
class1 = []
class2 = []
class3 = []
for i in range(len(Data)):
    if Data[i,0] == '0':
        # class0 = np.vstack([class0,Features[i,:]])
        class0.append(Features[i,:])
    if Data[i,0] == '1':
        class1.append(Features[i,:])
        # class1 = np.vstack([class1,Features[i,:]])
    if Data[i,0] == '2':
        class2.append(Features[i, :])
        # class2= np.vstack([class2,Features[i,:]])
    if Data[i,0] == '3':
        class3.append(Features[i, :])
        # class3 = np.vstack([class3,Features[i,:]])
Features = []

class0 = np.asanyarray(class0)
class1 = np.asanyarray(class1)
class2 = np.asanyarray(class2)
class3 = np.asanyarray(class3)

Features.extend(class0)
Features.extend(class1)
Features.extend(class2)
Features.extend(class3)
Features = np.asanyarray(Features)

from scipy import stats

scaler0 = StandardScaler()
class0 = scaler0.fit_transform(class0)
print(scaler0.scale_)
Save_mean_and_varaince(scaler0,"0")
mean0 = np.loadtxt('D:/LICENTA/py/Medie/medie0.txt')
std0  = np.loadtxt('D:/LICENTA/py/Varianta/std0.txt')
x = []
distante = []
for i in range(len(mean0)):
    y = np.linspace(mean0[i] - 3*std0[i], mean0[i] + 3*std0[i], 100)
    x.append(y)
for i in x:
    dist = i[-1] - i[0]
    distante.append(dist)
labels = ['MeanAbsoluteAX','ZeroFreqRateAX','WaveLengthAX','RootMeanSquareAX','SlopeSignChangeAX','HjorthAX','MeanAbsoluteAY','ZeroFreqRateAY','WaveLengthAY','RootMeanSquareAY','SlopeSignChangeAY','HjorthAY','MeanAbsoluteGX','ZeroFreqRateGX','WaveLengthGX','RootMeanSquareGX','SlopeSignChangeGX','HjorthGX','MeanAbsoluteGY','ZeroFreqRateGY','WaveLengthGY','RootMeanSquareGY','SlopeSignChangeGY','HjorthGY']
plt.figure()
# print(len(labels))
for i in range(len(mean0)):

    plt.plot(x[np.argmax(distante)], stats.norm.pdf(x[np.argmax(distante)], mean0[i], std0[i]),label = labels[i] )
plt.legend()
plt.show()


scaler1 = StandardScaler()
class1 = scaler1.fit_transform(class1)
print(scaler1.scale_)
Save_mean_and_varaince(scaler1,"1")
mean1 = np.loadtxt('D:/LICENTA/py/Medie/medie1.txt')
std1  = np.loadtxt('D:/LICENTA/py/Varianta/std1.txt')

x = []
distante = []
for i in range(len(mean1)):
    y = np.linspace(mean1[i] - 3*std1[i], mean1[i] + 3*std1[i], 100)
    x.append(y)
plt.figure()
for i in x:
    dist = i[-1] - i[0]
    distante.append(dist)

for i in range(len(mean1)):
    plt.plot(x[np.argmax(distante)], stats.norm.pdf(x[np.argmax(distante)], mean1[i], std1[i]),label = labels[i])
plt.legend()
plt.show()


scaler2 = StandardScaler()
class2 = scaler2.fit_transform(class2)
print(scaler2.scale_)
Save_mean_and_varaince(scaler2,"2")
mean2 = np.loadtxt('D:/LICENTA/py/Medie/medie2.txt')
std2  = np.loadtxt('D:/LICENTA/py/Varianta/std2.txt')

x = []
distante = []
for i in range(len(mean2)):
    y = np.linspace(mean2[i] - 3*std2[i], mean2[i] + 3*std2[i], 100)
    x.append(y)
for i in x:
    dist = i[-1] - i[0]
    distante.append(dist)
plt.figure()
for i in range(len(mean2)):

    plt.plot(x[np.argmax(distante)], stats.norm.pdf(x[np.argmax(distante)], mean2[i], std2[i]),label = labels[i])
plt.legend()
plt.show()


scaler3 = StandardScaler()
class3 = scaler3.fit_transform(class3)
Save_mean_and_varaince(scaler3,"3")
mean3 = np.loadtxt('D:/LICENTA/py/Medie/medie3.txt')
std3  = np.loadtxt('D:/LICENTA/py/Varianta/std3.txt')
x = []
distante = []
for i in range(len(mean3)):
    y = np.linspace(mean3[i] - 3*std3[i], mean3[i] + 3*std3[i], 100)
    x.append(y)
for i in x:
    dist = i[-1] - i[0]
    distante.append(dist)
plt.figure()
for i in range(len(mean3)):

    plt.plot(x[np.argmax(distante)], stats.norm.pdf(x[np.argmax(distante)], mean3[i], std3[i]),label = labels[i])
plt.legend()
plt.show()


scaler = StandardScaler()
Features = scaler.fit_transform(Data[:, 1:])
print(scaler.scale_)
Save_mean_and_varaince(scaler,"9")
mean9 = np.loadtxt('D:/LICENTA/py/Medie/medie9.txt')
std9  = np.loadtxt('D:/LICENTA/py/Varianta/std9.txt')

x = []
distante = []
for i in range(len(mean9)):
    y = np.linspace(mean9[i] - 3*std9[i], mean9[i] + 3*std9[i], 100)
    x.append(y)
plt.figure()
for i in x:
    dist = i[-1] - i[0]
    distante.append(dist)
for i in range(len(mean9)):
    plt.plot(x[np.argmax(distante)], stats.norm.pdf(x[np.argmax(distante)], mean9[i], std9[i]),label = labels[i])
plt.legend()
plt.show()

