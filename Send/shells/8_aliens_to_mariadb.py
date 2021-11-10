from kafka import KafkaConsumer
import mysql.connector as database
import psycopg2

mysql_connection = database.connect(host='0.0.0.0',
                              database='aliens',
                              user='root',
                              port='3366',
                              password='12345')
consumer2 = KafkaConsumer('aliens',
                           group_id='db',
                           bootstrap_servers=['localhost:9092'])
for message2 in consumer2:
    cursor_m = mysql_connection.cursor()
    line2 = message2.value.decode('utf-8').split(",")
    cursor_m.execute("INSERT INTO aliens (alien_id, alien_name, alien_type, alien_color) VALUES (%s, %s, %s, %s)", (line2[0][1:], line2[1], line2[2], line2[3][:-1]))
    mysql_connection.commit()
   

cursor_m.close()
mysql_connection.close()