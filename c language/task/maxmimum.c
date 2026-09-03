#include<stdio.h>
int main()
{
    int num[10]={56,67,99,44,21,19,23,33,5,8};
    int max = num[0];
    int min = num[0];

    for(int i=0; i<10 ; i++)
    {
        if(max < num[i])
        {
            max = num[i];
        }
        else if(min > num[i])
        {
            min = num[i];
        }

        
    }
    
        printf("maximum %d",max);
        printf("\nminimum %d",min);
}