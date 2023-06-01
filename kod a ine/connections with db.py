
import pymysql as MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="prax")
cur = db.cursor()
cur.execute("select * from a-table")
for row in cur.fetchall():
    print(row[0])
db.close()