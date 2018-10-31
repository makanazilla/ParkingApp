from mysql.connector import MySQLConnection, Error

import random

Meter = 0.00001
Seattle_Lat = 47.60621
Seattle_Lng = -122.33207
Host_Name = "localhost"
DB_Name = "parking_spots"
Table_Name = "spots"
DB_User = "root"
User_PW = "password"

#Give random numbers to populate coords
def rnd_offset_coordinates(base_lat, base_lng, radius):

    base_lat = base_lat + (random.randint(-1 * radius, radius) * Meter)
    base_lng = base_lng + (random.randint(-1 * radius, radius) * Meter)
    return base_lat, base_lng


def db_connect():
    """ Connect to MySQL database """

    db_config = {'password': User_PW, 'host': Host_Name, 'user': DB_User, 'database': DB_Name}

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    return conn


def db_close(conn):
    conn.close()
    print('Connection closed.')


def populate_sample_table():

    query = "INSERT INTO spots(id, lat, lng, reserved) VALUES({0}, {1}, {2}, {3})"

    id = 1

    try:
        conn = db_connect()

        cursor = conn.cursor()

        while id <= 100:
            lat, lng = rnd_offset_coordinates(Seattle_Lat, Seattle_Lng, 20000)
            reserved = random.randint(0,1)
            formatted_query = query.format(id, lat, lng, reserved)
            print (formatted_query)
            cursor.execute(formatted_query)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            id += 1

        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


# invoking this file will cause the DB populate function to run

if __name__ == '__main__':
    populate_sample_table()
