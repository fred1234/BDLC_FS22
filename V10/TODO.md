# TODOs

- points in projekt arbeit
- overview of ports and services (nur in slides)





# FAQ

## HDFS

### deleting files is not possible?

```bash
hdfs dfsadmin -safemode leave
```

### change replication factor after file is in HDFS

```bash
hdfs dfs -setrep -R -w 1 /taxi/raw
```

### set replication factor when putting a file

```bash
hdfs dfs -Ddfs.replication=1 -put /path/to/local/file /path/to/hdfs/dir
```

## spark

- SPARK_LOCAL_DIRS, storage directories to use on this node for shuffle and RDD data

```bash
sudo mkdir /data/tmpcluster
sudo chown cluster:root -R /data/tmpcluster
```

- less verbose logging
