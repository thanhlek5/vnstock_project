from vnstock import Listing
import datetime
import pandas as pd 
import os

def crawl_listing():

    date = datetime.date.today().strftime('%y_%m_%d')
    
    folder = '/mnt/d/workshop/vnstock_project/backend/raw'
    filename_se = f'symbol_exchange_data_crawl_{date}.json'
    filename_ind = f'indtry_icb_data_crawl_{date}.json'
    path_se = os.path.join(folder,filename_se)
    path_ind = os.path.join(folder,filename_ind)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
            
    listing = Listing(source = 'VCI')

    df_se =  listing.symbols_by_exchange()
    df_ind = listing.industries_icb()
    df_se.to_json(path_se,orient = 'records',indent = 4, force_ascii = False)
    print(f"Da luu symbol_exchange vao {path_se}")
    df_ind.to_json(path_ind,orient = 'records', indent = 4, force_ascii = False)
    print(f"Da luu industry_icb vao {path_ind}")

crawl_listing()


