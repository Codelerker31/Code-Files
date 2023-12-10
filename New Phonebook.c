#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAX 1000


typedef struct phonebook {
    char phoneNumber[20];
    char code[10];
    char name[50];
    char address[100];
    char status[10];
    struct phonebook *next;
} Phonebook;
 
Phonebook* hashTable[MAX];

void createList() {
    char line[200];
    FILE *fp = fopen("phonebook.txt", "r");
    while (fgets(line, 200, fp)) {
        Phonebook *temp = (Phonebook*)malloc(sizeof(Phonebook));
        sscanf(line, " %200[^|]| %49[^|]| %99[^|]| %9s",
            temp->phoneNumber, temp->name, temp->address, temp->status);
        temp->next = NULL;
 
        //This code is used to extract the code from a phone number string. The code takes a pointer to a phone number string and stores the code in the 'code' field of a structure. The strchr() function is used to search for the 'x' character in the phone number string, and if it is found, the code is then extracted by using strncat() to concatenate the code to the 'code' field in the structure. If the 'x' character is preceded by a space character then the space is removed before the code is extracted.
        temp->code[0] = '\0';
        char *p = strchr(temp->phoneNumber, 'x');        
        if (p) {
            strncat(temp->code, p, 9);
            if (p[-1] == ' ') --p;
            *p = '\0';
        }
        
        int hash_value = abs(atoi(temp->phoneNumber)) % MAX;
        if(hashTable[hash_value] == NULL) {      //if the hash value is null we store the number in temp variable
            hashTable[hash_value] = temp;
        }
        else {
            Phonebook *head = hashTable[hash_value];   //else store at head
            while (head->next != NULL) {
                head = head->next;
            }
            head->next = temp;
        }
    }
    fclose(fp);
}

int searchByNumber(char *number){
	int c = 1;
	
	if (*number == 'q'){
    	c = 0;
    	return c; 
	}
	
    int hash_value = abs(atoi(number)) % MAX;
    Phonebook *temp = hashTable[hash_value];
    while (temp != NULL) {
        if(strcmp(temp->phoneNumber,number) == 0){
            printf("Name: %s\nAddress: %s\nNumber: %s\nCode: %s\nStatus: %s\n",
                    temp->name, temp->address, temp->phoneNumber,temp->code,temp->status);
            break;
        }
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Phone number not found\n");
    }
    
    return c;
}

int main()
{
    createList();
    char number[30];
	
	do{
		printf("Enter phone number to search (type 'q' to exit): "); 
		fgets(number, sizeof number, stdin);
	    
	    int len1 = strlen(number);
	    if (len1 && number[len1 - 1] == '\n') {
	        number[--len1]= '\0';
	    }
	}while(searchByNumber(number) != 0);
	
	
    return 0;
}
