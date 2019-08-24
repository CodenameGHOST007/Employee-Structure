import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt 
import sqlite3 as sq

class create_database:
    def connect_database(self):
        self.connection = sq.connect("Employee.db")

        self.crs =self.connection.cursor()
    def create_table(self):
        sql_command="""CREATE TABLE IF NOT EXISTS emp (
        employee_name VARCHAR(30),
        employee_gender char(1),
        employee_post VARCHAR(40)
        );"""

        self.crs.execute(sql_command)
    def __init__() :
        connect_database()
        create_table()
        commit()
        close()
    def commit(self):
        self.connection.commit()
    def close(self):
        self.connection.close()


class fetch_db:
    def __init__(self):
        self.connect_db()
        self.get_points()
        self.close()

    def connect_db(self):
        self.conn=sq.connect("Employee.db")
        self.crs=self.conn.cursor()

    def get_points(self):
        self.crs.execute("SELECT * FROM emp");
        self.x=self.crs.fetchall()
        for i in self.x:
            print(i)
    def close(self):
        self.conn.close()
class add_new_entry:
    conn=sq.connect("Employee.db")
    crs=conn.cursor()
    def add_points(x,y,z,self):
        val=[x,y,z]
        self.crs.execute("INSERT INTO emp (employee_name,employee_gender,employee_post) VALUES (?,?,?)",val)
        self.conn.commit()

