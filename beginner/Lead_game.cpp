#include <iostream>
using namespace std;

int main() {
	int n,s1=0,s2=0,c1,c2,max1=0,max2=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>c1>>c2;
		s1+=c1;
		s2+=c2;
		if(s1>s2){
			if(s1-s2>max1)
				max1=s1-s2;
		}
		else{
			if(s2-s1>max2)
				max2=s2-s1;
		}
	}
	if(max1>max2)
		cout<<"1 "<<max1;
	else
		cout<<"2 "<<max2;
	return 0;
}