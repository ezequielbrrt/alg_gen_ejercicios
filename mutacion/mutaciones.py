#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import random

def mutacion_uniforme(poblacion,porcentajeMutacion):
	if porcentajeMutacion == None:
		pass
	else:
		pm = float(porcentajeMutacion)/100
		nuevaPoblacion = []
		for individuo in poblacion:
			ind = list(individuo)
			for i in range(len(ind)):
				r = random.random()
				if r > pm:
					if ind[i] == "0":
						ind[i] = "1" 
					elif ind[i] == "1":
						ind[i] = "0"
			ind = "".join(ind)
			nuevaPoblacion.append(ind)
	return nuevaPoblacion
	