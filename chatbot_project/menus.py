# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:40:14 2020

@author: Mateio

"""

def manual_intenciones():
	print("\n*****MENU DE INTENCIONES****")
	print("1. Informacion general una carrera")
	print("2. Planes de estudios")
	print("3. Salida laboral de una carrera")
	print("4. Informacion sobre pagos")
	print("5. Otros tramites")

	choice = int(input("Indique el numero de la opcion: "))
	if choice == 1:
		choice = 'generalidades'
	elif choice == 2:
		choice = 'plan'
	elif choice == 3:
		choice = 'trabajo'
	elif choice == 4:
		choice = 'pagos'
	elif choice == 5:
		choice = 'tramites'

	intencion = choice
	return intencion
	
def manual_tramites():
	print("\n*****OPCIONES DE TRAMITES****")
	print("1. Cursillo introductorio")
	print("2. Equivalencias")
	print("3. Preinscripcion")
	print("4. Requisitos para inscribirme")
	print("5. Otro")
	
	choice = int(input("Indique el numero de la opcion: "))

	if choice == 1:
		choice = 'cies'
	elif choice == 2:
		choice = 'equivalencias'
	elif choice == 3:
		choice = 'preinscripcion'
	elif choice == 4:
		choice = 'requisitos'
	elif choice == 5:
		choice = 'todas'

	SubIntencion = choice
	return SubIntencion
	
def manual_pagos():
	print("\n*****OPCIONES DE PAGOS****")
	print("1. Medios de pago")
	print("2. Aranceles-Precios")

	choice = int(input("Indique el numero de la opcion: "))
	if choice == 1:
		choice = 'medios'
	elif choice == 2:
		choice = 'precio'

	SubIntencion = choice
	return SubIntencion

def manual_carreras():
	print("\n*****MENU DE CARRERAS****")
	print("0. Quiero informacion general")
	print("1. Inteligencia artificial")
	print("2. Diseño de multimedia")
	print("3. Diseño grafico")
	print("4. Publicidad")
	print("5. Relaciones publicas")
	print("6. Higiene y seguridad")
	print("7. Logistica")
	print("8. Recursos humanos")
	print("9. Turismo")
	print("10. Agro negocios")
	print("11. Administracion de empresas")
	print("12. Marketing")
	print("13. Impresiones 3D")
	print("14. Informatica")
	print("15. Robotica")
	print("16. Simulaciones virtuales")
	
	choice = int(input("Indique el numero de la opcion: "))

	if choice == 1:
		choice = 'IA'
	elif choice == 2:
		choice = 'MM'
	elif choice == 3:
		choice = 'DG'
	elif choice == 4:
		choice = 'Pub'
	elif choice == 5:
		choice = 'RRPP'
	elif choice == 6:
		choice = 'HyS'
	elif choice == 7:
		choice = 'Log'
	elif choice == 8:
		choice = 'RRHH'
	elif choice == 9:
		choice = 'TUR'
	elif choice == 10:
		choice = 'Agro'
	elif choice == 11:
		choice = 'ADMIN'
	elif choice == 12:
		choice = 'MKT'
	elif choice == 13:
		choice = '3D'
	elif choice == 14:
		choice = 'INF'
	elif choice == 15:
		choice = 'Rob'
	elif choice == 16:
		choice = 'Svirt'
	elif choice == 0:
		choice = 'todas'

	carrera = choice
	
	return carrera


		

	
		
		
		
		