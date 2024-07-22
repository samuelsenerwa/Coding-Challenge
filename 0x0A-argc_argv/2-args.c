#include <stdio.h>
#include "main.h"

/**
 * @brief A program that prints all arguments it recieves
 *
 * @param argc The number of arguments
 * @param argv actual arguments in the program
 *
 * @return 0 on success
 */

int main(int argc, char *argv[])
{
    /* the number of arguments to be printed*/
    int i = 0;
    for(i = 0; i < argc; i++){
	    printf("%s\n", argv[i]);
    }
    return 0;
}
