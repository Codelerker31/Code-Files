#include <stdio.h>
#include <stdlib.h>
#include "box.h"


// Calculate the volume of a box
int volume(Box b) {
    return b.height * b.width * b.depth;
}

// Create the stack
Stack* create_stack(int num){
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->size = num;
    stack->top = -1;
    stack->boxes = (Box*)malloc(num * sizeof(Box));
    return stack;
}

// Push a box onto the stack
void push(Stack* s, Box b) {
    if (s->top < s->size) {
        s->boxes[s->top++] = b;
    } else {
        printf("Stack is full\n");
    }
}

// Pop a box off the stack
Box pop(Stack* s) {
    if (s->top > 0) {
        return s->boxes[--s->top];
    } else {
        printf("Stack is empty\n");
        Box empty_box = {0, 0, 0};
        return empty_box;
    }
}

// Display the boxes in the stack
void display(Stack* s) {
    printf("Stack contents:\n");
    for (int i = 0; i < s->top; i++) {
        printf("Box %d: Height=%d, Width=%d, Depth=%d, Volume=%d\n", 
               i+1, s->boxes[i].height, s->boxes[i].width, s->boxes[i].depth, volume(s->boxes[i]));
    }
}

// Free the memory used by the stack
void delete(Stack* s){
    free(s->boxes);
    free(s);
}
