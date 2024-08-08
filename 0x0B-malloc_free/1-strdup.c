#include<stdio.h>
#include<stdlib.h>
#include "main.h"

/**
 *@breif: function that returns a pointer to a newly allocated space in memory, which contains a copy
of the string given as a parameter.
 *
 * @return: Returns NULL if str = NULL
 */

char *_strdup(char *str) {
	char *dup_str;
	int len = 0;
	int i;


	if (str == NULL)
		return (NULL);

	while (str[len])
		len++;


	dup_str = malloc(sizeof(char) * (len++));
	
	if (dup_str == NULL)
		return (NULL);

	for (i = 0; i < len; i++)
		dup_str[i] = str[i];


	return(dup_str);
}
