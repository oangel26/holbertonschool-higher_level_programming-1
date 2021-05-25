#include "lists.h"

/**
 * get_node_idx - Get the node idx object
 * @head:  singly linked list
 * @idx: index to find
 * Return: listint_t*
 */
listint_t *get_node_idx(listint_t *head, size_t idx)
{
	size_t i;

	if (!head)
		return (0);

	for (i = 0; head->next && i < idx; i++)
		head = head->next;

	if (idx > i)
		return (NULL);
	return (head);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: single linked list
 * Return: 0 or 1 is palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *tmp = *head, *start = NULL, *end = NULL;

	if (!head || !*head) /*edge case*/
		return (IS_PALINDROME);

	for (len = 0; tmp->next; len++)
		tmp = tmp->next;

	tmp = *head; /* advance and compare since middle linked list*/
	for (i = 0; i < len; i++, len--)
	{
		start = get_node_idx(tmp, i);
		end = get_node_idx(tmp, len);
		if (start->n != end->n)
			return (NOT_PALINDROME);
	}
	return (IS_PALINDROME);
}
