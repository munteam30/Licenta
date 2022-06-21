
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import sklearn
from datetime import datetime
from sklearn.datasets import make_classification
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def Printare_matrice(X_train,y_train,X_test, y_test):

    clf = sklearn.svm.SVC(random_state=0)
    clf.fit(X_train, y_train)
    sklearn.svm.SVC(random_state=0)
    sklearn.metrics.plot_confusion_matrix(clf, X_test, y_test)
    plt.show()

def Save_mean_and_varaince(scaler, ID):
    mean = scaler.mean_
    np.savetxt('D:/LICENTA/py/Medie/medie'+ ID+'.txt', mean)

    std = scaler.var_
    np.savetxt('D:/LICENTA/py/Varianta/std'+ ID+'.txt', std)

# Denumire model pentru antrenare("Models/nume.h5"):

denumire = "Models/12s-200-160-2.h5"    #Modelul 12s-200-100 merge ok pentru 550 esantioane
train = 0  # 0- NU  1- DA
Data = np.load('D:/LICENTA/Features/utils.npy',allow_pickle=True)
Labels = Data[:,0]
Features = Data[:,1:]
scaler = StandardScaler()
Features = scaler.fit_transform(Features)
# Save_mean_and_varaince(scaler)

# Scaler2  = scaler.fit(Features)

X_train, X_test, Y_train, Y_test = train_test_split(Features, Labels, test_size=0.1, random_state=42,stratify=Labels)
X_train = np.asarray(X_train).astype('float32')
Y_train = np.asarray(Y_train).astype('float32').reshape((-1,1))
X_test = np.asarray(X_test).astype('float32')
Y_test = np.asarray(Y_test).astype('float32').reshape((-1,1))

checkpoint = tf.keras.callbacks.ModelCheckpoint(denumire, verbose=1, save_best_only=True)
# tensorboard --logdir logs/fit
log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
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
    tf.keras.layers.Dense(64 , activation = 'relu'),  #folosim relu si 64 de noduri in L2
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
    tf.keras.layers.Dense(32 , activation = 'relu'),  #folosim relu si 32 de noduri in L3
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
print(X_train.shape)

if train == 1:
    model.fit(X_train, Y_train, epochs=100, batch_size=128, validation_data = (X_test, Y_test), callbacks=[checkpoint , tensorboard_callback])

# print(model.summary())
model = tf.keras.models.load_model(denumire)
Data = np.load('D:/LICENTA/Features/Date_test.npy',allow_pickle=True)
Labels = Data[:,0]
Features = Data[:,1:]
Features = scaler.fit_transform(Features)
Features = np.asarray(Features).astype('float32')
Labels = np.asarray(Labels).astype('float32').reshape((-1,1))
print(model.evaluate(Features, tf.keras.utils.to_categorical(Labels , num_classes=4)))
# Asta este pentru validare
# y_predict = model.predict(X_test)
# y_score = np.argmax(y_predict, axis=1)
# y_testare = np.argmax(Y_test, axis=1)
# rfm = sklearn.metrics.confusion_matrix(y_testare,y_score)

#Asta e pentru testare de date noi

y_predict = model.predict(Features)
y_score = np.argmax(y_predict, axis=1)
rfm = sklearn.metrics.confusion_matrix(Labels,y_score)
print(rfm)
# Printare_matrice(Features, y_score, Features, Labels)
Miscare = "Error in detecting"
if rfm[0,0] > 4:
    Miscare = "Stationare"
else:
    argument = np.argmax(rfm[0,1:])
    match argument:
        case 0:
            Miscare = "Mers normal"
        case 1:
            Miscare = "Alergare"
        case 2:
            Miscare = "Cadere!"

print(Miscare)

