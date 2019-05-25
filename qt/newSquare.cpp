#include <iostream>
#include <cstdlib>

#include "square.h"

using namespace std;

int main(int argc, char *argv[]){
	if(argc!=2){
		cerr << "Usage: square <number>"<< endl;
		return 1;
	}

	double n = strtod(argv[1], 0);
	cout << "The square of "<<argv[1]<<" is "<< square(n)<<endl;
	return 0;
}


double square(double n){
	return n*n;
}