
# from Trial import *
import numpy as np
import Windower as fct
# from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import sklearn
from datetime import datetime
import os
import pandas as pd
from matplotlib import pyplot as plt
def Save_mean_and_varaince(scaler, ID):
    mean = scaler.mean_
    np.savetxt('D:/LICENTA/py/medie'+ ID+'.txt', mean)

    std = scaler.scale_
    np.savetxt('D:/LICENTA/py/std'+ ID+'.txt', std)

# Denumire model pentru antrenare:

denumire = "Models/12s-200-160.h5"    #Modelul 12s-200-100 merge ok pentru 550 esantioane
train = 0 # 0- NU  1- DA




Data = np.load('D:/LICENTA/Features/utils.npy',allow_pickle=True)
Labels = Data[:,0]
Features = Data[:,1:]
scaler = StandardScaler()
Features = scaler.fit_transform(Features)
Save_mean_and_varaince(scaler,"9")

# class0 = np.zeros(24)
# class1 = np.zeros(24)
# class2 = np.zeros(24)
# class3 = np.zeros(24)
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


scaler0 = StandardScaler()
class0 = scaler0.fit_transform(class0)
Save_mean_and_varaince(scaler0,"0")
mean0 = np.loadtxt('D:/LICENTA/py/medie0.txt')
std0  = np.loadtxt('D:/LICENTA/py/std0.txt')

scaler1 = StandardScaler()
class1 = scaler1.fit_transform(class1)
Save_mean_and_varaince(scaler1,"1")
mean1 = np.loadtxt('D:/LICENTA/py/medie1.txt')
std1  = np.loadtxt('D:/LICENTA/py/std1.txt')

scaler2 = StandardScaler()
class2 = scaler2.fit_transform(class2)
Save_mean_and_varaince(scaler2,"2")
mean2 = np.loadtxt('D:/LICENTA/py/medie2.txt')
std2  = np.loadtxt('D:/LICENTA/py/std2.txt')

scaler3 = StandardScaler()
class3 = scaler3.fit_transform(class3)
Save_mean_and_varaince(scaler3,"3")
mean3 = np.loadtxt('D:/LICENTA/py/medie3.txt')
std3  = np.loadtxt('D:/LICENTA/py/std3.txt')



# scaler = StandardScaler()
# Features = scaler.fit_transform(Features)
# Save_mean_and_varaince(scaler)
# Scaler2  = scaler.fit(Features)
X_train, X_test, Y_train, Y_test = train_test_split(Features, Labels, test_size=0.1, random_state=42,stratify=Labels)


X_train = np.asarray(X_train).astype('float32')
Y_train = np.asarray(Y_train).astype('float32').reshape((-1,1))
X_test = np.asarray(X_test).astype('float32')
Y_test = np.asarray(Y_test).astype('float32').reshape((-1,1))

checkpoint = tf.keras.callbacks.ModelCheckpoint(denumire, verbose=1, save_best_only=True)
#tensorboard =tf.tensorboard(log_dir='logs/'+datetime.now().strftime('%d-%H%M'))

# log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")

# tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(24,)),
    tf.keras.layers.Dense(128 , activation = 'relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.BatchNormalization(
    axis=-1,
    momentum=0.99,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    moving_mean_initializer="zeros",
    moving_variance_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
),
    tf.keras.layers.Dense(64 , activation = 'relu'),  #folosim relu si 100 de noduri in L2
    tf.keras.layers.BatchNormalization(
    axis=-1,
    momentum=0.99,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    moving_mean_initializer="zeros",
    moving_variance_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
),
    tf.keras.layers.Dense(32 , activation = 'relu'),  #folosim relu si 100 de noduri in L2
    tf.keras.layers.BatchNormalization(
    axis=-1,
    momentum=0.99,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    moving_mean_initializer="zeros",
    moving_variance_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
),
    tf.keras.layers.Dropout(0.7),
    tf.keras.layers.Dense(4 , activation='softmax' ),  #softmax se asigura ca toate nodurile vor avea o suma de probabilitati egala cu 1

    ])

model.compile(optimizer='adam', # algoritmul care foloseste gradient decesnt
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])
Y_train = tf.keras.utils.to_categorical(Y_train,num_classes = 4)
Y_test  = tf.keras.utils.to_categorical(Y_test ,num_classes = 4)
if train == 1:
    model.fit(X_train, Y_train, epochs=300, batch_size=128, validation_data = (X_test, Y_test), callbacks=[checkpoint , tensorboard_callback])


# print(model.summary())
# exec(open('D:/LICENTA/py/Predictie.py').read())

model = tf.keras.models.load_model(denumire)
Data = np.load('D:/LICENTA/Features/Date_test.npy',allow_pickle=True)
Labels = Data[:,0]
Features = Data[:,1:]




# skaler = StandardScaler()
# Features = skaler.fit_transform(Features)
# Save_mean_and_varaince(skaler,'4')
mean = np.loadtxt('D:/LICENTA/py/medie9.txt')
std = np.loadtxt('D:/LICENTA/py/std9.txt')
Features = np.asarray(Features).astype('float32')
# Features = (Features-mean)/std
Features = scaler.fit_transform(Features)
# print(Features1 - Features)

