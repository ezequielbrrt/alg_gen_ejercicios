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
		x = ran.uniform(-10,10)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr


def evaluar_funcion(x1,x2,tipoProblema):
	suma1 = 0
	suma2 = 0
	for i in range(1,6):
		aux = (i + 1)*x2+i
		suma1 = suma1 + i*(math.cos(math.radians(aux)))
	for j in range(1,6):
		aux2 = (j + 1)*x1+j
		suma2 = suma2 + j*(math.cos(math.radians(aux2)))
	suma = suma1 * suma2
	return suma * tipoProblema

#print evaluar_funcion(26,41,-1)

def checar(x1,x2):
	if (float(x1) >= -10 and float(x1) <= 10):
			if (float(x2) >= -10 and float(x2) <= 10):
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
			aptitud.append(-500)
			aptitud.append(-500)
	return aptitud
