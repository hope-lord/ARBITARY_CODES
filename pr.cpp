#include <iostream>

using namespace std;
void func(int n,int ar1[],int ar2[],int &w,int i){
    bool b=1;
    for(int s=0;s<n;s++){if(ar1[s]!=ar2[i]){b=0;break;}}
    if(b==1){w++;return;}
    else {
        if(ar1[i]<ar2[i]){ar1[i]++;func(n,ar1,ar2,w,i);}
        if(i<n-1) func(n,ar1,ar2,w,i+1);
        else return ;
    }
}
int main()
{
    int n;int ar1[1000];int ar2[1000];
    cout<<"Give the dimension.";
    cin>>n;
    cout<<"Enter the initial coordinate.";
    for(int i=0;i<n;i++){cin>>ar1[i];}
    cout<<"Enter the final coordinate.";
    for(int i=0;i<n;i++){cin>>ar2[i];}
    int a=0;
    //the reccuring functon
    func(n,ar1,ar2,a,0);
    cout<<"The answer is="<<a<<endl;
    return 0;
}