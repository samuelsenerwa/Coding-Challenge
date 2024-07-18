#include <stdio.h>
#include "main.h"

/**
 * @brief Print the name of the program
 *
 * @param argc
 * @param argv
 * @return int
 *
 * Return 0 on success
 */

int main(int argc, char *argv[])
{
    (void)argv; /*ignoring agrv*/
    printf("%i\n", argc - 1);

    return (0);
}