#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:08:35 2026

@author: miranda
"""

import numpy as np
import matplotlib.pyplot as plt

def mi_funcion_sen(vmax, dc, ff, ph, nn, fs):
    ts=1/fs
    tt= np.arange(0,nn)*ts
    xx= dc + vmax*np.sin(2*np.pi*ff*tt + ph)
    
    return tt, xx

#%%
N = 8
fs=1/2 #ancho de banda
tt= np.arange(0,N+1)
xx = 4 + 3*np.sin(tt*np.pi/3)

XX = np.fft.fft(xx)
XXmod = np.abs(XX)
XXfase = np.angle(XX) 

plt.figure(figsize=(11,6))

# xXmod
plt.subplot(2,1,1)
plt.stem(tt, XXmod, linefmt='slateblue', basefmt="royalblue")
plt.title("Modulo")
plt.grid()

# y[n]
plt.subplot(2,1,2)
plt.stem(tt, XXfase, linefmt='slateblue', basefmt="royalblue", label="convolución")

plt.title("Fase")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

#%%
Energia = (1/N**2)*(XXmod)**2

plt.figure()
plt.subplot(2,1,2)
plt.stem(tt, Energia, linefmt='khaki', basefmt="darkkhaki", label="convolución")
plt.title("Energia")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
#Efecto learkage o desparramo espectral 
#Pregunta de parcial: si quiero ver una frecuencia 1/3pi, cuantas muestras necesito? - La cantidad de muestras N tal que 2pi/N=pi/3
