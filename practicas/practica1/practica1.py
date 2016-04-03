#! /usr/bin/python
# -*- coding: utf-8 -*-

from tqdm import tqdm
import random  as ran
import numpy as np


##########poblacion############3
def genotipo(tamanioGenotipo):
	gen = ""
	for i in range(tamanioGenotipo):
		x = ran.randint(0,1)
		gen = gen + str(x)
	return gen
def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = genotipo(tamanioGenotipo)
		arr.append(x)
	return arr
##########################################

###########Calcular Aptitud########
def contarAlelo(individuo,tipoProblema):
	contador = 0
	individuo = str(individuo)
	for i in individuo:
		if i == "1":
			contador += 1
	return contador * tipoProblema
def calcular_Aptitud(poblacion,tipoProblema):
	aptitud = []
	for i in range(len(poblacion)):
		aptitud.append(contarAlelo(poblacion[i],tipoProblema))
	return aptitud
##############################



