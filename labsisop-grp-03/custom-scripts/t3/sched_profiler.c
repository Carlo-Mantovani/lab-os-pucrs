#define _XOPEN_SOURCE 600 // required for barriers to work
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <linux/sched.h>
#include <semaphore.h>

// Buffer
char *buffer;
int bufferSize;
int bufferIndex = 0;

// Thread array
pthread_t *threads;

// Mutex (Semaphore)
pthread_mutex_t thread_lock;

// Barrier
pthread_barrier_t thread_barrier;

// Print buffer
void print_buffer()
{
	for (int i = 0; i < bufferSize; i++) {
		printf("%c", buffer[i]);
	}
}

// Thread task
void *thread_run(void *id)
{
	char tag = (char)id + 0x41; // convert int to char (A, B, C, ...)

	// barrier to sync threads
	pthread_barrier_wait(&thread_barrier);

	// write to buffer until it is full
	while (bufferIndex < bufferSize) {
		pthread_mutex_lock(&thread_lock);
		buffer[bufferIndex] = tag;
		bufferIndex++;
		pthread_mutex_unlock(&thread_lock);
	}

	return NULL;
}

int main(int argc, char **argv)
{
	// check parameters
	if (argc <= 2) {
		printf("Parameters: <Thread Number> <Buffer Size(kb)> \n\n");
		return 0;
	}

	// mutex init
	pthread_mutex_init(&thread_lock, NULL);

	// barrier init with number of threads
	pthread_barrier_init(&thread_barrier, NULL, atoi(argv[1]));

	// buffer init
	bufferSize = atoi(argv[2]) * 1000; // convert mb to bytes
	buffer = (char *)malloc(bufferSize); // allocate buffer memory

	// threads array init
	int nThreads = atoi(argv[1]);
	threads = (pthread_t *)malloc(nThreads * sizeof(pthread_t));

	// create threads
	for (int i = 0; i < nThreads; i++) {
		pthread_create(&threads[i], NULL, thread_run, (void *)i);
	}

	printf("\nThreads created\n");

	printf("Waiting for threads to finish...\n\n");
	for (int i = 0; i < nThreads; i++) {
		pthread_join(threads[i], NULL);
	}

	//print_buffer();

	int *counter = (int *)malloc(nThreads * sizeof(int)); // array to count the number of times each thread was scheduled

	printf("Scheduling order: ");
	for (int i = 0; i < bufferSize; i++) {
		if ((i > 0 && buffer[i] != buffer[i - 1]) || i == 0) { // if the char is different from the previous one
			printf("%c", buffer[i]); // print the char
			counter[(int)buffer[i] - 0x41] += 1; // increment the counter
		}
	}

	printf("\n\nCounter of each thread: \n");
	for (int i = 0; i < nThreads; i++) {
		printf("%c = %d\n", i + 0x41, counter[i]);
	}

	pthread_barrier_destroy(&thread_barrier);
	pthread_mutex_destroy(&thread_lock);

	return 0;
}
