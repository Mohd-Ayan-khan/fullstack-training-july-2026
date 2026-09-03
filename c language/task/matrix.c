#include<stdio.h>
int main()
{
    int matrix[3][3]={{1,2,3},{4,5,6},{7,8,9}};

    for(int i=0; i<3; i++)
    {

        for(int x=0; x<3; x++)
        {

            printf(" %d ",matrix[i][x]);
        }
        printf("\n");

    }

}