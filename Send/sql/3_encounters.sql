CREATE TABLE encounters ( 
alien_id INT,
witness_id INT, 
location_id INT, 
time_of_day VARCHAR(5),
FOREIGN KEY(alien_id) REFERENCES aliens(alien_id),
FOREIGN KEY(location_id) REFERENCES locations(location_id),
FOREIGN KEY(witness_id) REFERENCES witnesses(witness_id)
);