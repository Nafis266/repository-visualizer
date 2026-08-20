#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

void greet()
{
    printf("Hello World\n");
}

int main()
{
    int result = add(5, 3);

    greet();

    printf("Result: %d\n", result);

    return 0;
}