Labels = np.asarray(Labels).astype('float32').reshape((-1,1))
print(model.evaluate(Features, tf.keras.utils.to_categorical(Labels , num_classes=4)))

# Asta este pentru validare
# y_predict = model.predict(X_test)
# y_score = np.argmax(y_predict, axis=1)
# y_testare = np.argmax(Y_test, axis=1)
# rfm = sklearn.metrics.confusion_matrix(y_testare,y_score)

#Asta e pentru testare de date noi
print(model.evaluate(Features, tf.keras.utils.to_categorical(Labels , num_classes=4)))
print(denumire)
y_predict = model.predict(Features)
y_score = np.argmax(y_predict, axis=1)
print(y_score)
rfm = sklearn.metrics.confusion_matrix(Labels,y_score)
print(rfm)

#
# format = 1
# files = os.listdir('D:/LICENTA/Date_test2/')
# files.sort()
# flagF = 0
# for Fisier in files:
#     result = result1 = result2 = result3 = []
#     denumire = 'D:/LICENTA/Date_test2/' + str(Fisier)
#     Label = str(Fisier)[2]
#     if len(str(Fisier)) == 10:
#         Label = str(Fisier)[3]
#     if format == 0:
#         df = pd.read_csv(denumire, sep=";", engine="python", usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
#     else:
#         df = pd.read_csv(denumire, usecols=['Accel_X', 'Accel_Y', 'Gyro_X', 'Gyro_Y'])
#     for epsilon in range(4):
#         flag = 0
#         ferestre = fct.Windower(np.asarray(df.values[:, epsilon]), 200, 160)  # inainte folosisem 200-50
#         for i in ferestre:
#             if epsilon == 0:
#                 AX = []
#                 AX = np.array(
#                     [Label, fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
#                      fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
#                 if flag == 0: result = AX
#                 if flag > 0: result = np.vstack((result, AX))
#             elif epsilon == 1:
#                 AY = []
#                 AY = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
#                                fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
#                 if flag > 0:
#                     result1 = np.vstack((result1, AY))
#                 else:
#                     result1 = AY
#
#             elif epsilon == 2:
#                 GX = []
#                 GX = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
#                                fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
#                 if flag > 0:
#                     result2 = np.vstack((result2, GX))
#                 else:
#                     result2 = GX
#
#             elif epsilon == 3:
#                 GY = []
#                 GY = np.array([fct.MeanAbsolute(i), fct.ZeroFreqRate(i, 0), fct.WaveLength(i), fct.RootMeanSquare(i),
#                                fct.SlopeSignChange(i, 0), fct.Hjorth(i, fct.MeanAbsolute(i))], dtype=object)
#                 if flag > 0:
#                     result3 = np.vstack((result3, GY))
#                 else:
#                     result3 = GY
#             flag += 1
#     # for i in range(len(AX)):
#     #     if i == 7:
#     #         i = i-1
#     #     coloana = np.asarray(result[:,i+1])
#     #     result[:,i+1] = fct.Normalizare(coloana)
#     # for i in range(len(AY)):
#     #     coloana1 = np.asarray(result1[:,i])
#     #     result1[:,i] = fct.Normalizare(coloana1)
#     # for i in range(len(GX)):
#     #     coloana = np.asarray(result2[:,i])
#     #     result2[:,i] = fct.Normalizare(coloana)
#     # for i in range(len(GY)):
#     #     coloana1 = np.asarray(result3[:,i])
#     #     result3[:,i] = fct.Normalizare(coloana1)
#     for i in range(3):
#         if i == 0: denumire = result1
#         if i == 1: denumire = result2
#         if i == 2: denumire = result3
#         result = np.column_stack((result, denumire))
#     if flagF == 0:
#         FINAL = result
#         flagF += 1
#     else:
#         FINAL = np.vstack((FINAL, result))
#     print(FINAL.shape)
# for i in range(24):
#     coloana = np.asarray(FINAL[:, i + 1])
#     FINAL[:, i + 1] = fct.Normalizare(coloana)
#
#
# np.save('D:/LICENTA/Features/Date_test2.npy', np.asarray(FINAL), allow_pickle=True)
# print('Done Date_test2.npy!!')
# Data = np.load('D:/LICENTA/Features/Date_test2.npy',allow_pickle=True)
# Labels = Data[:,0]
# Features = Data[:,1:]
#
#
# Features = np.asarray(Features).astype('float32')
# # Features = (Features-mean)/std
# Features = scaler.transform(Features)
# Labels = np.asarray(Labels).astype('float32').reshape((-1,1))
# # print(model.evaluate(Features, tf.keras.utils.to_categorical(Labels , num_classes=4)))
#
# # Asta este pentru validare
# # y_predict = model.predict(X_test)
# # y_score = np.argmax(y_predict, axis=1)
# # y_testare = np.argmax(Y_test, axis=1)
# # rfm = sklearn.metrics.confusion_matrix(y_testare,y_score)
#
# #Asta e pentru testare de date noi
# # print(model.evaluate(Features, tf.keras.utils.to_categorical(Labels , num_classes=4)))
#
# y_predict = model.predict(Features)
# y_score = np.argmax(y_predict, axis=1)
# # print(y_score)
# rfm = sklearn.metrics.confusion_matrix(Labels,y_score)
# print(rfm)
