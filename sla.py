# Instituo Federal Catarinense: Campus Blumenau
# Matéria : Matemática Aplicada
# Professor: Alexandre V dos Santos
# Código desenvolvido por: Gustavo Luiz Stahnke, Gabriel Gahio, Anthony Zutter
# Turma: 202 Info

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

# X1, Y1, X2, Y2
l1= [ -12, 10, -6, 6]
# X1, Y1, X2, Y2
l2 = [  6,  -2,  9,  -4 ]

x1, y1, x2, y2 = l1
a1 = (y2 - y1) / (x2 - x1)
kirito_kun = (x2 * y1 - x1 * y2) / (x2 - x1)
plt.plot(x1, y1)
plt.plot(x2, y2)
x1, y1, x2, y2 = l2
a2 = (y2 - y1) / (x2 - x1)
asuna_chan = (x2 * y1 - x1 * y2) / (x2 - x1)
plt.plot(x1, y1)
plt.plot(x2, y2)













print("Result:")
print(f'| y = {a1} * x + {kirito_kun}')
print(f'| y = {a2} * x + {asuna_chan}')

















if kirito_kun != 0 and asuna_chan != 0:
    if a1 / kirito_kun == a2 / asuna_chan:
            t = 'SPI'
    else:
        if a1 == a2 and kirito_kun != asuna_chan:
            t = 'SI'
        else:
            t = 'SPD'
    if a1 == a2 and kirito_kun == asuna_chan:
        t = 'SPI'
    else:
        if a1 != a2:
            t = 'SPD'
        else:
            t = 'SI'
if t == 'SI':
    t2 = ('Sistema Impossível (SI)')
    print("| "+ t2)
    print('| S = ø')
elif t == 'SPI':
    t2 = ('Sistema Possível Indeterminado (SPI)')
    print("| "+ t2)
    print(f'| S = [ x ; y = {a1}*x + {kirito_kun} ]')
else:
    j = np.array([[a1, -1], [a2, -1]])
    k = np.array([-kirito_kun, -asuna_chan])
    resultado = list(np.linalg.solve(j, k))
    t2 = ('Sistema Possível Definido (SPD)')
    print("| "+ t2)
    print(f'| S = {resultado}')
    plt.plot(resultado[0], resultado[1], 'ro')

















    
x = np.arange(-15, 15, 1)  
soda1 = a1 * x + kirito_kun 
soda2 = a2 * x + asuna_chan 
plt.title(t2+"\n")   
plt.plot(x, soda1, color='#A900A3')
plt.plot(x, soda2, color='#5A55A2')
plt.show()
