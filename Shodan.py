# -*- coding: utf-8 -*-
"""
Shodan Keyword Search Engine
August 2021
@project manager : Seha Solakoğlu
@author          : Harun Karaman

"""
SHODAN_API_KEY = "RHlEwVP3WRn9sOelFiM5ak5pmL38fiqI"

from pandas import DataFrame as df
import pyexcel_xlsx as excel
import datetime
import os
import time
import shodan

api = shodan.Shodan(SHODAN_API_KEY)

scriptcurrentdirectory = os.path.dirname(os.path.realpath(__file__))

os.chdir(scriptcurrentdirectory)

results = api.search('enerjisa')

# Show the results
print('Results found: {}'.format(results['total']))
for result in results['matches']:
    print('IP: {}'.format(result['ip_str']))
    print(result['data'])
    final_data = df(RESULTS)
    final_data.to_excel("shodan_results.xlsx",sheet_name='RESULTS')
    print('Veriler excel dosyasına aktarıldı.')
    print('')
    

    

