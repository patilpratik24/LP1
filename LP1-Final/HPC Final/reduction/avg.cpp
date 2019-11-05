#include<iostream>
#include<omp.h>
#include<stdio.h>
#include<time.h>
using namespace std;
#define n 10

int main()
{
    float arr[n],sum=0;
    #pragma omp parallel for
    for(int i=0;i<n;i++)
    {
        arr[i]=i+1;
    }
    double start_time=omp_get_wtime();
    #pragma omp parallel for reduction(+:sum)
    for(int i=0;i<n;i++)
    {
        sum+=arr[i];
    }

    cout<<"\nAverage:  "<<(sum/n);
    return 0;
}
