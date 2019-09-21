#include<stdio.h>


void swapByValue(int a, int b){
	int c;
	c = a;
	a = b;
	b = c;
}
void swapByReference(int* a, int* b){
	int c;
	c = *a;
	*a = *b;
	*b = c;
}
int main(){
	int a = 10, b = 20;
	swapByValue(a,b);
	printf("value %d %d",a,b);
	swapByReference(&a ,&b);
	printf("ref %d %d",a,b);
}