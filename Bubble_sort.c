/* Program to demonstrate time taken by function quickSort() */
#include <stdio.h> 
#include <stdlib.h>
#include <time.h>

// A function to implement bubble sort 
void bubbleSort(int arr[], int n) 
{ 
	int i, j, swap; 
	for (i = 0; i < n-1; i++) {
		swap = -1;
		for (j = 0; j < n-1; j++) {
			if (arr[j] > arr[j+1]) {
				int temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
				swap = 1;
			}
		}
		if(swap == -1)
			break;
	}
} 

// The main program calls bubblesort() and measures time taken by bubblesort()
int main()
{
    int arr[10000], i;
    int n = 10000;
	for (i=0;i<n;i++)
    {
        arr[i] = (rand() % 1000);
    }
    // Calculate the time taken by bubblesort()
    clock_t t;
    t = clock();
    bubbleSort(arr, n);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
 
    printf("bubblesort() took %f seconds to execute \n", time_taken);
    return 0;
}
