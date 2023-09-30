import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import pandas as pd

print('--------------------Gráficos da Manivela--------------------')
manivela = open('dadosM.txt', 'r')
vetm = []
matrizm = []
vetm = manivela.readlines()
for i in range(len(vetm)):
    matrizm.append(vetm[i].split())

dadosmanivela = np.array(matrizm, dtype=float)
tempom = dadosmanivela[:, 0]
xmanivela = dadosmanivela[:, 1]
ymanivela = dadosmanivela[:, 2]
vmanivela = dadosmanivela[:, 3]
amanivela = dadosmanivela[:, 4]

plt.plot(tempom, xmanivela, color='red')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Posição X da Manivela")
plt.legend(['Deslocamento da Manivela no eixo X'])
plt.show()

plt.plot(tempom, ymanivela, color='blue')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Posição Y da Manivela")
plt.legend(['Deslocamento da Manivela no eixo Y'])
plt.show()

plt.plot(tempom, vmanivela, color='green')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Velocidade da Manivela")
plt.legend(['Velocidade da Manivela em função do tempo'])
plt.show()

plt.plot(tempom, amanivela, color='orange')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Aceleração da Manivela")
plt.legend(['Aceleração da Manivela em função do tempo'])
plt.show()

print('--------------------Gráficos do Pistão--------------------')
pistao = open('/content/dadosP.txt', 'r')
vetp = []
matrizp = []
vetp = pistao.readlines()
for i in range(len(vetp)):
    matrizp.append(vetp[i].split())

dadospistao = np.array(matrizp, dtype=float)
tempop = dadospistao[:, 0]
xpistao = dadospistao[:, 1]
ypistao = dadospistao[:, 2]
vpistao = dadospistao[:, 3]
apistao = dadospistao[:, 4]

plt.plot(tempop, xpistao, color='red')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Posição X do Pistão")
plt.legend(['Deslocamento do Pistão no eixo X'])
plt.show()

plt.plot(tempop, ypistao, color='blue')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Posição Y do Pistão")
plt.legend(['Deslocamento do Pistão no eixo Y'])
plt.show()

plt.plot(tempop, vpistao, color='green')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Velocidade do Pistão")
plt.legend(['Velocidade do Pistão em função do tempo'])
plt.show()

plt.plot(tempop, apistao, color='orange')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Aceleração do Pistão")
plt.legend(['Aceleração do Pistão em função do tempo'])
plt.show()

manivela.close()
pistao.close()
