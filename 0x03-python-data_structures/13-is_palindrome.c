#include "lists.h"

#define BUFFER_SIZE 5000

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
	int array[BUFFER_SIZE];

	if (!head || !*head) /*edge case*/
		return (IS_PALINDROME);

	tmp = *head;
	for (len = 0; tmp; len++) /*create array */
	{
		array[len] = tmp->n;
		tmp = tmp->next;
	}

	/* advance and compare since middle linked list*/
	for (i = 0; i < len; i++, len--)
		if (array[i] != array[len - 1])
			return (NOT_PALINDROME);
	return (IS_PALINDROME);
}
