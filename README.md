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
