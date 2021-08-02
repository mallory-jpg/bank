"""Bring it all togetha now!"""

# database, logging
# TEST!!

import queue
import time
import random
import concurrent.futures
import threading
import logging
import psycopg2
import config

from bank_ops import *
from bank_admin import *
from bank_customers import *

def connect():
    conn = None
    try:
        params = config()
        print('Connecting...')
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.close()
    except:
        logging.error('Sorry, could not connect')
    finally:
        if conn is not None:
            conn.close()
            print('Your session has ended')

bank_db = psycopg2.connect(
    host= 'localhost',
    database = 'bank',
    user = 'admin',
    password = '0000'
)

with bank_db as db:
    while __name__ == '__main__':
        # configure logs
        logging.basicConfig(filename='bank.log', filemode='w',
                    format=f'%(asctime)s - %(self.name)s - %(levelname)s - %(message)s')
        # connect to db
        connect()
        # login
