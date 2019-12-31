#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main(){
	int n; cin>>n;
	vector<int> a(n);
	map<int, int> mp;
	for(int i=0;i<n;i++){ 
		cin>>a[i];
		if(mp.find(a[i]) == mp.end())
			mp[a[i]] = 1;
		else
			mp[a[i]]++;
	}
	int mx = 0;
	for(auto i: mp){
		mx = max(mx, i.second);
	}
	cout<<mx;
}