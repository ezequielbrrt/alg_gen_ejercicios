
#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as ran
import math 
import struct
import copy
import numpy as np

def convertirBin_Dec(numero):
    f = int(numero, 2)
    return struct.unpack('f', struct.pack('I', f))[0]
def convertirDec_Bin(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = ran.uniform(1,59)
		x = convertirDec_Bin(x)
		arr.append(x)
	return arr


def evaluar_funcion(x1,x2,x3,x4,x5,tipoProblema):
	suma = (0.0)
	x = [x1,x2,x3,x4,x5]
	for i in range(1,25):
		ti = (0.1*(i - 1))
		sen_yi = (2.13*ti)
		cos_yi = ((math.e)**(0.507))* ti
		yi = 1.27**ti* math.tanh((3.012*ti)) + math.sin(sen_yi) * math.cos(cos_yi)
		#print ti
		cos_suma = ti*((math.e)**x5 )
		seno_suma = ((x4*ti))
		tanh_suma = math.tanh((x3*i) + math.sin(seno_suma))
		suma = suma +((x1 * x2**ti *math.tanh(tanh_suma)* math.cos(cos_suma) ) -yi)**2
		#print suma
	#print suma
	return suma * tipoProblema	

#print evaluar_funcion( 1.000000000000000000692698538303,1.000000000000000000252737492323,1.00000000000000000015521144867,1.00000000000000000032817471027,1.0000000003589413166,-1)
#print evaluar_funcion(1.000000000000000000692698538303,1.000000000000000000252737492323,1.0000000000000000000059,1.0000000000000000000059,1.0000000000000000000040,-1)

def checar(x1,x2,x3,x4,x5):
	if (float(x1) > 1 and float(x1) < 60):
		if (float(x2) > 1 and float(x2) < 60):
			if (float(x3) > 1 and float(x3) < 60):
				if (float(x4) > 1 and float(x4) < 60):
					if (float(x5) > 1 and float(x5) < 60):
						return True
					else:
						return False
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
	for i in range(0,len(poblacion),5):
		x1 = convertirBin_Dec(poblacion[i])
		x2 = convertirBin_Dec(poblacion[i+1])
		x3 = convertirBin_Dec(poblacion[i+2])
		x4 = convertirBin_Dec(poblacion[i+3])
		x5 = convertirBin_Dec(poblacion[i+4])
		if checar(x1,x2,x3,x4,x5):
			aux = evaluar_funcion(x1,x2,x3,x4,x5,tipoProblema)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
			aptitud.append(aux)
		else:
			aptitud.append(-1000000000000)
			aptitud.append(-1000000000000)
			aptitud.append(-1000000000000)
			aptitud.append(-1000000000000)
			aptitud.append(-1000000000000)
	return aptitud
