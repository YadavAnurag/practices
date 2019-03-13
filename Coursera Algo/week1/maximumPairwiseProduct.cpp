#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int main(){
	int n;
	cin>>n;
	int arr[n];
	for(int i=0; i<n; i++){
		std::cin>>arr[i];
	}
	sort(arr, arr+n);
	ll l = (ll)((ll)(arr[n-1])*arr[n-2]);
	cout<< l;
	return 0;
}


// #include <iostream>
// #include <vector>

// using std::cin;
// using std::cout;
// using std::max;
// using std::vector;

// int MaxPairwiseProductNaive(const vector<int> &numbers){
// 	int product = 0;
// 	int n = numbers.size();
// 	for(int i=0; i<n; i++){
// 		for(int j=i+1; j<n; j++){
// 			product = max(product, numbers[i]*numbers[j]);
// 		}
// 	}
// 	return product;
// }
// int main(){
// 	int n;
// 	cin>>n;
// 	vector<int> numbers(n);
// 	for(int i=0; i<n; i++){
// 		cin>>numbers[i];
// 	}
// 	int product = MaxPairwiseProductNaive(numbers);
// 	cout<<product;
// 	return 0;
// }


// #include<iostream>
// int main(){
// 	int n, max=-1;
// 	std::cin>>n;
// 	int arr[n];
// 	for(int i=0; i<n; i++){
// 		std::cin>>arr[i];
// 	}
// 	int temp;
// 	for(int i=0; i<n; i++){
// 		for(int j=0; j<n; j++){
// 			if(arr[i] != arr[j]){
// 				temp = arr[i]*arr[j];
// 				if(temp>max){
// 					max = temp;
// 				}
// 			}
// 		}
// 	}
// 	std::cout<<max;
// 	return 0;
// }