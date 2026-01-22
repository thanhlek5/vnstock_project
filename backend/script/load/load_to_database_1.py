import psycopg2 
import json 
import datetime
import pandas as pd 
import numpy as np 
import os 
from dotenv import load_dotenv 



def get_data_json(path): 
    """
    lay du lieu tu file json 
    
    :param path: duong dan file 
    :param extension: duoi file 
    """
    if not os.path.exists(path): 
        return None 
    with open(path, 'r', encoding='utf-8') as data: 
        info_object = json.load(data)
    return info_object

def insert_to_database_1(data,table_name,columns,conflict_columns): 

    placeholder = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    conflict_columns_str = ', '.join(conflict_columns)

    query = f"""
        INSERT INTO {table_name} ({columns_str})
        VALUES ({placeholder})
        ON CONFLICT ({conflict_columns_str}) DO NOTHING 
    """
    conn = psycopg2.connect(
            host = os.getenv('DB_HOST'),
            database = os.getenv('DB_NAME'),
            user = os.getenv('Thanhle'),
            password = os.getenv('lepphuocthanh0205')
            )










