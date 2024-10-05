#include <stdio.h>

void modifyValue(int *x) {
    *x = 20;  // Dereference the pointer and change the actual memory value
}

int main() {
    int num = 10;
    modifyValue(&num);  // Pass the address of 'num'
    printf("Value of num: %d\n", num);  // Output: Value of num: 20
    return 0;
}

