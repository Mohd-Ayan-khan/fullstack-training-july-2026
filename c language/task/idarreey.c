#include<stdio.h>
int main()
{
    int id[10];
    int age;
    char gmail[20];
    char name[10];
    

    printf("\n*********student information********");
    printf("\nenter the name");
    scanf("%s",&name);
    printf("\nenter your age");
    scanf("%d",&age);
    printf("\nenter the gmail");
    scanf("%s",&gmail);
    printf("\nenter the id");
    scanf("%d",&id);

    printf("\n******output*********");
    printf("\nyour name is :%s",name);
    printf("\nyour age is %d",age);
    printf("\nyour gmail is %s",gmail);
    printf("\nyour id is %d",id);
    

}