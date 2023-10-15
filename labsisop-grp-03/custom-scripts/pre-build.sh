#!/bin/sh

cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
chmod +x $BASE_DIR/target/etc/init.d/S41network-config

cp $BASE_DIR/../custom-scripts/hello/hello.i686 $BASE_DIR/target/usr/bin
chmod +x $BASE_DIR/target/usr/bin/hello.i686

cp $BASE_DIR/../custom-scripts/S50hello $BASE_DIR/target/etc/init.d
chmod +x $BASE_DIR/target/etc/init.d/S50hello

cp $BASE_DIR/../custom-scripts/t1/webserver.py $BASE_DIR/target/usr/bin
chmod +x $BASE_DIR/target/usr/bin/webserver.py

cp $BASE_DIR/../custom-scripts/t1/S51webserver $BASE_DIR/target/etc/init.d
chmod +x $BASE_DIR/target/etc/init.d/S51webserver

# Compile disk-test.c in disk-test dir
BUILDROOT_DIR=$BASE_DIR/..
COMPILER=$BUILDROOT_DIR/output/host/bin/i686-buildroot-linux-gnu-gcc
$COMPILER -o $BUILDROOT_DIR/output/target/usr/bin/disk-test $BUILDROOT_DIR/custom-scripts/disk-test/disk-test.c
chmod +x $BUILDROOT_DIR/output/target/usr/bin/disk-test

#Compile the syscall_test.c
BUILDROOT_DIR=$BASE_DIR/..
COMPILER=$BUILDROOT_DIR/output/host/bin/i686-buildroot-linux-gnu-gcc
$COMPILER -o $BUILDROOT_DIR/output/target/bin/syscall_test $BUILDROOT_DIR/custom-scripts/syscall_test.c

make -C $BASE_DIR/../modules/simple_driver/