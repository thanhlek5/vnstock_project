import psycopg2 
import json 
import datetime
import pandas as pd 
import numpy as np 
import os 
from dotenv import load_dotenv 

load_dotenv()

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

def insert_to_database_1(data,table_name,columns,conflict_columns = None): 

    placeholder = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    
    if not conflict_columns: 
        query = f"""
        INSERT INTO {table_name} ({columns_str})
        VALUES ({placeholder})
        """
    else: 
        conflict_columns_str = ', '.join(conflict_columns)   
        query = f"""
            INSERT INTO {table_name} ({columns_str})
            VALUES ({placeholder})
            ON CONFLICT ({conflict_columns_str}) DO NOTHING 
        """
    conn = psycopg2.connect(
            host = os.getenv('DB_HOST'),
            database = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD')
            )
    cur = conn.cursor()

    for record in data: 
        values = [record[col] for col in columns]
        cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()
    print(f'Insert data into {table_name}')

def load_to_database(): 
    # table exchange 
    insert_to_database_1(get_data_json('/mnt/d/workshop/vnstock_project/backend/process/transform_exchange_26_01_26.json'),
                            'exchanges',
                            ['exchange_code']
                        )
    # table group 
    insert_to_database_1(get_data_json('/mnt/d/workshop/vnstock_project/backend/process/transform_group_26_01_26.json'),
                         'stock_groups',
                         ['stock_group_code']
            )
    # table sector 
    insert_to_database_1(get_data_json('/mnt/d/workshop/vnstock_project/backend/process/transform_sector_26_01_26.json'),
            'sectors',
            ['sector_code','sector_name'],
            ['sector_code','sector_name']
            )
    # table company 
    insert_to_database_1(get_data_json('/mnt/d/workshop/vnstock_project/backend/process/transform_company_26_01_26.json'),
                         'companies',
                         ['company_name','company_profile','company_issue_share','company_charter_capital','company_financial_ratio_issue_share']
            )


load_to_database()







