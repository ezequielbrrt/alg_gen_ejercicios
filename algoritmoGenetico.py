#! /usr/bin/python
# -*- coding: utf-8 -*-

import cruza.cruzas as cruza
import mutacion.mutaciones as mutacion
import seleccion.seleccion as seleccion
import practicas.practica1.practica1 as pract1_unos
import practicas.ejercicio1.ejercicio1 as ejercicio1
import practicas.ejercicio2.ejercicio2 as ejercicio2
import practicas.ejercicio3.ejercicio3 as ejercicio3
import practicas.ejercicio4.ejercicio4 as ejercicio4
import practicas.ejercicio5.ejercicio5 as ejercicio5
import practicas.ejercicio6.ejercicio6 as ejercicio6
import practicas.ejercicio7.ejercicio7 as ejercicio7
import practicas.ejercicio8.ejercicio8 as ejercicio8
import random  as ran
import numpy as np
import struct

metodoAptitud = {
	0 : pract1_unos.calcular_Aptitud, 
	1 : ejercicio1.calcular_Aptitud, 
	2 : ejercicio2.calcular_Aptitud,
	3 : ejercicio3.calcular_Aptitud,
	4 : ejercicio4.calcular_Aptitud,
	5 : ejercicio5.calcular_Aptitud,
	6 : ejercicio6.calcular_Aptitud,
	7 : ejercicio7.calcular_Aptitud,
	8 : ejercicio8.calcular_Aptitud,
}
MAX = 1
MIN = - 1
metodoPoblacion = {
	0 : pract1_unos.crearPoblacion, 
	1 : ejercicio1.crearPoblacion,
	2 : ejercicio2.crearPoblacion,
	3 : ejercicio3.crearPoblacion,
	4 : ejercicio4.crearPoblacion,
	5 : ejercicio5.crearPoblacion,
	6 : ejercicio6.crearPoblacion,
	7 : ejercicio7.crearPoblacion,
	8 : ejercicio8.crearPoblacion,
}
#
#Verificar 7,6 y 4
#
#
#
#
#
###############CONFIGURACION INICIAL ##################
NUMERO_PRACTICA = 4
TIPO_PROBLEMA = MIN

TAMANIO_POBLACION =   10000
NUMERO_GENERACIONES = 1000
PORCENTAJE_CRUZA = 60
PORCENTAJE_MUTACION = 93
NUMERO_MEJORES_INDIVIDUOS = 8
TAMANIO_GENOTIPO = 32
######################################################

def convertirBin_Dec(numero):
    f = int(numero, 2)
    f =  struct.unpack('f', struct.pack('I', f))[0]
    return f
def convertirDec_Bin(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


####################Elitismo######################
def getKey(item):
	return item[1]
def ordenar(poblacion, aptitud):
	lista = []
	aux = []
	ordenados = [] 
	for i,(pob,apt) in enumerate(zip(poblacion,aptitud)):
		aux.append(i)
		aux.append(apt)
		aux.append(pob)
		lista.append(aux)
		aux = []
	lista = sorted(lista,key=getKey,reverse=True)
	for x  in range(len(poblacion)):
		ordenados.append(lista[x][2])
	return ordenados
def elitismo(poblacion, mejoresIndividuos,aptitud,numeroMejoresIndividuos):
	if mejoresIndividuos == None:
		ordenados = ordenar(poblacion,aptitud)
		mejoresIndividuos = []
		for i in range(0,numeroMejoresIndividuos):
			mejoresIndividuos.append(ordenados[i])
	else:
		ordenados = ordenar(poblacion,aptitud)
		for x in range(numeroMejoresIndividuos):
			mejoresIndividuos.append(ordenados[x])
		aptitud = metodoAptitud[NUMERO_PRACTICA](mejoresIndividuos,TIPO_PROBLEMA)
		ordenados2 = ordenar(mejoresIndividuos,aptitud)
		mejoresIndividuos = ordenados2[:numeroMejoresIndividuos]
	return mejoresIndividuos
##############################################

############Algoritmo Genetico######################
def algoritmoGeneticoSimple(tamanioPoblacion,numeroGeneraciones,porcentajeCruza,
	porcentajeMutacion, numeroMejoresIndividuos, tamanioGenotipo,mejoresIndividuos):
	generacionActual = 0
	poblacion = metodoPoblacion[NUMERO_PRACTICA](tamanioPoblacion,tamanioGenotipo)
	aptitud = metodoAptitud[NUMERO_PRACTICA](poblacion,TIPO_PROBLEMA)
	mejoresIndividuos = elitismo(poblacion,mejoresIndividuos,aptitud,numeroMejoresIndividuos)
	print "Mejores Individuos Iniciales \n"
	print "Inidivuo                       | Valor Decimal | Aptitud"
	for i,y in zip(mejoresIndividuos,metodoAptitud[NUMERO_PRACTICA](mejoresIndividuos,TIPO_PROBLEMA)) :
		print i, convertirBin_Dec(i), y * TIPO_PROBLEMA
	print 
	listaPadres = seleccion.obtener_lista(poblacion,aptitud) 
	nuevaPoblacion = poblacion
	while generacionActual < numeroGeneraciones:
		nuevaPoblacion = cruza.cruzaPadres(nuevaPoblacion,listaPadres,porcentajeCruza)
		nuevaPoblacion = mutacion.mutacion_uniforme(nuevaPoblacion, porcentajeMutacion)
		aptitud = metodoAptitud[NUMERO_PRACTICA](nuevaPoblacion,TIPO_PROBLEMA)
		mejoresIndividuos = elitismo(nuevaPoblacion,mejoresIndividuos,aptitud,numeroMejoresIndividuos)
		print "Generación "+str(generacionActual + 1) 
		print "Mejores Individuos  \n"
		print "Inidivuo                        | Valor Decimal | Aptitud"
		for i,y in zip(mejoresIndividuos,metodoAptitud[NUMERO_PRACTICA](mejoresIndividuos,TIPO_PROBLEMA)) :
			print i, convertirBin_Dec(i), y * TIPO_PROBLEMA
		print
		listaPadres = seleccion.obtener_lista(nuevaPoblacion,aptitud)
		generacionActual += 1
#####################################################


def main():
	mejoresIndividuos = None
	listaPadres = []
	algoritmoGeneticoSimple(TAMANIO_POBLACION,NUMERO_GENERACIONES,PORCENTAJE_CRUZA,
		PORCENTAJE_MUTACION, NUMERO_MEJORES_INDIVIDUOS,TAMANIO_GENOTIPO,mejoresIndividuos)
 	
main()

#print ejercicio1.evaluar_funcion(-63.3409309387,62.0879707336, -1)
#print ejercicio2.evaluar_funcion(4.75402641296,4.91424512863,-2.96496462822,-4.01688623428,1)




