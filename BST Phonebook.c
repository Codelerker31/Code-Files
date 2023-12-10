#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdio.h>
#define MAX 1000

typedef struct phonebook {
    char phoneNumber[20];
    char code[10];
    char name[50];
    char address[100];
    char status[10];
    struct phonebook *next;
} Phonebook;
 
typedef struct BSTNode {
    char phoneNumber[20];
    Phonebook *data;
    struct BSTNode *left;
    struct BSTNode *right;
} BSTNode;

BSTNode* hashTable[MAX];

BSTNode* createNode(char* number, Phonebook *data) {
    BSTNode *newNode = (BSTNode*)malloc(sizeof(BSTNode));
    strcpy(newNode->phoneNumber, number);
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

void insertNode(BSTNode **root, char* number, Phonebook *data) {
    if (*root == NULL) {
        *root = createNode(number, data);
        return;
    }
    if (strcmp(number, (*root)->phoneNumber) < 0) {
        insertNode(&(*root)->left, number, data);
    } else {
        insertNode(&(*root)->right, number, data);
    }
}

Phonebook *searchNode(BSTNode *root, char* number) {
    if (root == NULL) {
        return NULL;
    }
    if (strcmp(number, root->phoneNumber) == 0) {
        return root->data;
    }
    if (strcmp(number, root->phoneNumber) < 0) {
        return searchNode(root->left, number);
    }
    return searchNode(root->right, number);
}

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
            hashTable[hash_value] = createNode(temp->phoneNumber, temp);
        }
        else {
            insertNode(&hashTable[hash_value], temp->phoneNumber, temp);
        }
    }
    fclose(fp);
}

void searchByNumber(char *number){
    int hash_value = abs(atoi(number)) % MAX;
    Phonebook *temp = searchNode(hashTable[hash_value], number);
    if (temp == NULL) {
        printf("Phone number not found\n");
    } else {
        printf("Name: %s\nAddress: %s\nNumber: %s\nCode: %s\nStatus: %s\n",
            temp->name, temp->address, temp->phoneNumber,temp->code,temp->status);
    }
}

int main()
{
	createList();
	char number[30];
	printf("Enter phone number to search (type 'q' to exit): "); 
	if (fgets(number, sizeof number, stdin) == NULL)
		fprintf(stderr, "No line read\n");
		
	int len1 = strlen(number);
	if (len1 && number[len1 - 1] == '\n')
		number[--len1] = '\0';
		
	while(strcmp(number, "q") != 0) {
		searchByNumber(number);
		printf("Enter phone number to search (type 'q' to exit): "); 
	    if (fgets(number, sizeof number, stdin) == NULL)
	        fprintf(stderr, "No line read\n");
	    int len1 = strlen(number);
	    if (len1 && number[len1 - 1] == '\n')
	        number[--len1] = '\0';
	}
    return 0;
}
