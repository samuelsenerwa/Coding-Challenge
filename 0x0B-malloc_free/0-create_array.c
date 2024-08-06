#include "main.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * @brief a function that creates an array of chars, and initializes it with a specific char.
 *
 * @param char *create_array(unsigned int size, char c);
 *
 * @returns NULL if size = 0
 *  otherwise a pointer to the array, or NULL if it fails
 *
 */

char *create_array(unsigned int size, char c)
{
	unsigned int i;
	char *arr = NULL;
    
	/* check if the size is zero */
	if (size == 0 )
		return (NULL);
	
	if (size != 0){
		arr = (char *)malloc(size * sizeof(char));

		if (arr != 0) {
			for (i = 0; i < size; i++) {
				arr[i] = c;
			}
		}
	}
	return (arr);

}
