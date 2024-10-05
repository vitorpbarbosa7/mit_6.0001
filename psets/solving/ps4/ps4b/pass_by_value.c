#include <stdio.h>

void modifyValue(int x) {
    x = 20;  // This change will not affect the original variable
}

int main() {
    int num = 10;
    modifyValue(num);
    printf("Value of num: %d\n", num);  // Output: Value of num: 10
    return 0;
}

