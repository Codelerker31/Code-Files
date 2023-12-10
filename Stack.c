#include <stdio.h>
#include <stdlib.h>

struct Box {
    int height;
    int width;
    int depth;
};

typedef struct {
    int size; // number of boxes the stack can hold
    int top; // index of the top element in the stack
    struct Box *arr; // array of boxes
} Stack;

// function to create a new box
struct Box createBox(int h, int w, int d) {
    struct Box box;
    box.height = h;
    box.width = w;
    box.depth = d;
    return box;
}

// function to calculate the volume of a box
int calculateVolume(struct Box box) {
    return box.height * box.width * box.depth;
}

// function to create a new stack
Stack* createStack(int size) {
    Stack *stack = (Stack*) malloc(sizeof(Stack));
    stack->size = size;
    stack->top = -1;
    stack->arr = (struct Box*) malloc(size * sizeof(struct Box));
    return stack;
}

// function to check if the stack is full
int isFull(Stack *stack) {
    return stack->top == stack->size - 1;
}

// function to check if the stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// function to push a box onto the stack
void push(Stack *stack, struct Box box) {
    if (isFull(stack)) {
        printf("Stack is full\n");
        return;
    }
    stack->top++;
    stack->arr[stack->top] = box;
}

// function to pop a box from the stack
struct Box pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        struct Box box = createBox(0, 0, 0);
        return box;
    }
    struct Box box = stack->arr[stack->top];
    stack->top--;
    return box;
}

int main() {
    Stack *stack = createStack(5);
    struct Box box1 = createBox(1, 2, 3);
    struct Box box2 = createBox(4, 5, 6);
    push(stack, box1);
    push(stack, box2);
    struct Box popped = pop(stack);
    printf("Popped box: height = %d, width = %d, depth = %d\n", popped.height, popped.width, popped.depth);
    free(stack->arr);
    free(stack);
    return 0;
}