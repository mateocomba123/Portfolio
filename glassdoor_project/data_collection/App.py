# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:59:19 2021

@author: Mateio
"""
import GlassdoorScraper as gs 
import pandas as pd

path = 'C:/Users/Mateio/Desktop/ds_project/chromedriver'

df = gs.get_jobs('data-scientist', 300, False, path, 5, 10)