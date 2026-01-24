import pandas as pd 
import json 
import os 

def check_symbols_icb():

    folder = '/mnt/d/workshop/vnstock_project/backend/raw'
    filename_icb ='crawl_icb_code_company_26_01_21.json'
    filename_com ='symbol_exchange_data_crawl_26_01_19.json'
    
    path_icb = os.path.join(folder, filename_icb)
    path_com = os.path.join(folder,filename_com)

    # open icb json 
    with open(path_icb,'r',encoding= 'utf-8') as file:
        icb_info = json.load(file)

    # open com json 
    with open(path_com, 'r', encoding= 'utf-8') as file:
        com_info = json.load(file)
    count = 0 
    for i in icb_info: 
        for j in com_info: 
            if i.get('symbol') == j.get('symbol'): 
                count +=1
                break
            
    
    size = len(icb_info)
    if count == size : 
        print('data oke ')
    else: 
        print('ERROR')


    

check_symbols_icb()
