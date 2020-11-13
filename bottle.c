#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
clock_t start, end;
double cpu_time_used;
start = clock();
int arg = strtol(argv[1], NULL, 10);
int answer;
int number = arg;
int counter = number;
int B_group = number;
int C_group = number;
int b = 1;
int c = 0;
int bremainder;
int cremainder;
int addon_bottle;

while (b || c)
{
    b = B_group / 2;
    c = C_group / 4;
    bremainder = B_group % 2;
    cremainder = C_group % 4;
    addon_bottle = b + c;
    counter = counter + addon_bottle;
    B_group = bremainder + addon_bottle;
    C_group = cremainder + addon_bottle;
}
answer = counter;
printf("%d \n", answer);
end = clock();
cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
printf("%f \n", cpu_time_used);
}