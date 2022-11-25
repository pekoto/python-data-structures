from typing import Any

from problems.fast_and_slow import Node


class Node:

    def __init__(self, value: Any, next: Node = None):
        self.value = value
        self.next = next

    def __str__(self) -> None:
        return self.val


def reverse_linked_list(head: Node) -> Node:
    """
    Given the head of a Singly LinkedList, reverse the LinkedList.
    Write a function to return the new head of the reversed LinkedList.
    1 > 2 > 3 > 4 > 5
    """
    previous = None
    current = head
    next_node = None

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def reverse_sublist(head: Node, p: int, q: int) -> Node:
    """
    Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList
    from position ‘p’ to ‘q’.

    1 > 2 > 3 > 4 > 5 > null, p=2, q=4 -->
    1 > 4 > 3 > 2 > 5

    Similar problems:
        - Reverse the first ‘k’ elements of a given LinkedList.
    """
    # 1 > 2 > 3 > 4 > 5
    # i = 1
    # store start_of_reverse
    # store prev, current, next
    # once i = p, start reversing
    # prev = 4
    # curr = 5
    # next = null
    # 1 > 4< 2 4< 3 < 4 > 5 >
    # 2 > 1
    # just before reverse.next = prev (4)
    # old_head.next = curr (5)
    i = 1

    previous = None
    current = head
    next_node = None
    before_start_of_reversed_list = None
    start_of_reversed_list = None

    while current:

        if i == p:
            # Save the start of reverse section
            start_of_reversed_list = current
            before_start_of_reversed_list = previous
        if p <= i <= q:
            # In reverse section
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        else:
            next_node = current.next
            previous = current
            current = next_node

        if i == q:
            # Finished reversing sub list
            break

        i += 1

    before_start_of_reversed_list.next = previous
    start_of_reversed_list.next = current

    return head


def reverse_k_element_sublist(head: Node, k: int) -> Node:
    """
    Given the head of a LinkedList and a number ‘k’,
    reverse every ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than
    ‘k’ elements, reverse it too.
    
    1 > 2 > 3 > 4 > 5 > 6 > 7 > 8, k = 3 -->
    3 > 2 > 1 > 6 > 5 > 4 > 8
    """
    previous = None
    current = head
    next_node = None
    start_of_reversed_list = head
    end_of_reversed_list = None
    head_to_return = None

    while current:

        i = 0
        start_of_reversed_list = current

        while i < k and current:
            # Reverses sublist
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            i += 1

        if not head_to_return:
            # Set the head for the whole list (one time)
            head_to_return = previous
        else:
            # Connect end of previous list with this list
            end_of_previous_list.next = previous
            previous = None

        end_of_previous_list = start_of_reversed_list

    return head_to_return


def reverse_alternating_k_element_sublist(head: Node, k: int) -> Node:
    """
    Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’
    sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

    1 > 2 > 3 > 4 > 5 > 6 > 7 > 8, k = 2 -->
    2 > 1 > 3 > 4 > 6 > 5 > 7 > 8
    """
    previous = None
    current = head
    next_node = None
    start_of_reversed_list = head
    end_of_reversed_list = None
    head_to_return = None
    alternating = True

    while current:

        i = 0
        start_of_reversed_list = current

        while i < k and current:
            # Reverses sublist
            next_node = current.next
            if alternating:
                current.next = previous
            previous = current
            current = next_node

            i += 1

        if not head_to_return:
            # Set the head for the whole list (one time)
            head_to_return = previous
        else:
            if alternating:
                end_of_previous_list.next = previous
            else:
                end_of_previous_list.next = start_of_reversed_list

        if alternating:
            end_of_previous_list = start_of_reversed_list
        else:
            end_of_previous_list = previous

        alternating = not alternating
        previous = None

    return head_to_return


def rotate_linked_list(head: Node, rotations: int) -> Node:
    """
    Given the head of a Singly LinkedList and a number ‘k’,
    rotate the LinkedList to the right by ‘k’ nodes.

    1 > 2 > 3 > 4 > 5 > 6  k=3  --> 4 > 5 > 6 > 1 > 2 > 3
    1 > 2 > 3 > 4 > 5,     k=8  --> 3 > 4 > 5 > 1 > 2
    1 > 2 > 3 > 4 > 5 > 6  k=4  --> 3 > 4 > 5 > 6 > 1 > 2
    """
    # Find the length and last node in the list
    last_node = head
    list_length = 1

    while last_node.next:
        last_node = last_node.next
        list_length += 1

    # Connect the last node in the list to make it circular
    last_node.next = head  # Connect for rotations
    rotations %= list_length  # In case rotations > len of list
    length_of_sublist_to_move = list_length - rotations  # Skip length = length of sublist to move.

    # Get the last node in the rotated list
    last_node_of_rotated_list = head
    i = 1
    while i < length_of_sublist_to_move:
        last_node_of_rotated_list = last_node_of_rotated_list.next
        i += 1

    head = last_node_of_rotated_list.next  # e.g. 3 > 4 (4 becomes head)
    last_node_of_rotated_list.next = None

    return head


def rotate_linked_list_2(head: Node, rotations: int) -> Node:

    # First, work out the tail and size of the current linked list
    tail = head
    len_of_list = 1
    while tail.next:
        tail = tail.next
        len_of_list += 1

    # Next, make it a circular list, so when we rotate it we don't go off the end
    tail.next = head

    # Now, work out the rotations and size of list to move, skip size
    rotations %= len_of_list
    size_of_sublist = len_of_list - rotations

    # Now, get the last node in the sublist to move
    last_node_in_sublist = head
    i = 1

    while i < size_of_sublist:
        last_node_in_sublist = last_node_in_sublist.next
        i += 1

    head = last_node_in_sublist.next
    last_node_in_sublist.next = None

    return head
