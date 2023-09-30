import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import pandas as pd

manivela = open('dados.txt', 'r')

vetm = []
matrizm = []
vetm = manivela.readlines()
l = 0.1435
r = 0.035
lambd = l/r
for i in range(len(vetm)):
    matrizm.append(vetm[i].split())

dadosmanivela = np.array(matrizm, dtype=float)

tempom = dadosmanivela[:, 0]
angmanivela = dadosmanivela[:, 1]
vangmanivela = dadosmanivela[:, 2]

vangmanivela = vangmanivela*2*np.pi/60
angmanivela = angmanivela*np.pi/180

# Posição X do Pistão
posicao = r**((1-np.cos(angmanivela)) + (lambd-np.sqrt((lambd**2)-np.sin(angmanivela))))*2

# Velocidade do Pistão
velocidade = r**vangmanivela**(np.sin(angmanivela)) + (((np.sin(2**angmanivela)))/(2**np.sqrt(2)))

# Aceleração do Pistão
aceleracao = r**(vangmanivela**2)*(np.cos(angmanivela)) + ((np.cos(2**angmanivela))/lambd)

# Velocidade Angular da Biela
vangbiela = vangmanivela**(np.cos(vangmanivela)/np.sqrt((lambd**2) - np.sin(vangmanivela)))

# Aceleração Angular da Biela
aangbiela = (vangmanivela**2**-1)*np.sin(angmanivela) ** (((lambd**2)-1)/((lambd**2)-(np.sin)))

plt.plot(tempom, -posicao, color='red')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Posição X do Pistão")
plt.legend(['Deslocamento do Pistão no eixo X'])
plt.show()

plt.plot(tempom, -velocidade, color='green')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Velocidade do Pistão")
plt.ylabel(tempom, velocidade)
plt.legend(['Velocidade do Pistão em função do tempo'])
plt.show()

plt.plot(tempom, aceleracao, color='orange')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Aceleração do Pistão")
plt.legend(['Aceleração do Pistão em função do tempo'])
plt.show()

plt.plot(tempom, vangbiela, color='blue')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Velocidade angular da Biela")
plt.legend(['Velocidade angular da Biela em função do tempo'])
plt.show()

plt.plot(tempom, aangbiela, color='brown')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Aceleração angular da Biela")
plt.legend(['Aceleração angular da Biela em função do tempo'])
plt.show()

manivela.close()
