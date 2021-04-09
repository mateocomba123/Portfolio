# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:59:19 2021

@author: Mateio
"""
import GlassdoorScraper as gs 
import pandas as pd

path = 'C:/Users/Mateio/Desktop/subir/glassdoor_project/data_collection/chromedriver'

#1st: the job name you wanna scrap.
#2nd: how many jobs do you wanna scrap?
#3rd: Verbose
#4th: Chrome driver path
#5th: sleep time, depending on your internet connection. 5 should work fine.
#6th: intents: how many times do you wanna try scrap the same page when something failed before moving to the next one?

df = gs.get_jobs('data-scientist', 300, False, path, 5, 10)