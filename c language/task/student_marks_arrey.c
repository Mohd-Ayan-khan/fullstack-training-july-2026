#include<stdio.h>
int main()
{
char student[3][20];
int marks[3];


for(int i=0;i<3;i++)
{
    printf("enter student name ");
    scanf("%s",&student[i]);
}
printf("\n*** enter marks ***");
for(int i=0;i<3;i++)
{
    printf("\nenter a marks");
    scanf("%d",&marks[i]);
}

for(int i=0;i<3;i++)
{

   
    
        printf("%s %d\n",student[i],marks[i]);
    
}

    

 
    return 0;
}