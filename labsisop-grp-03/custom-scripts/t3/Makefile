
BUILDROOT_DIR := ../..
COMPILER := $(BUILDROOT_DIR)/output/host/bin/i686-buildroot-linux-gnu-gcc

all:

	$(COMPILER) -o cpu_profiler cpu_profiler.c
	cp cpu_profiler $(BUILDROOT_DIR)/output/target/usr/bin
	
	
	
clean:
	rm -f cpu_profiler

