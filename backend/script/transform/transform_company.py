import pandas as pd 
import datetime 
import json 
import os 
import time 
import numpy as np
def get_data(path): 
    
    if not os.path.exists(path): 
        return None 
    with open(path,'r', encoding= 'utf-8') as file: 
        json_object = json.load(file) 
    return json_object 
def cleaned_data(dataframe): 
    dataframe.replace('\s*%',np.nan,regex = True).drop_duplicates().dropna()
    return dataframe 
def save_data(dataframe,path): 
    dataframe.to_json(path,orient = 'records',indent =4, force_ascii = False)
def transform_company(): 
    company = get_data('/mnt/d/workshop/vnstock_project/backend/raw/stock_type_data_crawl_26_01_21.json')
    company_name = get_data('/mnt/d/workshop/vnstock_project/backend/raw/symbol_exchange_data_crawl_26_01_19.json')   
    
    df_com = pd.DataFrame(company)

    companies = [{
        'company_name': i.get('organ_name'),
        'company_code': i.get('symbol')
    } for i in company_name if i.get('type') == 'STOCK' ]
    companies = cleaned_data(pd.DataFrame(companies))
    
    companies = pd.merge(
            companies,
            df_com[['symbol','id','issue_share','company_profile','financial_ratio_issue_share','charter_capital']]\
                    .rename(columns = {'id': 'company_id', 
                                       'issue_share': 'company_issue_share', 
                                       'company_profile':'company_profile',
                                       'financial_ratio_issue_share':'company_financial_ratio_issue_share',
                                       'charter_capital': 'company_charter_capital'}),
                    left_on = 'company_code',
                    right_on = 'symbol',
                    how ='left'
            )
    companies = companies.drop(columns = ['symbol'])
    date = datetime.date.today().strftime('%y_%m_%d')
    path_save = f'/mnt/d/workshop/vnstock_project/backend/process/transform_company_{date}.json'
    save_data(companies, path_save)

transform_company()
