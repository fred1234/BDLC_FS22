
# Setup on all Nodes

## User

We are going to create a new user for the cluster setup. This user will be used for your project work.

As user `student`.

```bash
sudo adduser cluster
```

## Namenode & Datanode Directories

```bash
sudo mkdir -p /data/hdfscluster/namenode
sudo mkdir -p /data/hdfscluster/datanode
```

and give the `cluster` user the access rights to the folders:

```bash
sudo chown cluster:root -R /data/hdfscluster/
```

## Switching the User

Now, we will switch to this user. All following steps should be executed as user `cluster`.

```bash
# switch to the user cluster
su - cluster

# change to the home directory
cd ~

# verify "who you are" with
whoami
```

## Hadoop & Spark

Download Hadoop and Spark, extract it and rename.

```bash
cd ~

echo "Hadoop"
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvzf hadoop-3.3.1.tar.gz
mv hadoop-3.3.1 hadoop

echo "Spark"
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar xvf spark-3.2.1-bin-hadoop3.2.tgz
mv spark-3.2.1-bin-hadoop3.2 spark
```
