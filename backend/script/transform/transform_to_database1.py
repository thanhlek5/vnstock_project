import json 
import datetime 
import pandas as pd 
import numpy as np 
import os 
import time 
def get_data(path):
    
    if not os.path.exists(path):
        return None  
    with open(path,'r',encoding='utf-8') as file: 
        json_object = json.load(file) 
    return json_object 

def cleaned_data(data_frame): 
    return data_frame.replace('^\s*%',np.nan,regex = True).drop_duplicates().dropna()

def save_data(folder,filename,dataframe): 
    
    if not os.path.exists(folder): 
        os.makedirs(folder)
    path = os.path.join(folder,filename)
    dataframe.to_json(path,orient = 'records',indent = 4 ,force_ascii = False)
    print('DONE')

def transform_data():
    start_time = time.perf_counter()
    date = datetime.date.today().strftime('%y_%m_%d') 
    info_icb = get_data('/mnt/d/workshop/vnstock_project/backend/raw/indtry_icb_data_crawl_26_01_19.json')
    info_other = get_data('/mnt/d/workshop/vnstock_project/backend/raw/symbol_exchange_data_crawl_26_01_19.json')

    
   
    sectors = [{
            'sector_code': i.get('icb_code'),
            'sector_name': i.get('icb_name')
    } for i in info_icb if i.get('level') == 1 ]

    sectors = cleaned_data(pd.DataFrame(sectors))
    save_data('/mnt/d/workshop/vnstock_project/backend/process',f'transform_sector_{date}.json',sectors)
    print('DONE SECTOR')
    

    exchanges = [{
        'exchange_code': i.get('exchange')
    } for i in info_other] 
    exchanges = cleaned_data(pd.DataFrame(exchanges))
    groups = [{
        'stock_group_code': i.get('product_grp_id')
    } for i in info_other]
    groups = cleaned_data(pd.DataFrame(groups))
    save_data('/mnt/d/workshop/vnstock_project/backend/process',f'transform_exchange_{date}.json',exchanges)
    print('DONE EXCHANGE')
    save_data('/mnt/d/workshop/vnstock_project/backend/process',f'transform_group_{date}.json',groups)
    print('DONE GROUP')
    end_time = time.perf_counter()
    duration = end_time - start_time 
    minutes = int(duration // 60)
    seconds = duration % 60

    print(f"{minutes} minutes {seconds} seconds")

    



  

transform_data()
