#! /usr/bin/python
# -*- coding: utf-8 -*-


import random  as ran
import struct
from tqdm import tqdm
import numpy as np

def convertirBin_Dec(numero):
    f = int(numero, 2)
    return struct.unpack('f', struct.pack('I', f))[0]
def convertirDec_Bin(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = ran.uniform(-65.536,65.536)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr

a = ([None,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32],
	[None,-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32])

###########Calcular Aptitud########
def evaluar_funcion(x1,x2,tipoProblema):
	suma = 0.0
	for i in range(1,26):
		new = float(1 / i +((x1 - a[0][i])**6)+ ((x2 -a[1][i])**6))
		suma = new + suma
	suma += 0.002
	suma = suma** -1
	return suma * tipoProblema

def checar(x1,x2):
	if (float(x1) > -65.536 and float(x1) < 65.536):
			if (float(x2) > -65.536 and float(x2) < 65.536):
				return True
			else:
				return False
	else:
		return False
def calcular_Aptitud(poblacion,tipoProblema):
	aptitud = []
	for i in range(0,len(poblacion),2):
		x1 = convertirBin_Dec(poblacion[i])
		x2 = convertirBin_Dec(poblacion[i+1])
		if checar(x1,x2):
			aux = evaluar_funcion(x1,x2,tipoProblema)
			aptitud.append(aux)
			aptitud.append(aux)
		else:
			aptitud.append(-100)
			aptitud.append(-100)
	#print len(aptitud)
	#print aptitud
	return aptitud
def calcular_Aptitud2(poblacion,tipoProblema):
	aptitud = []
	n = len(poblacion)/2

##############################