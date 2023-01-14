import os
from pathlib import Path
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

# Database file directory and name

Path(os.getcwd() + '\\db').mkdir(parents=True, exist_ok=True)
db_file = os.getcwd() + '\\db\\Sofka_Ships.db'

def create_connection(db_file):
    """ Create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_ship(db_file, values):
    """ Insert row into ship table
        db_file str locating database
        
        values tuple (name str, type str, country str, year int, active int, 
        weight int, trust int, fuel str, function str)
    """

    sql_populate_ship = """ INSERT INTO ship (
                                name, 
                                type, 
                                country, 
                                year,
                                active,
                                weight,
                                trust,
                                fuel,
                                function,
                                load_weight, 
                                height,
                                power,
                                speed,
                                capacity, 
                                orbit_height)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """

    conn = create_connection(db_file)

    try:
        c = conn.cursor()
        c.execute(sql_populate_ship, values)
        conn.commit()
    except Error as e:
        print(e)
        messagebox.showwarning('Insert not posible', 
                                f'{values[0]} is already in the DB')
    
    conn.close()

def create_ship_tables(db_file):
    """Create ship, shuttle, ntrip, trip tables in db_file"""
    sql_create_ship_table = """ CREATE TABLE IF NOT EXISTS ship (
                                    name text PRIMARY KEY,
                                    type text,
                                    country text,
                                    year integer,
                                    active text,
                                    weight integer,
                                    trust integer,
                                    fuel text,
                                    function text,
                                    load_weight integer,
                                    height integer,
                                    power integer,
                                    speed integer,
                                    capacity integer,
                                    orbit_height integer
                                ); """

    conn = create_connection(db_file)

    # create tables
    if conn is not None:
        # create ship (parent) table
        create_table(conn, sql_create_ship_table)
        conn.close()

    else:
        print("Error! cannot create the database connection.")

def populate_db():
    create_ship_tables(db_file)
    insert_ship(db_file,('TEST SHIP 1', 'Basic', 'Colombia', 2010, 'Active',
                        3500, 4000, 'Liquid hydrogen and Liquid Oxigen',
                        'Reach for the stars', 0, 0, 0, 0, 0, 0 ))
    insert_ship(db_file,('TEST SHIP 2', 'Basic', 'Colombia', 2010, 'Active',
                        3500, 4000, 'Liquid hydrogen and Liquid Oxigen',
                        'Reach for the stars', 0, 0, 0, 0, 0, 0 ))
    insert_ship(db_file,('TEST SHIP 3', 'Basic', 'Colombia', 2010, 'Active',
                        3500, 4000, 'Liquid hydrogen and Liquid Oxigen',
                        'Reach for the stars', 0, 0, 0, 0, 0, 0))
    insert_ship(db_file,('TEST SHUTTLE 1', 'Shuttle', 'Venezuela', 2000, 
                        'Inactive', 3500, 4000, 'Liquid hydrogen',
                        'Reach for the stars', 150, 135, 780, 0, 0, 0 ))
    insert_ship(db_file,('TEST SHUTTLE 2', 'Shuttle', 'Venezuela', 2000, 
                        'Inactive', 3500, 4000, 'Liquid hydrogen',
                        'Reach for the stars', 150, 135, 780, 0, 0, 0  ))
    insert_ship(db_file,('TEST SHUTTLE 3', 'Shuttle', 'Venezuela', 2000, 
                        'Inactive', 3500, 4000, 'Liquid hydrogen',
                        'Reach for the stars', 150, 135, 780, 0, 0, 0  ))
    insert_ship(db_file,('TEST NOT TRIPULATED 1', 'Not Tripulated',
                        'USA', 1990, 'Inactive', 1500, 2000, 
                        'Solar', 
                        'Reach for the stars', 0, 0, 0, 15000, 0, 0))
    insert_ship(db_file,('TEST NOT TRIPULATED 2', 'Not Tripulated',
                        'USA', 1990, 'Inactive', 1500, 2000, 
                        'Solar', 
                        'Reach for the stars', 0, 0, 0, 15000, 0, 0 ))
    insert_ship(db_file,('TEST NOT TRIPULATED 3', 'Not Tripulated',
                        'USA', 1990, 'Inactive', 1500, 2000, 
                        'Solar', 
                        'Reach for the stars', 0, 0, 0, 15000, 0, 0 ))
    insert_ship(db_file,('TEST TRIPULATED 1', 'Tripulated',
                        'RUSSIA', 2018, 'Active', 1500, 2000, 
                        'Jet Fuel', 
                        'Reach for the stars', 0, 0, 0, 0, 3, 250 ))
    insert_ship(db_file,('TEST TRIPULATED 2', 'Tripulated',
                        'RUSSIA', 2018, 'Active', 1500, 2000, 
                        'Jet Fuel', 
                        'Reach for the stars', 0, 0, 0, 0, 3, 250 ))
    insert_ship(db_file,('TEST TRIPULATED 3', 'Tripulated',
                        'RUSSIA', 2018, 'Active', 1500, 2000, 
                        'Jet Fuel', 
                        'Reach for the stars', 0, 0, 0, 0, 3, 250 ))

def main():
    if os.path.exists(db_file):
        pass
    else:
        populate_db()
    
if __name__ == '__main__':
    main()