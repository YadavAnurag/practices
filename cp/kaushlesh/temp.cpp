/**
 *   created: 27 January 2019  17:10:26
**/
#include<bits/stdc++.h>
using namespace std;




typedef vector<int> vi;
typedef pair<int , int> pii;
typedef vector< pair<int , int> > vii;
typedef long long ll;
typedef vector<long long> vl;
typedef pair<long long , long long> pll;
typedef vector< pair<long long , long long> > vll;

#define PB push_back
#define PPB pop_back
#define all(c) (c).begin,(c).end()
#define F(i,a,b) for(int i = (int)(a); i <= (int)(b); i++)
#define RF(i,a,b) for(int i = (int)(a); i >= (int)(b); i--)
#define INFLL 2000000000000000007
#define INF 2000000007
#define MOD 1000000007

void optimizeIO()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
}

//                                        //AUTHOR: Kaushalesh Shukla

//=========================================================================================================

int main()
{
	optimizeIO();
	// Set uses balance binary search tree(may be RB or avl tree)
	cout<<"Set"<<endl;
	set<int> s = {1,2,9};
	s.insert(5);
	s.insert(3);
	s.insert(8);
	s.insert(5);
	auto it = s.lower_bound(5);//works same as in vector
	// cout<<s.lower_bound(5)-s.begin()<<endl;//this will not work bcz set doesn't allow jump access
	if(it==s.end())
		it--;
	cout<<*it<<endl;
	//does not allow repetition
	cout<<s.count(5)<<endl;
	cout<<s.count(3)<<endl;
	cout<<s.erase(2)<<endl;//returns 1 if number is present else 0
	cout<<s.count(3)<<endl;
	for(auto x:s)
		cout<<x<<" ";
	cout<<endl;
	for(auto it=s.begin();it!=s.end();it++)
		cout<<*it<<" ";
	cout<<endl;
	//s.find(num) returns iterator of number and returns s.end() if number is not present
	if(s.find(5)!=s.end())
		cout<<"5 Exist in set"<<endl;
	if(s.find(11)==s.end())
		cout<<"11 does not available in set"<<endl;
	// if iterator is passed in erase fn then erase the element and returns next-pointer
	cout<<*s.erase(s.find(3))<<endl;
	cout<<*s.begin()<<endl;
	cout<<"size of set "<<s.size()<<endl;

	//Multiset same as set.. It allows repetition in set
	cout<<"Multiset"<<endl;
	multiset<int> ms = {1,2,2,3,4,5,5,5};
	cout<<ms.count(1)<<" "<<ms.count(2)<<endl;
	ms.erase(5);//deletes all instances
	cout<<ms.count(5)<<endl;
	ms.erase(ms.find(2));
	cout<<ms.count(2)<<endl;


	//Map consist of key-value pair. Uses balanced binary tree. Sort according to key value
	cout<<"Map"<<endl;
	map<string, int> m;
	m["a"] = 0;
	m["z"] = 1;
	m["c"] = 5;
	m.insert({"b",3});
	for(auto it = m.begin(); it!=m.end(); it++)
		cout<<(*it).first<<" "<<it->second<<endl;
	m.erase(m.find("a"));
	cout<<endl;
	for(auto x:m)
		cout<<x.first<<" "<<x.second<<endl;
	cout<<m["z"]<<endl;
	// Note: if a key is requested which is not in map then it will add that key in map with some default value
	cout<<m["k"]<<endl;//will add key 'k' with '0' as default value
	cout<<m.count("k")<<endl;


	//Unordered map uses hashing and takes O(1) accessing time
	cout<<"Unordered Map"<<endl;
	unordered_map<int, int> um;
	um.insert({0,10});
	um.insert({2,20});
	um.insert({1,5});
	um[4]=32;
	cout<<um[4]<<endl;

	// Stack provides access to only top element
	cout<<"Stack"<<endl;
	stack<int> st;
	st.push(3);
	cout<<st.top()<<endl;
	st.pop();
	st.push(3);
	st.push(5);
	st.push(4);
	while(!st.empty()){
		cout<<st.top()<<" ";
		st.pop();
	}
	cout<<endl;

	// Queue adds element at end and pop elements from front(FIFO)
	cout<<"Queue"<<endl;
	queue<int> q;
	q.push(3);
	q.push(5);
	cout<<q.front()<<endl;
	q.pop();

	// Dequeue add and deletes element from both end
	cout<<"Dequeue"<<endl;
	deque<int> dq;
	dq.push_back(3);
	dq.push_back(5);
	dq.push_front(2); // sim pop_back and pop_front
	for(int i =0;i<dq.size();i++)
		cout<<dq[i]<<" ";//allows index wise traversal like vector
	cout<<endl;


	// Priority queue uses heap data structure
	cout<<"Priority Queue"<<endl;
	priority_queue<int> pq;
	pq.push(3);
	pq.push(5);
	pq.push(4);
	pq.push(7);
	cout<<pq.top()<<endl;
	pq.pop();
	cout<<pq.top()<<endl;

	//Heap
	cout<<"Heap"<<endl;
	vector<int> v = {10,30,20,5,50,25};
	//make_heap heapify the values of given range
	make_heap(v.begin(),v.end());
	for(int i=0;i<v.size();i++)
		cout<<v[i]<<" ";
	cout<<endl;
	// pop_heap places the max element at the last index of vector
	pop_heap(v.begin(),v.end());
	for(int i=0;i<v.size();i++)
		cout<<v[i]<<" ";
	cout<<endl;
	v.pop_back();
	v.push_back(50);
	// v.push_back(90);
	// push_heap adjust only last element of array
	push_heap(v.begin(),v.end());
	for(int i=0;i<v.size();i++)
		cout<<v[i]<<" ";
	cout<<endl;

}
