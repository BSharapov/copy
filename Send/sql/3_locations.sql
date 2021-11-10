CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    place VARCHAR (13),
    country VARCHAR (2),
    region VARCHAR (17)
);