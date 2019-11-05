#include<iostream>
#include<omp.h>
#include<stdlib.h>
using namespace std;
#define m 4
#define n 3


int main()
{
    int mat[m][n],vec[n],out[m];

    cout<<"Matrix:\n";
    for(int row=0;row<m;row++)
    {
        for(int col=0;col<n;col++)
        {
            mat[row][col]=rand()%5;
        }
    }

    for(int row=0;row<m;row++)
    {
        for(int col=0;col<n;col++)
        {
            cout<<mat[row][col]<<"\t";
        }
        cout<<endl;
    }

    cout<<"\nVector:\n";
    for(int row=0;row<n;row++)
    {
        vec[row]=rand()%5+1;
    }
    for(int row=0;row<n;row++)
    {
        cout<<vec[row]<<endl;
    }

    #pragma omp parallel
    {
        #pragma omp parallel for
        for(int row=0;row<m;row++)
        {
            out[row]=0;
            for(int col=0;col<n;col++)
            {
                out[row]+=mat[row][col]*vec[col];
            }
        }
    }
    cout<<"\n\nResult:\n";
    for(int row=0;row<m;row++)
    {
        cout<<"out["<<row<<"]: "<<out[row]<<endl;
    }

    return 0;
}
