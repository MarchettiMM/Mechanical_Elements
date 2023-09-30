import math
import matplotlib.pyplot as plt

ang = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vsa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rpm = 2500
comprimento = 0.035

for i in range(0, 10, 1):
    ang[i] = ang[i-1] + 36
for i in range(0, 10, 1):
    wab = rpm*((2*math.pi)/60)
    x1 = comprimento * math.cos(math.radians(ang[i]))
    x2 = 0.124 * math.cos(math.radians(ang[i]))
    xt = x1 + x2
    rt = xt / math.sin(math.radians(ang[i]))
    rtt = rt - comprimento
    vsa[i] = (wab * comprimento) * ((rt * 0.3420) / (rt - comprimento))
print("O angulo de entrada é", ang[i], "°C e a velocidade de saída em função da entrada é", " % .4f" % vsa[i],"m/s")
print('\n')
plt.plot(ang, vsa)
plt.title('Velocidade de saída pelo ângulo de entrada')
plt.xlabel('Ângulo de entrada')
plt.ylabel('Velocidade de saída')
plt.show()