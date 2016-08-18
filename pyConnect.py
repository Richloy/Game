import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",         # your password
                     db="game1")        # name of the data base

class pyConnect:




    def my_connect(self):
        print("I've Connected to PyConnect.py")

    def get_player(self):

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute the SQL query using execute() method.
        cursor.execute ("select * from players where ID = 1")

        # fetch all of the rows from the query
        data = cursor.fetchall()

        for row in data:
            print (row[0], row[1], row[2], row[3])
            return("p"+str(row[2])+".png")
        
