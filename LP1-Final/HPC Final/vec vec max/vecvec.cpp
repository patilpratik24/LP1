#include<iostream>
#include<omp.h>
#include<stdlib.h>
using namespace std;
#define MAX 100

int main()
{
    int a[MAX],b[MAX],c[MAX],i,j,k;

    cout<<"\nFirst Vector:\n";
    #pragma omp parallel for
    for(i=0;i<MAX;i++)
    {
        a[i]=rand()%1000;
    }
    for(i=0;i<MAX;i++)
    {
        cout<<a[i]<<"\t";
    }

    cout<<"\n\nSecond Vector:\n";
    #pragma omp parallel for
    for(j=0;j<MAX;j++)
    {
        b[j]=rand()%1000;
    }
    for(j=0;j<MAX;j++)
    {
        cout<<b[j]<<"\t";
    }

    cout<<"\n\nAddition of two vectors (a,b,c):\n";
    #pragma omp parallel for
    for(k=0;k<MAX;k++)
    {
        c[k]=a[k]+b[k];
    }
    for(k=0;k<MAX;k++)
    {
        cout<<a[k]<<"\t"<<b[k]<<"\t"<<c[k]<<endl;
    }

    return 0;
}
