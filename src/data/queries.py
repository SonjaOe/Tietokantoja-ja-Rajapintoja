import psycopg2
from config import config
import pandas as pd

#Collects all values of table person, this is modified by the fetchall function.
#Or this function collects all columns of table person (marked with # in the end)
def collect_data():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT *FROM person;'
        cursor.execute(SQL)
        # column_names = [desc[0] for desc in cursor.description]#
        # for i in column_names:#
        #     print(i)#
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        (error)
    finally:
        if con is not None:
            con.close()

#Gets the column names and values of the table certificates
def get_columns_values():
    conn = psycopg2.connect(**config())
    results = pd.read_sql("SELECT * FROM certificates", conn)
    print(results)


#Gets all with a specific value (scrum)
def collect_specific():
    con = None
    try:
        con = psycopg2.connect(**config())
        #cursor = con.cursor()
        SQL = "select distinct person.id, person.name, certificates.name AS cert from person, certificates where certificates.person_id = person.id AND certificates.name = 'scrum';"
        results = pd.read_sql(SQL, con)
        print(results)
        #cursor.execute(SQL)
        # column_names = [desc[0] for desc in cursor.description]
        # print(f"{column_names[0]}, {column_names[1]}, {column_names[2]}")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        #cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        (error)
    finally:
        if con is not None:
            con.close()


def insert_line(nimi, person_id):
    sql = 'INSERT INTO certificates (name, person_id) VALUES(%s, %s)'
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**config())
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (nimi, person_id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def update_person(name, id):
    SQL = "update person set name=%s where id = %s"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        cur.execute(SQL, (name, id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return update_person


def delete_part(part_id):
    SQL = "delete from person where person.id = %s"
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the DELETE statement
        cur.execute(SQL, (part_id,))
        #rows_deleted = cur.rowcount
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted


if __name__ == '__main__':
    collect_data()
    #get_columns_values()
    #collect_specific()
    #insert_line('testi', 6)
    #update_person("matti", 2)
    #delete_part(2)