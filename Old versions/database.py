'''Adding Database functionality'''

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",         # your password
                     db="game1")        # name of the data base

cur = db.cursor()

cur.execute("SELECT * FROM players")

for row in cur.fetchall():
    print (row[0], row[1], row[2], row[3])

db.close()
