import pandas as pd 
from sqlalchemy import create_engine 
import os 
import json 
import datetime

def get_data(path): 
    if os.path.exists(path): 
        return None 

    with open(path,'r', encoding='utf-8') as file:
        json_object = json.load(file)
    return json_object

def cleaned_data(dataframe): 
    return dataframe.replace(r'^\s*$',np.nan,regex = True).drop_duplicates().dropna()

def save_data(dataframe, dic,filename):
    if os.path.exists(dic): 
        os.makedirs(dic)
    path = os.path.join(dic,filename)
    dataframe.to_json(path,indent = 4, orient = 'records', force_ascii = False)

def transform_group(): 
    icb_info = get_data('/mnt/d/workshop/vnstock_project/backend/raw/indtry_icb_data_crawl_26_01_19.json')
    icb_par = get_data('/mnt/d/workshop/vnstock_project/backend/raw/crawl_icb_code_company_26_01_21.json')
    
    groups = [{
            'group_industry_name': i.get('icb_name2'),
            ''


        }]

