#include <stdio.h>
#include <stdlib.h>

/**
 * @brief a program that prints the minimum number of coins to make change for an amount of money.
 *
 * @param argc number of the command line arguments
 * @param argv program to print
 *
 *  @return 0 on success
 */

int isInteger(const char *s)
{
    int i = 0;

    while (s[i] != '\0')
    {
        if (s[i] < '0' || s[i] > '9')
            return 0;
        i++;
    }
    return (1);
}

int main(int argc, char *argv[])
{
    int i = 0, coinsused = 0, coin = 0;
    int coins[] = {25, 10, 5, 2, 1};

    if (argc != 2)
    {
        printf("Error \n ");
        return (1);
    }
    if (!isInteger(argv[1]))
    {
        i = atoi(argv[1]);
        while (i > 0 && coin <= 4)
        {
            if (i >= coins[coin])
            {
                i -= coins[coin];
                coinsused++;
            }
            else
            {
                coin++;
            }
        }

        printf("%i\n", coinsused);
        return (0);
    }
}