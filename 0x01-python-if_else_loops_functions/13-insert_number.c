#include "lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: linked list
 * @number: new data
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp = *head;

	if (!head)/*edge case*/
		return (NULL);

	node = malloc(sizeof(listint_t));
	if(!node)
		return (NULL);

	node->n = number;

	if (!*head) /*add first node */
	{
		*head = node;
		return (node);
	}

	while (tmp->next) /* add in sorted */
	{
		if (number <= tmp->next->n)
		{
						node->next = tmp->next;
						tmp->next = node;
						return (node);
		}
		tmp= tmp->next;
	}
	return (node);
}
