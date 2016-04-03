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
		x = ran.uniform(-100,100)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr


def evaluar_funcion(x1,x2,tipoProblema):
	absoluto = (math.radians((x1**2) - (x2**2)))
	absoluto = abs(absoluto)
	seno = math.sin(absoluto)
	suma = (math.cos(math.radians(seno))**2) - 0.5
	suma = float(suma) / (1+(0.001*((x1**2) + (x2**2))))**2
	suma = suma + 0.5
	return suma * tipoProblema

#print evaluar_funcion(26,41,-1)

def checar(x1,x2):
	if (float(x1) >= -100 and float(x1) <= 100):
			if (float(x2) >= -100 and float(x2) <= 100):
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
	return aptitud
