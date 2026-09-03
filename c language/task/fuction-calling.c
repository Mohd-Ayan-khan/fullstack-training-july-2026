#include<stdio.h>

int sum()
{
    int num1=30;
    int num2=20;

    printf("\nsum %d",num1+num2);
}

int division()
{
    int num1=30;
    int num2=10;
    printf("\ndivision %d",num1/num2);
}

int multiply()
{
    int num1=30;
    int num2=10;
    printf("\nmultiply %d",num1*num2);
}

int subtract()
{
    int num1=30;
    int num2=10;
    printf("\nsubtration  %d",num1-num2);
}
int main()
{
    printf("therer is a output");
    sum();  
    division();
    subtract();
    multiply();
    

    return 0;
}