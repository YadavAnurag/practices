// #include <cstlib>
#include <iostream>
#include <string>

using namespace std;

double square(double);

int main(int argc, char *argv[]){
	if(argc!=2){
		cerr << "Usage: square <number>";
		return 1;
	}

	// double n = strtod(argv[1], 0);
	double n = stoi(argv[1]);
	cout <<"The square of "<<argv[1]<<" is "<<square(n);
	return 0;

}

double square(double n){
	return n*n;
}