#include <stdio.h>
#include <stdlib.h>
#define N 512
// ^ ????

// host is the CPU
// device is the GPU

__global__ void mykernel(void){
	
}

int main(void){
	int *a, *b, *c;
	int *d_a, *d_b, *d_c;
	int size = N * sizeof(int);
	// int size = 512 x 4 = 2048

	cudaMalloc((void **) &d_a, size);
	cudaMalloc((void **) &d_b, size);
	cudaMalloc((void **) &d_c, size);
	a = (int *)malloc(size); random_ints(a, N);
	b = (int *)malloc(size); random_ints(b, N);
	c = (int *)malloc(size);

	cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

	add <<<N,1>>>(d_a, d_b, d_c);

	cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);

	free(a); free(b); free(c);

	cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);

	return 0;
}