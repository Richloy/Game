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
        cursor.execute ("SELECT * FROM players WHERE ID = 1")

        # fetch all of the rows from the query
        data = cursor.fetchall()

        for row in data:
            print (row[0], row[1], row[2], row[3])
            return("p"+str(row[2])+".png")
        
    def get_login(self, name):

        print(name)
        command = "SELECT * FROM login WHERE player_name = \'"+name+"\'"
        print(command)
        cursor = db.cursor()
        cursor.execute (command)
        data = cursor.fetchall()
        return data

    def check_new_username(self, name):

        print(name)
        command = "SELECT COUNT(*) FROM login WHERE player_name = \'"+name+"\'"
        print(command)
        cursor = db.cursor()
        cursor.execute (command)
        data = cursor.fetchall()
        print(data)
        
        if data[0][0] == 0:
            print("Not found")
            return False
        else:
            return True
