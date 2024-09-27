#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: a pointer to the head od listint_s
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *f1 = list;
	listint_t *f2 = list;

	while (f2 != NULL && f2->next != NULL)
	{
		f1 = f1->next;
		f2 = f2->next->next;

		if (f1 == f2)
			return (1);
	}
	return (0);
}
