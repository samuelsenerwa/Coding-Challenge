#include <stdio.h>
#include <stdlib.h>

/**
 *
 * @brief: a function that concatenates two strings.
 *
 * function: char *str_concat(char *s1, char *s2)
 *
 * returned pointer should point a newly allocated memory  which contains
 * contents of s1
 *
 * on failure: return NULL
 *
 */

char *str_concat(char *s1, char *s2)
{
	char *concat_str;

	int i, j;
	int len1 = 0;
	int len2 = 0;

	/* Treat NULL as an empty string */
	if (s1 == NULL)
		s1 = "";
	if (s2 == NULL)
		s2 = "";

	/*calculating the length of s1 an s2 */
	while (s1[len1])
		len1++;
	while (s2[len2])
		len2++;
	len2++;

	/* allocating memory for the concatenated string */
	concat_str = malloc(sizeof(char) * (len1 + len2));
	if (concat_str == NULL)
		return (NULL);

	/* copy s1 into concat_str */
	i = 0;
	j = 0;

	while (s1[i])
		concat_str[j++] = s1[i++];
	i = 0;
	while (s2[i])
		concat_str[j++] = s2[i++];


	/*concat_str[i] = '\0';*/

	return (concat_str);
}
