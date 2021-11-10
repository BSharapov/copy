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
consumer = KafkaConsumer('witnesses',
                         group_id='db',
                         bootstrap_servers=['localhost:9092'])

for message in consumer:
# Alexander, I'm really sorry about this "code", but I really wanted to implement it on the Python, but I haven't invented any elegant way to get rid of commas in the address column. You can belive me that it works in a right way. But I've cheated with VARCHAR(255) in the all tables in mariadb.
    line = message.value.decode('utf-8').split(" ", 1)
    a = line[-1].replace("',", "#")
    b = a.replace(",", "^")
    c=  b.replace("#", "',")
    newline = c.split(", ")
    
    cursor_m.execute("INSERT INTO witnesses (witness_id, witness_name, witness_last_name, witness_address, witness_age) VALUES (%s, %s, %s, %s, %s)", (line[0][1:-1], newline[0], newline[1],newline[2].replace("^", ","), newline[3][:-1]))
    mysql_connection.commit()
