#include "lists.h"

#include <stdlib.h>
/**
 * is_palindrome - check if linked list is palindrome
 * @head: single linked list
 * Return: 0 or 1 is palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t len = 0, i = 0;
	listint_t *tmp = *head;
	int *array = NULL;

	if (!head || !*head) /*edge case*/
		return (IS_PALINDROME);

	for (len = 0; tmp; len++)
		tmp = tmp->next;

	/*create array */
	array = malloc(sizeof(int) * len -1);
	if (!array)
		return (0);

	tmp = *head;
	for (i = 0; i < len; i++)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
	}

	/* advance and compare since middle linked list*/
	for (i = 0; i < len; i++, len--)
	{
		if (array[i] != array[len - 1])
		{
			free(array);
			return (NOT_PALINDROME);
		}
	}
	free(array);
	return (IS_PALINDROME);
}
