'''  importing neccesity '''

import os
import pandas as pd
import logging 
from sqlalchemy import create_engine,text
import time

''' configuring Logging structure  '''

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filename='logs/Project1.log',
    filemode='w'
)

''' makin engine for creating DB and Ingestion'''

con_string_data_set='mysql+pymysql://root:tanishk@localhost/data_set'
con_string_project1="mysql+pymysql://root:tanishk@localhost/project1"
engine_creating_data_base=create_engine(con_string_data_set)
engine_insgestion=create_engine(con_string_project1)

start=time.time()
def ingestion_db():

    query1='''
    drop database project1;
    create database project1;
    '''
    query2=''' show tables; '''
    
    def query_executer(query,engine):
        with engine.connect() as conn:
            for exe in query.strip().split(';'):
                exe = exe.strip()
                if exe:
                    result = conn.execute(text(exe))
                    try: # try block will execute query select tpye not create type
                        rows=result.fetchall()
                        for row in rows:
                             print(row)
                    except:
                        pass        
                            
    ''' used to create database project1 '''
    query_executer(query1,engine_creating_data_base)
    logging.info('database successfully created')
    
    ''' function to ingest data into Mysql datbase  '''
    
    def ingest_db(df,table,engine):
        df.to_sql(table,con=engine,if_exists='replace',index=False)
        logging.info(f"{table} is ingested")
    
    for files in os.listdir():
        if '.csv' in files:
            df=pd.read_csv(files)
            df.columns = df.columns.str.strip()
            ingest_db(df,files[:-4].lower(),engine_insgestion)#function 1 for ingest
            
    query_executer(query2,engine_insgestion)#function 2 for showing tables in DB
    
if __name__=='__main__':
    ingestion_db()
    end=time.time()
    final_time=(end-start)/60 # to get time in minutes default is seconds
    logging.info(f'ingestion completed in {final_time}')