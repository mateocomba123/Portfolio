# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:17:12 2021

@author: Mateio
"""

import Scraper1 as gs 
import pandas as pd 

path = 'C:/Users/Mateio/Desktop/ds_project/chromedriver'

df = gs.get_jobs('data scientist',1000, False, path, 5)

df