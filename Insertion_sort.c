/* Program to demonstrate time taken by function quickSort() */
#include <math.h> 
#include <stdio.h> 
#include <stdlib.h>
#include <time.h>

//author https://www.geeksforgeeks.org/insertion-sort

// Function to sort an array using insertion sort
void insertionSort(int arr[], int n) 
{ 
	int i, key, j; 
	for (i = 1; i < n; i++) { 
		key = arr[i]; 
		j = i - 1; 

		/* Move elements of arr[0..i-1], that are 
		greater than key, to one position ahead 
		of their current position */
		while (j >= 0 && arr[j] > key) { 
			arr[j + 1] = arr[j]; 
			j = j - 1; 
		} 
		arr[j + 1] = key; 
	} 
} 

// The main program calls insertionsort() and measures time taken by insertionsort()
int main()
{
    int arr[10000], i;
    int n = 10000;
	for (i=0;i<n;i++)
    {
        arr[i] = (rand() % 1000);
    }
    // Calculate the time taken by insertionsort()
    clock_t t;
    t = clock();
    insertionSort(arr, n);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
 
    printf("insertionort() took %f seconds to execute \n", time_taken);
    return 0;
}
