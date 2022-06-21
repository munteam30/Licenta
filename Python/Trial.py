# -*- coding: utf-8 -*-

import Windower as fct
import pandas as pd
import numpy as np
import os
def Total_esantioane():
    files = os.listdir('D:/LICENTA/OwnDatabase/')
    files.sort()
    total = np.zeros(4)

    for Fisier in files:
        result = result1 = result2 = result3 = []
        denumire = 'D:/LICENTA/Owndatabase/' + str(Fisier)
        df = pd.read_csv(denumire, usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
        total = np.vstack([total, df])

    print(len(total))


#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#888888888888888888888 Meniul de editare 88888888888888888888888888888888888888888888888888888
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

Total_esantioane()
Length = 200
Overlap = 160
format = 1                 # 0- NU               1- DA
format_test = 0
baza_de_date = 0          # 0- Doar date_test   1- Ambele


#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888



if baza_de_date==1:
    files = os.listdir('D:/LICENTA/OwnDatabase/')
    files.sort()
    flagF = 0
    for Fisier in files:
        result = result1 = result2 = result3 = []
        denumire = 'D:/LICENTA/Owndatabase/' +str(Fisier)
        Label = str(Fisier)[2]
        if len(str(Fisier)) == 10:
            Label = str(Fisier)[3]

        df = pd.read_csv(denumire,usecols = ['Accel_X','Accel_Y','Gyro_X','Gyro_Y'])
        for epsilon in range(4):
            flag = 0
            ferestre = fct.Windower(np.asarray(df.values[:,epsilon]),Length,Overlap)    # inainte folosisem 200-50
            for i in ferestre:
                if epsilon == 0:
                   AX = np.array([Label,fct.MeanAbsolute(i),fct.ZeroFreqRate(i,0),fct.WaveLength(i),fct.RootMeanSquare(i),fct.SlopeSignChange(i,0),fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                   if flag == 0: result = AX
                   if  flag > 0: result = np.vstack((result,AX))
                elif epsilon==1:
                   AY = np.array([fct.MeanAbsolute(i),fct.ZeroFreqRate(i,0),fct.WaveLength(i),fct.RootMeanSquare(i),fct.SlopeSignChange(i,0),fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                   if flag > 0:result1 = np.vstack((result1,AY))
                   else: result1 = AY

                elif epsilon == 2:
                   GX = np.array([fct.MeanAbsolute(i),fct.ZeroFreqRate(i,0),fct.WaveLength(i),fct.RootMeanSquare(i),fct.SlopeSignChange(i,0),fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                   if flag>0:result2 = np.vstack((result2,GX))
                   else:result2 = GX

                elif epsilon == 3:
                   GY = np.array([fct.MeanAbsolute(i),fct.ZeroFreqRate(i,0),fct.WaveLength(i),fct.RootMeanSquare(i),fct.SlopeSignChange(i,0),fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
                   if flag>0:result3 = np.vstack((result3,GY))
                   else:result3 = GY
                flag+=1
        # for i in range(len(AX)):
        #     if i == 7:
        #         i = i-1
        #     coloana = np.asarray(result[:,i+1])
        #     result[:,i+1] = fct.Normalizare(coloana)
        # for i in range(len(AY)):
        #     coloana1 = np.asarray(result1[:,i])
        #     result1[:,i] = fct.Normalizare(coloana1)
        # for i in range(len(GX)):
        #     coloana = np.asarray(result2[:,i])
        #     result2[:,i] = fct.Normalizare(coloana)
        # for i in range(len(GY)):
        #     coloana1 = np.asarray(result3[:,i])
        #     result3[:,i] = fct.Normalizare(coloana1)
        for i in range(3):
           if i == 0: denumire = result1
           if i == 1: denumire = result2
           if i == 2: denumire = result3
           result = np.column_stack((result,denumire))

        if flagF == 0:
            FINAL = result
            flagF +=1
        else:
            FINAL = np.vstack((FINAL,result))
        print(FINAL.shape)
    for i in range(24):
               coloana = np.asarray(FINAL[:,i+1])
               FINAL[:,i+1] = fct.Normalizare(coloana)


    np.save('D:/LICENTA/Features/utils.npy', np.asarray(FINAL),allow_pickle=True)
    print('Done Utils.npy!!')

#***********************************************************************
#   Aici se formeaza datele pentru test
#***********************************************************************

files = os.listdir('D:/LICENTA/Date_test/')
files.sort()
flagF = 0
for Fisier in files:
    result = result1 = result2 = result3 = []
    denumire = 'D:/LICENTA/Date_test/' + str(Fisier)
    Label = str(Fisier)[2]
    if len(str(Fisier)) == 10:
        Label = str(Fisier)[3]
    if format_test == 0:
        df = pd.read_csv(denumire, sep=";", engine="python", usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
    else:
        df = pd.read_csv(denumire, usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
    for epsilon in range(4):
        flag = 0
        ferestre = fct.Windower(np.asarray(df.values[:, epsilon]), Length, Overlap)  # inainte folosisem 200-50
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
    # for i in range(len(AX)):
    #     if i == 7:
    #         i = i-1
    #     coloana = np.asarray(result[:,i+1])
    #     result[:,i+1] = fct.Normalizare(coloana)
    # for i in range(len(AY)):
    #     coloana1 = np.asarray(result1[:,i])
    #     result1[:,i] = fct.Normalizare(coloana1)
    # for i in range(len(GX)):
    #     coloana = np.asarray(result2[:,i])
    #     result2[:,i] = fct.Normalizare(coloana)
    # for i in range(len(GY)):
    #     coloana1 = np.asarray(result3[:,i])
    #     result3[:,i] = fct.Normalizare(coloana1)
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


np.save('D:/LICENTA/Features/Date_test.npy', np.asarray(FINAL), allow_pickle=True)
print('Done Date_test.npy!!')
#*******************************************************************************************
#
#     Rezultatul ar trebui sa arate de forma (x, 25) pentru ca prima coloana este Label-ul
# iar restul reprezinta cele 4 coloane de interes impreuna cu cate 7 caracteristici. Modul 
# in care functioneaza acest cod este ca scoate datele de la toate fisierele din OwnDatabase
# si le analizeaza impreuna facand un .npy cu toate datele de la toti oamenii. 
#     Pentru ca la modul in care am scris eu fisierele, actiunea se afla pe bitul 3/4, am 
# scris linia 14 care ne garanteaza ca label-ul este dat de actiune.
#
#*******************************************************************************************
