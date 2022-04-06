# Big Data Lab Cluster FS22

```text
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
```

This repository is used to provide additional resources for `BDLC_FS22`.

## [V1](./V1/)

- Introduction to the module
- Setup Virtual Machine
- Installation of Apache Hadoop in Standalone Operation

``` bash
.
├── disk.md             # how to add additional disk space
├── install_hadoop.md   # how to install Apache Hadoop in Standalone Operation
└── v1_exercises.md      # exercises for this session
```

## [V2](./V2/)

- HDFS, YARN and MapReduce.
- Run the Hadoop services as daemons (pseudo distributed mode).
- Learn how to navigate in `hdfs` (listing, removing and adding files).
- Write an own word count in python.

``` bash
.
├── python_solution                         # solutions for v2_exercises
│   ├── mapper.py
│   └── reducer.py
├── install_hadoop_pseudo_distributed.md    # how to install Apache Hadoop in Pseudo Distributed Mode
├── install_jupyterlab.md                   # guide for installing JupyterLab
└── v2_exercises.md                         # exercises for this week
```

## [V3](./V3/)

- Setup and Customize `JupyterLab`.
- Setup some dataset.
- Tune our `Hadoop` Cluster.
- Get familiar with `MapReduce` and `MrJob`.

```bash
.
├── resources                           # used during the lesson
├── v3_exercises_material               # exercise material
├── install_mrjob.md                    # guide for installing MRJob 
├── jupyter_lab.md                      # guide for configuring JupyterLab
├── preparing_dataset.md                # some example dataset
├── tuning_yarn.md                      # using all cores and more memory
└── v3_exercises.md                     # exercises for this week
```

## [V4](./V4/)

- Basics of SQL
- SQL to MapReduce
- Hive
- Installation of Hive

```bash
.
├── resources                           # used during the lesson
│   ├── SQL_to_MR                       # Used for SQL basic understanding and writing SQLs in MapReduce.
│   ├── Formatter_JupyterLab.md         # Question about formatters from last week.
│   ├── hive-site.xml                   # Config file for Hive. Will be used when we install Hive. 
│   ├── Testing_Hive.ipynb              # Testing if Hive itself works and if the JupyterLab extensions work with Hive as well.
│   └── Testing_MYSQL.ipynb             # Testing if the metastore has been initialized. Testing SQL Magic for JupyterLab.
├── v4_exercises_material               # Exercises for this week
├── ddl.md                              # Creating databases and tables. Insert data into tables with Hive.
└── install_hive.md                     # Installation guide for Hive.
```

## [V5](./V5/)

- Pandas Workshop created by Stefanie Molin

```bash
.
└── pandas_course.md                # Guide to run and install the workshop.
```

## [V6](./V6/)

- Adding MovieLens 25M dataset to Hive.
- Together: Answering some questions to the MovieLens dataset.
- Parquet Files: how to read, save parquet files.
- Save the MovieLens files as parquet.
- Exercise with "die Post" dataset where we also use partitions.  

```bash
.
├── 1_movie_lens                    # MovieLens 25M dataset
├── 2_parquet                       # Parquet and python
├── 3_movie_lens_parquet            # All notebooks for movielens to parquet
├── v6_exercises_material           # Exercises for this week
```

## [V7](./V7/)

- Intro to Spark.
- Install Spark.
- Testing Spark Context and SQL Context in our Setup.
- Testing Spark in JupyterLab
- Exercises

```bash
.
├── v7_exercises_material                   # Exercises for this week
│   ├── 1_PySpark.ipynb                     # This exercise comes from [pnavaro](https://github.com/pnavaro/big-data)
│   └── 2_Text_Processing.ipynb             # Word Count and Text-Generator
├── 1_spark_context.ipynb                   # Testing Spark Context in Jupyterlab.
├── 2_spark_sql.ipynb                       # Testing Spark-SQL in Jupyterlab.
├── install_spark.md                        # How to install Spark.
```
