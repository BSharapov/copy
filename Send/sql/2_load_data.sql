LOAD DATA INFILE 'data.сsv' INTO TABLE raw_input COLUMNS TERMINATED BY ','OPTIONALLY  ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;