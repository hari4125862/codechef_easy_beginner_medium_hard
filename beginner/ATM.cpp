#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int withdraw;
    double balance;
    double final_bal;
    cin>>withdraw>>balance;
    
    if(withdraw%5!=0)
	cout<<balance;
    	else if((withdraw+0.5)>balance)
	cout<<balance;    
	else if(withdraw>=0)
    {
        final_bal=balance-withdraw-0.5;
cout<<final_bal;
    }
        
}