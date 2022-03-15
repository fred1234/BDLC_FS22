```bash
beeline -n hadoop -u jdbc:hive2://localhost:10000
```


```sql
create database if not exists gutenberg;
use gutenberg;




CREATE TABLE IF NOT EXISTS raw_text (
    line STRING
)
ROW FORMAT DELIMITED
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;


EVTL create external table table_name (
  id int,
  myfields string
)
location '/my/location/in/hdfs';

LOAD DATA INPATH '/dataset/gutenberg_all.txt'
OVERWRITE INTO TABLE raw_text;

```


