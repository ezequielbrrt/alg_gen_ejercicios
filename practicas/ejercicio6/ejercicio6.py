#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as ran
import math 
import struct
import copy

def convertirBin_Dec(numero):
    f = int(numero, 2)
    return struct.unpack('f', struct.pack('I', f))[0]
def convertirDec_Bin(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = ran.uniform(0,10)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr

C =  ([4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],
	[4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0],
	[4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],
	[4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0])

beta = [1,2,2,4,4,6,3,7,5,5]

def evaluar_funcion(x1,x2,x3,x4,tipoProblema):
	suma =  0
	suma2 = 0
	x = [x1,x2,x3,x4]
	for i  in range(0,10):
		for j in range(0,4):
			suma = suma + ((x[j]-C[j][i])**2 + (beta[i]/10))**-1
	suma = suma  
	return suma * tipoProblema

#print evaluar_funcion(1.59686687341e-19,1.05000330893e-38, 6.53386840146e-29,1.42497047031e-19,-1)

def checar(x1,x2,x3,x4):
	if (float(x1) >= 0 and float(x1) <= 10):
		if (float(x2) >= 0 and float(x2) <= 10):
			if (float(x3) >= 0 and float(x3) <= 10):
				if (float(x4) >= 0 and float(x4) <= 10):
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
			aux = evaluar_funcion(x1,x2,x3,x4,tipoProblema)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
		else:
			aptitud.append(-90000000)
			aptitud.append(-90000000)
			aptitud.append(-90000000)
			aptitud.append(-90000000)
	return aptitud
#poblacion = crearPoblacion(100,32)
#calcular_Aptitud2(poblacion,-1)