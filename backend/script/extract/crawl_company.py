from vnstock import Listing, Company
import pandas as pd 
import datetime 
import json 
import numpy as np 
import time



def crawl_company():
    start_time = time.perf_counter()     

    list_stock = []
    list_other = []
    list_stock_not_extract = []
    
    date = datetime.date.today().strftime('%y_%m_%d')

    path = '/mnt/d/workshop/vnstock_project/backend/raw/symbol_exchange_data_crawl_26_01_19.json'
    with open(path,'r', encoding='utf-8') as f:
        json_object = json.load(f)
    
    
    count = 0 


    for i in json_object: 
        if count == 30: 
            print(f"--- Đã gửi 30 request. Đang nghỉ 50s để tránh bị chặn... ---")
            count = 0
            time.sleep(50)

        if i.get('type') == 'STOCK':
            symbol = i.get('symbol')
            try:
                company = Company(symbol= symbol, source= 'VCI')
                info_company = company.overview()
                count+=1

                if info_company is None or info_company.empty:
                    print(f"pass ticker {symbol}")
                    continue
                info_dict = info_company.to_dict(orient = 'records')[0]
                info_dict['type'] = i['type']
                list_stock.append(info_dict)
            except Exception as e:
                list_stock_not_extract.append(symbol)
                print(f'ERROR while system is processing: symbol: {symbol}: {e}')

        else: 
            info_company = {
                        'symbol': i.get('symbol'),
                        'name': i.get('organ_name'),
                        'type': i.get('type')
                    }
            list_other.append(info_company)

    path_stock = f'/mnt/d/workshop/vnstock_project/backend/raw/stock_type_data_crawl_{date}.json'
    path_other = f'/mnt/d/workshop/vnstock_project/backend/raw/other_type_data_crawl_{date}.json'
    path_stock_not_extract = f'/mnt/d/workshop/vnstock_project/backend/raw/symbol_not_data_crawl_{date}.json'
    
    with open(path_stock,'w', encoding= 'utf-8') as f:
        json.dump(list_stock,f,ensure_ascii = False,indent = 4)
    
    with open(path_other,'w', encoding= 'utf-8') as f:
        json.dump(list_other,f,ensure_ascii = False,indent = 4)
    
    with open(path_stock_not_extract,'w', encoding= 'utf-8') as f:
        json.dump(list_stock_not_extract,f,ensure_ascii = False,indent = 4)
    
    end_time = time.perf_counter()
    duration = end_time-start_time
    minutes = int(duration // 60)
    seconds = (duration % 60)

    print('Da luu xong')
    print(f"⏱️ Tổng thời gian chạy: {minutes} phút {seconds:.2f} giây")

crawl_company()
