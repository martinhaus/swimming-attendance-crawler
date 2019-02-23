from config import *
import requests
from bs4 import BeautifulSoup
import psycopg2

def save_current_occupancy():
    try:
        connection = psycopg2.connect(user = DBNAME,
                                    password = DBPASSWORD,
                                    host = DBHOST,
                                    port = "5432",
                                    database = DB)
        cursor = connection.cursor()
        sql = "INSERT INTO crawled_data(crawl_dt, attendance) VALUES (NOW(), {});".format(get_current_occupancy())
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while craeting PostgreSQL entry", error)
    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_current_occupancy():
    page = requests.get(website_url)
    soup = BeautifulSoup(page.content, features="lxml")
    return soup.body.find('span', attrs={'class' : 'szp-occupancy'}).text