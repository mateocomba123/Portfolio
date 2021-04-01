# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:38:30 2020

@author: Mateio
"""

def consultasql(carrera, intencion, SubIntencion, w5):
	import pandas as pd

	import sqlalchemy
	database_username = 'root'
	database_password = ''
	database_ip       = 'localhost'
	database_name     = 'chatbot'
	cnxn = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))

	query = "select Respuesta from tblrespuestas_1 where carrera = '" + carrera + "' and Intencion = '" + intencion + "' and SubIntencion = '" + SubIntencion + "' and w5 = '" + w5 + "'"
	respuesta = pd.read_sql(query,cnxn) #Tomo conexion a la db y la query y me traigo el valor
	respuesta = respuesta.iloc[0][0]
	return respuesta
"""
carrera = '3D'
intencion = 'pagos'
SubIntencion = 'precio'
w5 = 'que'

consultasql(carrera, intencion, SubIntencion, w5)
"""
