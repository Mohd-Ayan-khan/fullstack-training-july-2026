#include<stdio.h>
int main()
{
int marks[5];
char subject1[10],subject2[10],subject3[10],subject4[10],subject5[10];
float total=0;



printf("enter your  subject");
scanf("%s",&subject1);
printf("enter your  subject");
scanf("%s",&subject2);
printf("enter your  subject");
scanf("%s",&subject3);
printf("enter your  subject");
scanf("%s",&subject4);
printf("enter your  subject");
scanf("%s",&subject5);

printf("\n enter your subject number\n");
for(int i=0;i<5;i++)
{
    
    scanf("%d",&marks[i]);
    total += marks[i];
    
}


printf("*********report card***********");
printf("\n%d",total);
printf("\n%.2f",total/5);

























    
}
