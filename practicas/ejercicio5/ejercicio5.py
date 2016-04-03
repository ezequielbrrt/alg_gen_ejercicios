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
		x = ran.uniform(-500,500)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr


def evaluar_funcion(x1,x2,x3,x4,tipoProblema):
	suma = 0
	d = 4
	x = [None,x1,x2,x3,x4]
	for i  in range(1,d+1):
		absoluto = abs(x[i])
		seno = math.radians(math.sqrt(absoluto))
		suma = suma + (x[i]*math.sin(seno))
	suma = (418.9829 * d) - suma
	return suma * tipoProblema

#print evaluar_funcion(407,264,446,243,-1)

def checar(x1,x2,x3,x4):
	if (float(x1) >= -500 and float(x1) <= 500):
		if (float(x2) >= -500 and float(x2) <= 500):
			if (float(x3) >= -500 and float(x3) <= 500):
				if (float(x4) >= -500 and float(x4) <= 500):
					return True
				else:
					return False
			else:
				return False
		else:
			return False	
	else:
		return False

"""def calcular_Aptitud2(poblacion,tipoProblema):
	aptitud = copy.copy(poblacion)
	for i in range(len(poblacion)):
		x1i = int(ran.uniform(0, len(poblacion) -1))
		x2i = int(ran.uniform(0, len(poblacion) -1))
		x3i = int(ran.uniform(0, len(poblacion) -1))
		x4i = int(ran.uniform(0, len(poblacion) -1))
		x1 = convertirBin_Dec(poblacion[x1i])
		x2 = convertirBin_Dec(poblacion[x2i])
		x3 = convertirBin_Dec(poblacion[x3i])
		x4 = convertirBin_Dec(poblacion[x4i])
		if (float(x1) > -500 and float(x1) < 500):
			
		else:
			aptitud[x1i] = -3000
	return aptitud"""
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
			aptitud.append(-3000)
			aptitud.append(-3000)
			aptitud.append(-3000)
			aptitud.append(-3000)
	return aptitud
#poblacion = crearPoblacion(100,32)
#calcular_Aptitud2(poblacion,-1)