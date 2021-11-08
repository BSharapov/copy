import mysql.connector as database
import psycopg2

mysql_connection = database.connect(host='0.0.0.0',
                              database='aliens',
                              user='root',
                              port='3366',
                              password='12345')

postgres_connection = psycopg2.connect(host='0.0.0.0',
                               database='aliens',
                               user='postgres',
                               port='5533',
                               password='12345')

cursor_m = mysql_connection.cursor()
cursor_p = postgres_connection.cursor()

# Obtaining alien data from raw_input table in mariadb and inserting them to table aliens in postgres;

cursor_m.execute("SELECT DISTINCT alien_id, alien_name, alien_type, alien_color FROM raw_input")
for line in cursor_m.fetchall():
    cursor_p.execute("INSERT INTO aliens (alien_id, alien_name, alien_type, alien_color) VALUES (%s, %s, %s, %s)", (line[0], line[1], line[2], line[3]))
    postgres_connection.commit()

# Obtaining alien location from raw_input table in mariadb and inserting them to table locations in postgres;

cursor_m.execute("SELECT DISTINCT location_id, lat, lon, place, country, region FROM raw_input")
for line in cursor_m.fetchall():
    cursor_p.execute("INSERT INTO locations (location_id, lat, lon, place, country, region) VALUES (%s, %s, %s, %s, %s, %s)", (line[0], line[1], line[2], line[3], line[4], line[5]))
    postgres_connection.commit()
    
# Obtaining witneses from raw_input table in mariadb and inserting them to table witnesses in postgres;

cursor_m.execute("SELECT DISTINCT witness_id, witness_name, witness_last_name, witness_address, witness_age FROM raw_input")
for line in cursor_m.fetchall():
    cursor_p.execute("INSERT INTO witnesses (witness_id, witness_name, witness_last_name, witness_address, witness_age) VALUES (%s, %s, %s, %s, %s)", (line[0], line[1], line[2], line[3], line[4]))
    postgres_connection.commit()

cursor_m.close()
cursor_p.close()
mysql_connection.close()
postgres_connection.close()   
