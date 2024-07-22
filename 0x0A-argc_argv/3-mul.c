#include <stdio.h>
#include "main.h"

/**
 * @brief program that multiplies two numbers
 *
 * @param argc The number of arguments
 * @param argv actual arguments in the program
 *
 * @return 0 on success
 */

int main(int argc, char *argv[]) {
	if(argc != 3) {
		printf("Error\n");
			return (1);
	}
	else
		printf("%d\n", (atoi(argv[argc - 1]) * atoi(argv[argc - 2])));

	return (0);
}
