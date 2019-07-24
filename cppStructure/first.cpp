#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Person
{
    char name[20];
    int age;
};

int main()
{
    //structure variable declaration with initialisation
    struct Person person = {"Deniss Ritchie", -60};
    //declare character buffer (byte array)
    char *buffer = (char *)malloc(sizeof(person));
    int i;

    //copying....
    memcpy(buffer, (const unsigned char *)&person, sizeof(person));

    //printing..
    printf("Copied byte array is:\n");
    for (i = 0; i < sizeof(person); i++)
        printf("%02X ", buffer[i]);
    printf("\n");

    //freeing memory..
    free(buffer);
    return 0;
}
