import configparser
import psycopg2
import logging 

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    conn = None
    try:
        print('Connecting...')
        conn = psycopg2.connect(host=config['PostgreSQLdb']['host'],
                                user=config['PostgreSQLdb']['user'],
                                passwd=config['PostgreSQLdb']['pass'],
                                db=config['PostgreSQLdb']['db'])
        cursor = conn.cursor()
        cursor.close()
    except:
        logging.error('Sorry, could not connect')
    finally:
        if conn is not None:
            conn.close()
            print('Your session has ended')
