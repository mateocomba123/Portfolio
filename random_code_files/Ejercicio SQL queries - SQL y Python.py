# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:58:16 2020

@author: Mateio
"""

import pandas as pd
import numpy as np

"""DATOS PARA CONECTAR CON MYSQL"""
import sqlalchemy
database_username = 'root'
database_password = 'admin'
database_ip       = 'localhost'
database_name     = 'Ventas2'
cnxn = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
"""
DATOS PARA CONECTAR CON SQL SERVER
import pyodbc
server = 'DESKTOP-QHGSP2P\SQLEXPRESS'
database = 'Ventas2' 
username = 'mateo1' 
password = 'asdasd' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
"""

def Procedimiento(sql):
	df = pd.read_sql(sql,cnxn) #Tomo conexion a la db y la query y creo el DF
	print(df)
	
	#Transformo en array de dos dimensiones para sklearn
	df_X=df[['Año']]
	df_Y=df[['Ventas']]
			
	from sklearn.linear_model import LinearRegression
	# creamos una instancia de LinearRegression
	regresion_lineal = LinearRegression() 
	
	# instruimos a la regresión lineal que aprenda de los datos (x,y)
	regresion_lineal.fit(df_X, df_Y) 
		
	print("\nInserte el año para el cual quiere realizar el pronostico:")
	año = int(input())
	#Limito solo los pronosticos al periodo 2009 - 2012
	while año < 2009 or año > 2012:
		print("Ingrese un año entre 2009 y 2012")
		año = int(input())
	print("Pronostico para el " + str(año) + ": " + str(int(regresion_lineal.predict([[año]]))))
	
	#Parametros del modelo
	choice = 0
	while choice != "s" and choice != "n":
		print("Ingrese 's' para conocer las metricas del modelo o 'n' para ir al menu principal")
		choice = input()
		choice = choice.lower()
	if choice == 's':
		# vemos los parámetros que ha estimado la regresión lineal
		print("La ecuacion de la recta es: ")
		print('y = ' + str(round(float(regresion_lineal.coef_),2)) + "x + " + str(int(regresion_lineal.intercept_)))
		
		# Predecimos los valores y para los datos usados en el entrenamiento
		prediccion_entrenamiento = regresion_lineal.predict(df_X)
		
		from sklearn.metrics import mean_squared_error
		# Calculamos el Error Cuadrático Medio (MSE = Mean Squared Error)
		mse = mean_squared_error(y_true = df_Y, y_pred = prediccion_entrenamiento)
		
		# La raíz cuadrada del MSE es el RMSE
		rmse = np.sqrt(mse)
		
		# calculamos el coeficiente de determinación R2
		r2 = regresion_lineal.score(df_X, df_Y)
		#A102121071
		print('Error Cuadrático Medio (MSE) = ' + str(round(mse,2)))
		print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(round(rmse,2)))
		print('Coeficiente de Determinación R2 = ' + str(round(r2,4)))
		
	else:
		print("Puedes realizar otra consulta en el menu principal")
		

		
def Procedimiento2(sql):
	df = pd.read_sql(sql,cnxn) #Tomo conexion a la db y la query y creo el DF
	
	print("\nVentas por año y por mes:")
	print(df)  #Muestro la consulta original
	
	print("\nInserte el mes para el cual quiere realizar el comparativo vs años anteriores:")
	mes= int(input())
	#Le pido que ingrese un mes valido
	while mes < 1 or mes > 12:
		print("Ingrese un mes valido (en numero)")
		mes = int(input())
		
	df = df[df['Mes'] == mes] #Filtro el dataframe por el mes ingresado
	
	print("\nInformacion de por año. Filtrada por el mes " + str(mes) + " : ")
	print(df)
	#Transformo en array de dos dimensiones para sklearn
	df_X= df[['Año']]
	df_Y= df[['Ventas']]
	
	año = df['Año'].max() + 1  #Obtengo el año siguiente al ultimo que tengo datos
	año = [año]  #Lo convierto en array 2D
	
	from sklearn.linear_model import LinearRegression
	# creamos una instancia de LinearRegression
	regresion_lineal = LinearRegression() 
	
	# instruimos a la regresión lineal que aprenda de los datos (x,y)
	regresion_lineal.fit(df_X, df_Y) 
	
	print("\nPronostico para el " + str(mes) + "/" + str(año[0]) + " es: " + str(int(regresion_lineal.predict([año]))))
	
	#Parametros del modelo
	choice = 0
	while choice != "s" and choice != "n":
		print("\nIngrese 's' para conocer las metricas del modelo o 'n' para ir al menu principal")
		choice = input()
		choice = choice.lower()
	if choice == 's':
		# vemos los parámetros que ha estimado la regresión lineal
		print("\nLa ecuacion de la recta es: \n")
		print('y = ' + str(round(float(regresion_lineal.coef_),2)) + "x + " + str(int(regresion_lineal.intercept_)))
		
		# Predecimos los valores y para los datos usados en el entrenamiento
		prediccion_entrenamiento = regresion_lineal.predict(df_X)
		
		from sklearn.metrics import mean_squared_error
		# Calculamos el Error Cuadrático Medio (MSE = Mean Squared Error)
		mse = mean_squared_error(y_true = df_Y, y_pred = prediccion_entrenamiento)
		
		# La raíz cuadrada del MSE es el RMSE
		rmse = np.sqrt(mse)
		
		# calculamos el coeficiente de determinación R2
		r2 = regresion_lineal.score(df_X, df_Y)
		#A102121071
		print('Error Cuadrático Medio (MSE) = ' + str(round(mse,2)))
		print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(round(rmse,2)))
		print('Coeficiente de Determinación R2 = ' + str(round(r2,4)))
		
	else:
		print("Puedes realizar otra consulta en el menu principal")
		
				
def print_menu():       ## Diseño del menu
    print("\n*****MENU PRINCIPAL****")
    print("1. Total de unidades vendidas de un articulo por año")
    print("2. Total de ventas de un articulo por año ($)")
    print("3. Total de ventas de una sucursal por año ($)")
    print("4. Cantidad de vendedores totales por MES (que hayan realizado ventas)")
    print("5. Total de ventas de una sucursal por MES ($)")
    print("6. Salir del programa")   
  
#Loop en true, muestro menu y pido input, muestro resultados, salvo 6 que finaliza o valores no validos que piden reingreso del dato.
loop=True      

while loop:
	print_menu()
	choice = input("Selecciona una opcion: ")
	if choice == "1":
		print("Ingrese el codigo de articulo. Por ejemplo A102121071:")
		cod = input()
		sql = "select year(vc.fecha) as 'Año',sum(vd.cantidad) as 'Ventas' from vencab as vc inner join vendet as vd on vd.factura = vc.factura and vd.letra = vc.letra where vc.anulada=0 and vd.articulo = '" + cod + "' group by year(vc.fecha) order by 1"
		Procedimiento(sql)
	elif choice =="2":
		print("Ingrese el codigo de articulo. Por ejemplo A102121071:")
		cod = input()
		sql = "select year(vc.fecha) as 'Año',sum(vd.precioventa * vd.cantidad) as 'Ventas' from vencab as vc inner join vendet as vd on vd.factura = vc.factura and vd.letra = vc.letra where vc.anulada=0 and vd.articulo = '" + cod + "' group by year(vc.fecha) order by 1"
		Procedimiento(sql)
	elif choice =="3":
		print("Ingrese el codigo de una sucursal activa. Por ejemplo: 13")
		cod = input()
		sql = "select year(vc.fecha) as 'Año', sum(vd.precioventa * vd.cantidad) as 'Ventas' from vencab as vc inner join vendet as vd on vd.factura = vc.factura and vd.letra = vc.letra inner join sucursales as s on s.sucursal = vc.sucursal where vc.sucursal= " + cod + " and s.Activa = 'S' group by year(vc.fecha) order by 1 asc"
		Procedimiento(sql)
	elif choice =="4":
		print("Presione cualquier tecla para visualizar.")
		cod = input()
		sql = "select year(vc.fecha) as 'Año', month(vc.fecha) as 'Mes', count(distinct(vc.vendedor)) as 'Ventas' from vencab as vc inner join vendet as vd on vd.factura = vc.factura and vd.letra = vc.letra inner join vendedores as v on v.vendedor = vc.vendedor group by year(vc.fecha), month(vc.fecha) order by 1,2"
		Procedimiento2(sql)
	elif choice =="5":
		print("Ingrese el codigo de una sucursal activa. Por ejemplo: 13")
		cod = input()
		sql = "select year(vc.fecha) as 'Año', month(vc.fecha) as 'Mes', sum(vd.precioventa * vd.cantidad) as 'Ventas' from vencab as vc inner join vendet as vd on vd.factura = vc.factura and vd.letra = vc.letra inner join sucursales as s on s.sucursal = vc.sucursal where vc.sucursal = " + cod + " and s.Activa = 'S' group by year(vc.fecha), month(vc.fecha) order by 1,2"
		Procedimiento2(sql)
	elif choice =="6":
		print("Adios!")
		loop = False
	else:
		input("Opcion erronea. Presiona cualquier tecla para continuar...")