#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,q; cin>>n>>q;
	string s; cin>>s;

	vector<int> ans(n), ch(26);

	for(int i=0;i<n;i++){
		ans[i] = ch[s[i]-'a'];
		ch[s[i]-'a']++;
	}

	while(q--){
		int x; cin>>x;
		cout<<ans[x-1]<<endl;		
	}
}