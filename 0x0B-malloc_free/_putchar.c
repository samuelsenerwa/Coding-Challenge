#include "main.h"
#include <unistd.h>

/**
 * @brief print character
 *
 */

int _putchar(char c)
{
    return (write(1, &c, 1));
}