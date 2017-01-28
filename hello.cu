__global__ void mykernal(void){
	
}

int main(void){
	mykernal<<<1,1>>>();
	printf("Hello World!\n");
	return 0;
}
