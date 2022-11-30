#include "lists.h"

/**
 * insert_node - Inserts a number in a sorted linked list.
 *
 * @head: List beginning.
 * @number: Integer value of the node to insert in the list.
 *
 * Return: NULL on failure, or Node address.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = NULL, *node;

	/* Create the linked-list node */
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	/* If linked list is enpty, insert new node */
	if (!(current))
	{
		*head = node;
		return (node);
	}

	/* Insert node in correct position */
	while (current->n < number)
	{
		if (current->next != NULL)
		{
			prev = current;
			current = current->next;
			continue;
		}
		current->next = node;
		return (node);
	}

	node->next = current;
	if (prev)
		prev->next = node;
	else
		*head = node;

	return (node);
}
