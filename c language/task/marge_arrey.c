#include<stdio.h>
int main()
{
int num1[5]={1,3,4,5,3};
int num2[3]={4,3,2};
int new[10],count=0;

for(int i=0;i<5;i++)
{
    new[count]=num1[i];
    count++;

}
for(int i=0;i<3;i++)
{
    new[count]=num2[i];
    count++;
    
}
for(int i=0;i<8;i++)
{
    printf("%d",new[i]);
}


}