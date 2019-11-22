#include<iostream>
#include<math.h>
using namespace std;

int main(int argc, char * argv[]){

	int num, anotherNum, rem,sum=0;
	cin>>num;
	anotherNum = num;
	int len = 0;
	while(anotherNum!=0){
		anotherNum /= 10;
		len++;
	}
	// 153, 370, 371, 407, 1634
	anotherNum = num;
	while(num!=0){
		rem = num%10; 
		sum += pow(rem, len);
		num /= 10;
	}
	cout<<sum<<endl;
	if(sum==anotherNum){
		cout<<"Armstrong number";
	}else{
		cout<<"Not a Armstrong number";
	}


	return 0;
}