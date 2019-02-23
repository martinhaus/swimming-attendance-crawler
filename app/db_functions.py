from config import *
import psycopg2

def get_all_entries():
    try:
        connection = psycopg2.connect(user = DBNAME,
                                    password = DBPASSWORD,
                                    host = DBHOST,
                                    port = "5432",
                                    database = DB)
        cursor = connection.cursor()
        sql = "SELECT id, crawl_dt, attendance FROM crawled_data;"
        cursor.execute(sql)
        return cursor.fetchall()
        
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while craeting PostgreSQL entry", error)
    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")