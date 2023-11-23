#! /bin/bash
sudo mount output/images/rootfs.ext2 /media/cdrom
sudo cp /media/cdrom/root/trace.dat .
sudo umount /media/cdrom