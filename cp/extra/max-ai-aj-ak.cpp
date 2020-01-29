#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    vector<int> prefix(n), suffix(n);
    
    int high = -100;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int i=0; i<n; i++){
        if(a[i]>high){
            high = max(high, a[i]);
            prefix[i] = high;
        }else{
            prefix[i] = high;
        }
    }
    high = -100;
    for(int i=n-1; i>=0; i--){
        if(a[i]>high){
            high = max(high, a[i]);
            suffix[i] = high;
        }else{
            suffix[i] = high;
        }
    }

    high = -100;
    int temp = 0;
    for(int i=1; i<n-1; i++){
        temp = a[i] + (prefix[i-1]*suffix[i+1]);
        high = max(high, temp);
    }

    // for(int i=0; i<n; i++){
    //     cout<<a[i]<<" "<<prefix[i]<<" "<<suffix[i]<<endl;
    // }
    cout<<high;
    return 0;
}