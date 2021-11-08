#!/usr/bin/python
import sys, subprocess, os#, psycopg2
from pykafka import KafkaClient

if __name__ == "__main__":
    if len (sys.argv) == 1:
        print ("You need to provide a table name")
        sys.exit (1)   
    else:
        if len (sys.argv) > 2:
            print ("Too many arguments")
            sys.exit (1)
        table_name = sys.argv[1]

f = open("table.txt", "w")
subprocess.run(["psql", "postgresql://postgres:12345@0.0.0.0:5533/aliens", "-tc", "SELECT * FROM {}".format(table_name)], stdout=f)
f.close()
#subprocess.run(["echo", table, "/opt/kafka_2.13-2.8.0/bin/kafka-console-producer.sh --bootstrap-server localhost:9092"])


client = KafkaClient(hosts='localhost:9092')
topic = client.topics[table_name]
#postgres_connection = psycopg2.connect(host='0.0.0.0',
#                               database='aliens',
#                               user='postgres',
#                               port='5533',
#                               password='12345')

#cursor_p = postgres_connection.cursor()
#cursor_p.execute(f"SELECT * FROM {table_name}")
#for line in cursor_p.fetchall():
f = open("table.txt", "r")
for line in f:
    with topic.get_sync_producer() as producer:
        print(line)
        producer.produce(bytes(line, encoding='utf8'))
        
