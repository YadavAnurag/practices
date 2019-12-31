#include <iostream>
int fabonacci(int m){
    if(m <= 1){
        return m;
    }
    else{
        return fabonacci(m-1) + fabonacci(m-2);
    }
}

int main(){
    int n;
    std::cin>>n;
    std::cout<<fabonacci(n);
    return 0;
}