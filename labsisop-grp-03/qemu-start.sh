#! /bin/bash
sudo qemu-system-i386 --device e1000,netdev=eth0,mac=aa:bb:cc:dd:ee:ff   --netdev tap,id=eth0,script=custom-scripts/qemu-ifup --smp cpus=4 -m 8G --kernel output/images/bzImage --hda output/images/rootfs.ext2 --hdb sdb.bin --nographic --append "console=ttyS0 root=/dev/sda" 
#--device e1000,netdev=eth0,mac=aa:bb:cc:dd:ee:ff   --netdev tap,id=eth0,script=custom-scripts/qemu-ifup