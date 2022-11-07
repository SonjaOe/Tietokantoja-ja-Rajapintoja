import psycopg2
from config import config
import pandas as pd

#Checks the whole table
def get_columns_values():
    conn = psycopg2.connect(**config())
    results = pd.read_sql("SELECT * FROM astia", conn)
    print(results)

#Adds a line to a table
def insert_line(nimi, lkm):
    sql = 'INSERT INTO Astia (nimi, lkm) VALUES(%s, %s)'
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (nimi, lkm))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id

#Shows only the values of a table
def collect_data():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT * FROM astia;'
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        (error)
    finally:
        if con is not None:
            con.close()


#Executes above functions
if __name__ == '__main__':
    get_columns_values()
    insert_line("Muki", "100kpl")
    insert_line("Lasi", "80kpl")
    insert_line("Iso lautanen", "40kpl")
    insert_line("Pieni lautanen", "40kpl")
    collect_data