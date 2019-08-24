import sqlite3 as sq
class fetch_db_forgraph:
    def __init__(self):
        connect_db()
        get_points()

    def connect_db(self):
        self.conn=sq.conenct("Employee.db")
        self.crs=conn.cursor()

    def get_points(self):
        self.crs.execute("SELECT * FROM emp");
        self.x=crs.fetchall()
        for i in x:
            print(i)