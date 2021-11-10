from kafka import KafkaConsumer
import mysql.connector as database
import psycopg2

mysql_connection = database.connect(host='0.0.0.0',
                              database='aliens',
                              user='root',
                              port='3366',
                              password='12345')


# Send data from Kafka to witnesses table in mariadb
cursor_m = mysql_connection.cursor()
consumer = KafkaConsumer('encounters',
                         group_id='db',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:

    cursor_m = mysql_connection.cursor()
    line = message.value.decode('utf-8').split(",")
    cursor_m.execute("INSERT INTO encounters (alien_id, witness_id, location_id, time_of_day) VALUES (%s, %s, %s, %s)", (line[0][1:], line[1], line[2], line[3][:-1]))
    mysql_connection.commit()
   

cursor_m.close()
mysql_connection.close()