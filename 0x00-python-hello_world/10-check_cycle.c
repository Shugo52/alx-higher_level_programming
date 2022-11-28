#include "lists.h"

/**
 * check_cycle - Checks if theres a cycle in a linked list.
 * @list: list head.
 *
 * Return: 1 if theres a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !(list->next))
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
	/* return (traverse(list->next, list->next->next)); */
}
