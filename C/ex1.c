#include <stdio.h>

/* This is a comment */

int main(int argc, char *argv[])
{
    int distance = 100;
    char lines[] = "-----"; 
    int age = 20;
    int year = 2026;
    int born = year - age;

    // this also comment
    printf("%s Test %s \n", lines, lines);
    printf("You born in %d. \n", born);
    printf("You are %d miles away. \n", distance);

    return 0;
}