
BUILDROOT_DIR := ../..
COMPILER := $(BUILDROOT_DIR)/output/host/bin/i686-buildroot-linux-gnu-gcc

all:

	$(COMPILER) sched_profiler.c -o sched_profiler
	cp sched_profiler $(BUILDROOT_DIR)/output/target/usr/bin
	
	
	
clean:
	rm -f sched_profiler

