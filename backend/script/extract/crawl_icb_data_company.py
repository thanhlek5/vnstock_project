import pandas as pd 
from vnstock import Listing 
import datetime 
import json 
import os 
import time  


def crawl_icb(): 

    # set up 
    date = datetime.date.today().strftime('%y_%m_%d')
    listing = Listing(source = "VCI")
    filename = f'crawl_icb_code_company_{date}.json'
    folder = '/mnt/d/workshop/vnstock_project/backend/raw'
    path = os.path.join(folder,filename)

    info_icb = listing.symbols_by_industries()
     
    info_icb.to_json(path,orient = 'records',indent = 4, force_ascii = False)
    
crawl_icb()

