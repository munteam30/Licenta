import numpy as np
import math

def isNaN(num):
    if float('-inf') < float(num) < float('inf'):
        return num
    else:
        return 0
def Windower(Signal, WindowLength, Overlap):
    Window = []
    matrix = []
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'
    if len(Signal) <= WindowLength:
        return 'Semnalul nu contine suficiente date pentru o fereastra de aceasta dimensiune'
    if WindowLength == 0 or Overlap >= WindowLength:
        return 'Valoare invalida a ferestrei'

    for i in range(0, len(Signal), WindowLength - Overlap):
        Window = Signal[i: i + WindowLength]
        if len(Window) != WindowLength: break
        matrix.append(Window)

    return np.asarray(matrix)

def MeanAbsolute(Signal):
    value = 0
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'

    for i in range(len(Signal)):
        value = value + Signal[i]
    value = value / len(Signal)
    if value < 0: value = value * (-1)
    return value
def ZeroFreqRate(Signal, alfa):
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'
    flag = 0
    zerorate = 0
    for i in range(1, len(Signal) - 1):
        if Signal[i] * Signal[i - 1] < 0:
            modul = Signal[i] - Signal[i - 1]
            if modul < 0: modul = modul * (-1)
            if modul >= alfa: zerorate = zerorate + 1
            flag = 0
        elif Signal[i] * Signal[i - 1] == 0:
            flag = flag + 1  # Conditie suplimentara necesara pentru trecerile prin 0
            if flag % 2 == 0:
                zerorate = zerorate + 1
    return zerorate
def WaveLength(Signal):
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'
    WL = 0
    suma = 0
    for i in range(1, len(Signal)):

        suma = Signal[i] - Signal[i - 1]
        if suma < 0: suma = suma * (-1)
        WL = WL + suma
    return WL
def RootMeanSquare(Signal):
    value = 0
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'

    for i in range(len(Signal)):
        value = value + Signal[i] ** 2
    value = value / len(Signal)
    RMS = math.sqrt(value)
    return RMS
def SlopeSignChange(Signal, alfa):
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'
    if alfa < 0:
        return 'Factorul de control al zgomotului trebuie sa fie >=0'

    SSC = 0
    for i in range(1, len(Signal) - 1):
        temp = (Signal[i] - Signal[i - 1]) * (Signal[i] - Signal[i + 1])
        if temp > alfa:
            SSC = SSC + 1

    return SSC
def Hjorth(Signal, media):
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'

    param = 0
    for i in Signal:
        param = param + (i - media) ** 2
    param = param / len(Signal)
    return param

def Skewness(Signal):
    suma = 0
    for i in Signal:
        suma = suma + ((i - np.mean(Signal)) / (np.std(Signal) + np.spacing(1))) ** 3
        suma = isNaN(suma)

    param = suma / len(Signal)
    return param

def Varianta(Signal, MediaLaPatrat):  # asta nu trebuie facuta ca si coloana
    if len(Signal) == 0:
        return 'Semnalul nu contine nicio data'
    Sigma = 0
    media = 0
    for i in Signal:
        media = media + i ** 2
    media = media / len(Signal)
    Sigma = media - MediaLaPatrat
    return Sigma
def Normalizare(Signal):
    Maximul = np.amax(Signal)
    Value = []
    for i in range(len(Signal)):
        if Signal[i] == np.amin(Signal):
            Value.append(0)
        else:
            Value.append((Signal[i] - np.amin(Signal)) / (Maximul - np.amin(Signal)))
    return np.asarray(Value)
def Standardizare(Signal):
    value = []
    for i in Signal:
        value.append(1 / (math.sqrt(2 * math.pi)) * math.exp(-(i ** 2 / 2)))

    return np.asarray(value)

