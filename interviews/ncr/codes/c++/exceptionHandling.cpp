#include<iostream>
using namespace std;

int main(int argc, char *argv[]){
	try{
		char *mystring;
		mystring = new char[10];

		for(int i=0;i<100; i++){
			if(i>9){
				throw i;
			}
		}
	}
	catch(int n){
		cout<<n;
	}
	catch(char * str){
		cout<<"Exception "<<str<<endl;
	}
}