#! /bin/python
# -*- coding: utf-8 -*-

import numpy as  np
import random as rand

def cruza_uniforme(padre,madre):
	t = len(padre)
	hijo1 = ""
	hijo2 = ""
	for i in range(t):
		a = np.random.uniform(1,0)
		if a < 0.5:
			hijo1 = hijo1 + padre[i]
		else:
			hijo1 = hijo1 + madre[i]
		a = np.random.uniform(1,0)
		if a > 0.5:
			hijo2 = hijo2 + padre[i]
		else:
			hijo2 = hijo2 + madre[i]
	return hijo1,hijo2		
	
def cruza_acentuada(padre,madre,d):
	t = len(padre)
	hijo1 = padre
	hijo2 = madre
	hijo1 = list(hijo1)
	hijo2 = list(hijo2)
	for x in range(d):
		p = np.random.random_integers(0,t-1)
		hijo1[p] = madre[p]
		p = np.random.random_integers(0,t-1)
		hijo2[p] = padre[p]
	hijo1 = "".join(hijo1)
	hijo2 = "".join(hijo2)
	return hijo1,hijo2	

def cruza_Un_punto(padre,madre):
	t = len(padre)
	i = int(np.random.randint(t,size=1))
	while i == 0:
		i = int(np.random.randint(t,size=1))
	hijo1 = padre[0:i]
	hijo2 = madre[0:i]
	hijo1 = hijo1 + madre[i:t] 
	hijo2 = hijo2 + padre[i:t]
	return hijo1,hijo2
	
def cruza_Dos_puntos(padre,madre):
	t = len(padre)
	i = int(np.random.randint(t)+1) 
	j = int(np.random.randint(t)+1)
	while i >= j:
		i = int(np.random.randint(t))
		j = int(np.random.randint(t))
	hijo1 = padre[0:i]
	hijo2 = madre[0:i]
	hijo1 = hijo1 + madre[i:j] + padre[j:]
	hijo2 = hijo2 + padre[i:j] + madre[j:]
	return hijo1,hijo2


def cruzaPadres(poblacion,listaPadres,porcentajeCruza):
	#print listaPadres

	#print poblacion
	nuevaPoblacion = []
	for i in range(0,len(poblacion),2):
		porcentaje = rand.random()
		if porcentaje < (float(porcentajeCruza)/100):
			hijo1,hijo2 = cruza_Un_punto(poblacion[listaPadres[i]],poblacion[listaPadres[i+1]])
		else:
			hijo1 = poblacion[listaPadres[i]]
			hijo2 = poblacion[listaPadres[i+1]]
		nuevaPoblacion.append(hijo1)
		nuevaPoblacion.append(hijo2)
	return nuevaPoblacion
