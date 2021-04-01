# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:24:04 2020

@author: AI

PROYECTO: CHATBOT INFORMATIVO
v=0.2
"""

''' importamos los clasificadores y los menus manuales
'''
from clasificadores import clasificador_intenciones
from clasificadores import clasificador_SubintencionPagos
from clasificadores import clasificador_SubintencionTramites
from clasificadores import clasificador_carreras
from clasificadores import clasificador_w5
from menus import manual_carreras
from menus import manual_intenciones
from menus import manual_pagos
from menus import manual_tramites
from procedimientos_sql import consultasql
import numpy as np

import warnings
warnings. filterwarnings('ignore')

while True:
	try:
		# Le pedimos que ingrese su consulta
		oracion_input=input("Hola! Ingrese su consulta: ")


		# CLASIFICADOR DE INTENCIONES: 
		intencion, prob_intencion = clasificador_intenciones(oracion_input)
		intencion = intencion.tolist()[0]

		#Seteo las siguientes variables que van a ir cambiando en los IF
		
		carrera = 'todas'
		w5 = 'todas'
		SubIntencion = 'todas'

			
		if prob_intencion<0.5:
			print("No entendí del todo tu intención, por favor selecciona una del siguiente listado: ")
			manual_intenciones()
			
		if intencion == 'generalidades' or intencion == 'plan' or intencion == 'trabajo':
			# CLASIFICADOR DE CARRERAS:
			carrera, prob_carrera = clasificador_carreras(oracion_input)
			#print(carrera, prob_carrera)
			carrera = carrera.tolist()[0]

			if prob_carrera<0.50:
				print("No comprendi la carrera. Por favor seleccionala: ")
				carrera = manual_carreras()
				
			print("Carrera: " + carrera)
			
		if intencion == 'charla':
			print("Tu intencion es charlar, pero solo soy un chat informativo :(")
		
			
		else:	
			if intencion == 'pagos':
				# CLASIFICADOR DE PAGOS: 
				SubintencionPagos, prob_SubintencionPagos = clasificador_SubintencionPagos(oracion_input)
				#print(SubintencionPagos, prob_SubintencionPagos)			
				SubIntencion = SubintencionPagos.tolist()[0]
				
				if prob_SubintencionPagos<0.5:
					print("Que tipo de consulta sobre pagos quieres realizar? ")
					SubIntencion = manual_pagos()
					#SubIntencion = SubIntencion.tolist()[0]

			if intencion == 'tramites':
				# CLASIFICADOR DE TRAMITES: 
				SubintencionTramites, prob_SubintencionTramites = clasificador_SubintencionTramites(oracion_input)       
				#print(SubintencionTramites, prob_SubintencionTramites)
				SubIntencion = SubintencionTramites.tolist()[0]
				
				if prob_SubintencionTramites<0.5:
					print("Sobre que tramite quieres informacion?: ")
					SubIntencion = manual_tramites()
					#SubIntencion = SubIntencion.tolist()[0]
					
					
			if intencion == 'pagos' or intencion == 'tramites':
				# CLASIFICADOR W5		    
				w5, prob_w5 = clasificador_w5(oracion_input)
				#print(w5, prob_w5)
				w5 = w5.tolist()[0]
			
		
			#La respuesta del chatbot:
			print("----------------------------------------------")
			print("Chatbot dice: ")
			print(consultasql(carrera, intencion, SubIntencion, w5))
			print("----------------------------------------------")
			
		#Vemos que quedo al final para cada cerebro
		print(carrera)
		print(intencion)
		print(SubIntencion)
		print(w5)
			   
		# Después de cada respuesta le preguntamos al usuario si quiere continuar.
        
		desea_continuar=input("Desea continuar? Ingrese s o n: ").lower()
		
		if (desea_continuar=="n"):
            # Nos despedimos
            
			print("----------------------------------------------")
			print("Chatbot dice: ")
			print("Chau, hasta la próxima!")
			print("----------------------------------------------")
            
            # y cortamos el while para terminar 
			break
       
	except (KeyboardInterrupt, EOFError, SystemExit):
		break       