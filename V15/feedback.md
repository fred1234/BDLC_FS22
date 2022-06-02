# Feedback for all

## Cluster Weekend-Blues

- ...

## Collaboration with Jupyterlab and Spark Driver

- ...

## Ist Ihr Projekt ein Big-Data-Problem?

- Kontinuum ...

## pre-processing und prototyping

- lohnt sich
- (pre) Joining von Tabellen kann sich lohnen

## Testen der Services

- Reicht ein `jps` ?

## Schemas

```python
flightData2015 = spark\
  .read\
  .option("inferSchema", "true")\
  .option("header", "true")\
  .csv(f"file:///{path}/Spark-The-Definitive-Guide-master/data/flight-data/csv/2015-summary.csv")
```

## Partitionierung

```python
all_data.repartition(55).write.parquet(f"/taxi/raw_all.parquet")
```

versus

```python
all_data.repartition(col("DEST_COUNTRY_NAME")).write.parquet(f"/taxi/raw_all.parquet")
```

## Spark SQL

```python
df.createOrReplaceTempView("air")
```

```python
spark.sql("SELECT COUNT(FlightNum) FROM air").show()

# +----------------+
# |count(FlightNum)|
# +----------------+
# |       123534969|
# +----------------+
```

```python
%load_ext sparksql_magic #once
```

```python
%%sparksql
SELECT COUNT(FlightNum) FROM air
```

## Markdown Hacks

### Backticks

- use \`test\` to get `test`
- use \``` CODE \``` to get multiple lines of code.

```
print("hello world")
```

- use \```python CODE \``` to get multiple lines of python code.

```python
print("hello world")
```

### Links

This is a link \[click me](www.google.com) and results into:

- [click me](www.google.com)

## Git and Github

Don't push large files. Use `.gitignore` to blacklist files/folders.

- [gitignore templates](https://github.com/github/gitignore)

## Besonders gefreut

### Distinct and Null checks

```python
df_carriers.select('Code').count()
df_carriers.select('Code').distinct().count()
```

### In die Daten Schauen

- Encoding Probleme gefunden.
- Null checks
- New Data over time problem
- Aggregation pitfalls

### Schema and Parquet

> Cooool, da gits d files i parquet, denn müemer eus nöd ums Schema kümmere.

### Pre-Processing with Spark

Erkenntnis, dass Spark auch ein super pre-processing tool ist.
