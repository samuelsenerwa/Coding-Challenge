#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a list_int list
 *@h: pointer to head of list
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *h;
    listint_t *h_prev;

    h = *head;
    new = malloc(sizeof(listint_t));

    if (new == NULL)
    {
        return NULL;
    }

    while (h != NULL)
    {
        if (h->n > number)
            break;
        h_prev = h;
        h = h->next;
    }

    new->n = number;

    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
    }
    else
    {
        new->next = h;
        if (h == *head)
        {
            *head = new;
        }
        else
        {
            h_prev->next = new;
        }
    }

    return new;
}