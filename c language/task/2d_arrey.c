#include<stdio.h>
int main()
{
int matrix[4][5];

printf("enter any number");
for(int i=0; i<4; i++)
{

    for(int x=0; x<5; x++)
    {
        scanf("%d",&matrix[i][x]);
    }
}

for(int i=0; i<4; i++)
{

    for(int x=0; x<5; x++)
    {
        printf(" %d ",matrix[i][x]);
    }
    printf("\n");
}

    return 0;
}