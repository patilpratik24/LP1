#include<iostream>
#include<omp.h>
#include<stdio.h>
#include<time.h>
using namespace std;

int main()
{
    double arr[10];
    double min_val=0.0;
    int i;
    for(i=0;i<10;i++)
    {
        arr[i]=2.0+i;
    }
    #pragma omp parallel for reduction(min:min_val)
    for(i=0;i<10;i++)
    {
        if(arr[i]<min_val)
        {
            min_val=arr[i];
        }
    }
    cout<<"\nMax:  "<<min_val;
    return 0;
}
