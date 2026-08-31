#include <stdio.h>

#define BUFFER_SIZE 10
char buffer[BUFFER_SIZE];
int index = 0;

void add_char(char c) {
    if (index < BUFFER_SIZE) {
        buffer[index++] = c;
    }
}

void print_buffer() {
    for (int i = 0; i < index; i++) {
        printf("%c", buffer[i]);
    }
    printf("\n");
}
