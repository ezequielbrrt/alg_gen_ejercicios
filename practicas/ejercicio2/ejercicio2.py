#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as ran
import math 
import struct

def convertirBin_Dec(numero):
    f = int(numero, 2)
    return struct.unpack('f', struct.pack('I', f))[0]
def convertirDec_Bin(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = ran.uniform(-5.12,5.12)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr


def evaluar_funcion(x1,x2,x3,x4,tipoProblema):
	d = 4
	suma = 0.0
	x = [None,x1,x2,x3,x4] 
	for i in range(1,d+1):
		new = (x[i]**2) - (-10 *math.cos(2*math.pi*x[i]))
		suma = suma + new
	suma = suma + (10*d)
	return suma * tipoProblema

def checar(x1,x2,x3,x4):
	if (float(x1) >= -5.12 and float(x1) <= 5.12):
		if (float(x2) >= -5.12 and float(x2) <= 5.12):
			if (float(x3) >= -5.12 and float(x3) <= 5.12):
				if (float(x4) >= -5.12 and float(x4) <= 5.12):
					return True
				else:
					return False
			else:
				return False
		else:
			return False	
	else:
		return False
def calcular_Aptitud(poblacion,tipoProblema):
	aptitud = []
	for i in range(0,len(poblacion),4):
		x1 = convertirBin_Dec(poblacion[i])
		x2 = convertirBin_Dec(poblacion[i+1])
		x3 = convertirBin_Dec(poblacion[i+2])
		x4 = convertirBin_Dec(poblacion[i+3])
		if checar(x1,x2,x3,x4):
			aux  = evaluar_funcion(x1,x2,x3,x4,tipoProblema)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
		else:
			aptitud.append(-100)
			aptitud.append(-100)
			aptitud.append(-100)
			aptitud.append(-100)
	return aptitud

#poblacion = crearPoblacion(12,32)
#print calcular_Aptitud(poblacion,-1)