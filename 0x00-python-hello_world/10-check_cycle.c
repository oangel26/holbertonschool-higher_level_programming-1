#include "lists.h"

/**
* check_cycle - validate if is a cycle linked list
* @list: linked list
* Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list, fast = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
