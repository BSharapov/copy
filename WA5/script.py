import mysql.connector as database
#import os

try:
    connection = database.connect(host='0.0.0.0',
                                  database='aliens',
                                  user='root',
                                  port='3366',
                                  password='12345')
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1) 

cur = connection.cursor()
#r = "raw_input"
cur.execute("SELECT alien_id, alien_name, alien_type, alien_color from raw_input")
for row in cur.fetchall():
    print(row)
    
