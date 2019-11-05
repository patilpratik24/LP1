#include<iostream>
#include<omp.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    int i,n,sum,a[100],b[100];
    n=100;
    for(i=0;i<n;i++)
    {
        a[i]=rand()%100;
    }
    for(i=0;i<n;i++)
    {
        b[i]=rand()%100;
    }
    sum=0;

    #pragma omp parallel for reduction(+:sum)
    for(i=0;i<n;i++)
    {
        sum=sum+(a[i]*b[i]);
    }
    printf("\nSum: %d",sum);
    return 0;
}

