#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>
#define tablesize 502
#define tablesize1 503
struct hash *hashtable=NULL;
struct hash *hashtable1=NULL;
struct node
{
char name[50];
char telnum[15];
struct node *next;
};
struct hash
{
struct node *head;
int pcount;
};
struct node *createnode(char *name, char *telnum)
{
struct node *newnode;
newnode=(struct node *)malloc(sizeof(struct node));

strcpy(newnode->telnum,telnum);
strcpy(newnode->name,name);
newnode->next=NULL;
return newnode;
}
int hf(char *s)
{
int i,sum=0;
for(i=0;s[i]!='\0';i++)
sum=sum+s[i]*(i+1);
return (sum*1/2)%tablesize;
}
int hf1(char *t)
{
int i,sum=0;
for(i=0;t[i]!='\0';i++)
sum=sum+t[i]*(i+2);
return (sum*1/4)%tablesize1;
}
void insert(char *name, char *telnum)
{
int hashindex=hf(name);
struct node *newnode=createnode(name,telnum);
if(!hashtable[hashindex].head)
{
hashtable[hashindex].head=newnode;
return;
}
newnode->next=(hashtable[hashindex].head);
hashtable[hashindex].head=newnode;
return;
}
void insert1(char *name, char *telnum)
{
int hashindex1=hf1(telnum);
struct node *newnode=createnode(name,telnum);
if(!hashtable1[hashindex1].head)
{
hashtable1[hashindex1].head=newnode;
return;
}
newnode->next=(hashtable1[hashindex1].head);
hashtable1[hashindex1].head=newnode;
return;
}


void searchinhash(char *name)
{
int hashindex=hf(name);
struct node *mynode=NULL;
mynode=hashtable[hashindex].head;
if(mynode==NULL)
{
printf("%s",mynode->name);
printf("not found");
getch();
return;
}
while(strcmp(mynode->name,name)!=0)
{
mynode=mynode->next;
if(mynode==NULL)
break;
}
if(mynode!=NULL)
{
printf("name:%s\n",mynode->name);
printf("num:%s",mynode->telnum);
}
else
{
printf("not found");
}
getch();
}
void searchinhash1(char *telnum)
{
int hashindex1=hf1(telnum);
struct node *mynode=NULL;
mynode=hashtable1[hashindex1].head;
if(mynode==NULL)
{
printf("%s",mynode->telnum);
printf("not found");
getch();
return;
}
while(strcmp(mynode->telnum,telnum)!=0)

{
mynode=mynode->next;
if(mynode==NULL)
break;
}
if(mynode!=NULL)
{
printf("name:%s\n",mynode->name);
printf("num:%s",mynode->telnum);
}
else
{
printf("not found");
}
getch();
}
void display(hashtable H)
{
position p;
list l;
int i; int j=0;

for(i=0;i<H->tablesize;i++)
{
l=H->lists[i];
p=l->nextnode;
while(p!=NULL)
{
printf("\n The name and telnum at[%d][%d] is:\t%s \t%s",i,j,p->name,p->telnum);
p=p->nextnode;
j++;
}
}
}
void main()
{
int ch,ch1,ch2;
char name[30],tel[30],search[30],search1[15];
clrscr();
while(1)
{
printf(" TELEPHONE DIRECTORY");
printf("\n____________________");
printf("   \n1. name search  \n 2.number search \n 3.back up the file \n 4.display \n 5. exit \n ");
printf(" enter ur choice");
scanf("%d",&ch);
if(ch==1)
{
printf("\n 1.add \n 2.search by name \n 3.exit");
printf(" \n enter ur choice");
scanf("%d",&ch1);                                                                                                       
switch(ch1)
{
case 1:     printf("enter name");
scanf("%s",name);
printf("enter telephone number");
scanf("%s",tel);
insert(name,tel);
break;
case 2:
 printf("enter name to search");
 scanf("%s",search);
 searchinhash(search);
break;
case 3:exit(0);
}
}
 if(ch==2)
 {
 printf("\n 1.add \n 2.search by ph num \n 3.exit");
 printf("enter ur choice ");
 scanf("%d",&ch2);
 switch(ch2)
{
case 1:     printf("enter name");
scanf("%s",name);
printf("enter telephone number");
scanf("%s",tel);
insert1(name,tel);
break;
case 2:
 printf("enter telephone num to search");
 scanf("%s",search1);
 searchinhash1(search1);
break;
case 3:Take_The_Backup_of_Hashtable(H);
        printf("\n The Backup was sucussesfull");
        break;

case 4:display(H); break;
case 5:exit(0);
}
}
if(ch==5)
exit(0);
}
