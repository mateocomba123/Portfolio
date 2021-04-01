# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:36:30 2020

@author: AI
"""

def clasificador_intenciones(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    import json
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro = 'cerebros/cerebro_intenciones.sav'
    cerebro = pickle.load(open(cerebro, 'rb'))
    vectorizer = 'cerebros/vectorizador_intenciones.sav'
    vectorizer = pickle.load(open(vectorizer, 'rb'))
	
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizer.transform(oracion_input_array).toarray()
    intencion_pronosticada= cerebro.predict(oracion_vectorizada)
    probabilidad= np.max(cerebro.predict_proba(oracion_vectorizada))
    
    return intencion_pronosticada, probabilidad


'''
resultado, proba=clasificador_intenciones("Quiero saber cuánto cuesta la carrera de IA")

print(resultado, proba)
'''

def clasificador_SubintencionPagos(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro = 'cerebros/cerebro_SubintencionPagos.sav'
    cerebro = pickle.load(open(cerebro, 'rb'))
    vectorizer = 'cerebros/vectorizador_SubintencionPagos.sav'
    vectorizer = pickle.load(open(vectorizer, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizer.transform(oracion_input_array).toarray()
    intencion_pronosticada= cerebro.predict(oracion_vectorizada)
    probabilidad= np.max(cerebro.predict_proba(oracion_vectorizada))
    
    return intencion_pronosticada, probabilidad


'''
resultado, proba=clasificador_SubintencionPagos("Quiero saber cuánto cuesta la carrera de IA")

print(resultado, proba)
'''

def clasificador_SubintencionTramites(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro = 'cerebros/cerebro_SubintencionTramites.sav'
    cerebro = pickle.load(open(cerebro, 'rb'))
    vectorizer = 'cerebros/vectorizador_SubintencionTramites.sav'
    vectorizer = pickle.load(open(vectorizer, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizer.transform(oracion_input_array).toarray()
    intencion_pronosticada= cerebro.predict(oracion_vectorizada)
    probabilidad= np.max(cerebro.predict_proba(oracion_vectorizada))
    
    return intencion_pronosticada, probabilidad


'''
resultado, proba=clasificador_SubintencionTramites("Quiero saber cuánto cuesta la carrera de IA")

print(resultado, proba)
'''

def clasificador_carreras(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro = 'cerebros/cerebro_carreras.sav'
    cerebro = pickle.load(open(cerebro, 'rb'))
    vectorizer = 'cerebros/vectorizador_carreras.sav'
    vectorizer = pickle.load(open(vectorizer, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizer.transform(oracion_input_array).toarray()
    intencion_pronosticada= cerebro.predict(oracion_vectorizada)
    probabilidad= np.max(cerebro.predict_proba(oracion_vectorizada))
    
    return intencion_pronosticada, probabilidad


'''
resultado, proba=clasificador_SubintencionTramites("Quiero saber cuánto cuesta la carrera de IA")

print(resultado, proba)
'''

def clasificador_w5(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro = 'cerebros/cerebro_w5.sav'
    cerebro = pickle.load(open(cerebro, 'rb'))
    vectorizer = 'cerebros/vectorizador_w5.sav'
    vectorizer = pickle.load(open(vectorizer, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizer.transform(oracion_input_array).toarray()
    intencion_pronosticada= cerebro.predict(oracion_vectorizada)
    probabilidad= np.max(cerebro.predict_proba(oracion_vectorizada))
    
    return intencion_pronosticada, probabilidad


'''
resultado, proba=clasificador_SubintencionTramites("Quiero saber cuánto cuesta la carrera de IA")

print(resultado, proba)
'''


