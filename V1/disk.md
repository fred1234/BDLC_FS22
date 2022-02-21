# Disk Installation

We need to mount the additional `150GB`-Disk. After you logged in to your machine with `ssh student@bdlc-XX.el.eee.intern`, where `XX` is your personal virtual machine number, execute the following commands. Note, this has to be done once.

## Commands

```bash
# list block devices
lsblk

# you should see the line:
# sdb                         8:16   0  150G  0 disk /data

# format /dev/sdb with ext4
sudo mkfs.ext4 /dev/sdb

# create the directory /data
sudo mkdir /data
```

add the line

```text
/dev/sdb /data ext4 defaults 0 2
```

to the end of the file `/etc/fstab`

```bash
# make the change with your favorite editor (nano/vi)
sudo nano /etc/fstab

# mount everything
sudo mount -a

# check all disks
# you should see the line: /dev/sdb        147G   61M  140G   1% /data
df -h

# reboot your machine
sudo reboot
```
