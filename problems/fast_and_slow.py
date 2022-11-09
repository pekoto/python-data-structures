from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


def has_cycle(node: Node) -> bool:
    """
    Given the head of a Singly LinkedList,
    write a function to determine if the LinkedList has a cycle in it or not.

    Ex:
    1 > 2 > 3 > 4 > 5 > 6
        ^               |
        |----------------
    """
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def cycle_length(node: Node) -> int:
    """
    Given the head of a LinkedList with a cycle, find the length of the cycle.

    Ex:
    1 > 2 > 3 > 4 > 5 > 6
        ^               |
        |----------------

    Length=5
    """
    slow = node
    fast = node
    cycle_found = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_found = True
            break

    if not cycle_found:
        return 0

    # Set to slow + 1 so we don't hit while condition immediately
    cycle_len = 1
    fast = slow.next

    while fast != slow:
        fast = fast.next
        cycle_len += 1

    return cycle_len


def start_of_cycle(node: Node) -> Node:
    """
    Given the head of a Singly LinkedList that contains a cycle,
    write a function to find the starting node of the cycle.

    Ex:
    1 > 2 > 3 > 4 > 5 > 6
        ^               |
        |----------------

    Solution:
    1. Find the cycle
    2. Move slow back to the start
    3. Move slow and fast 1 node at a time until they meet

    Proof:
    Floyd's Cycle Detection algorithm. Essentially we have to
    create a formula showing:
    slow_dist = m + slow*l + k
    fast_dist = m + fast*l + k
    m = len to start of loop
    l = loop len
    k = dist from start until they meet

    Given fast moves 2x more than slow, we can work these formulas out.
    Since m will be at point m+k (being at k) to the start, moving it
    m will put it back to the start.
    """
    slow = node
    fast = node
    loop_found = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            loop_found = True
            break

    if not loop_found:
        return None

    slow = node

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def is_happy(num: int) -> bool:
    """
    Any number will be called a happy number if, after repeatedly replacing it
    with a number equal to the sum of the square of all of its digits, leads us
    to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

    Input: 23,    Output: true (23 is a happy number)
    Here are the steps to find out that 23 is a happy number:

    2^2 + 3 ^22​2​​+3​2​​ = 4 + 9 = 13
    1^2 + 3^21​2​​+3​2​​ = 1 + 9 = 10
    1^2 + 0^21​2​​+0​2​​ = 1 + 0 = 1
    """
    slow = num
    fast = num

    while True:
        slow = _find_square_sum(slow)
        fast = _find_square_sum(fast)
        fast = _find_square_sum(fast)

        if fast == 1:
            return True

        if slow == fast:
            return False

    return False


def _find_square_sum(num: int) -> int:
    """Helper function to find the square of a numbers digits"""
    result = 0

    while num > 0:
        result += ((num % 10)**2)
        num //= 10

    return result


def find_middle_of_linked_list(head: Node) -> Node:
    """
    Given the head of a Singly LinkedList, write a method to return
    the middle node of the LinkedList.

    If the total number of nodes in the LinkedList is even, return the
    second middle node.

    Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
    Output: 3
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def linked_list_palindrome(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList,
    write a method to check if the LinkedList is a palindrome or not.

    Input: 2 -> 4 -> 6 -> 4 -> 2 -> null, True
                     ^
                               ^
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null, False
    """
    # If list is an even size, not a palindrome
    # If fast becomes null, it is even size: return false
    # When fast.next is None, slow in the middle of the list
    # Reverse from mid to end

    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if not fast:
        # List was even size
        return False

    # Reverse and copy the second half
    second_half_reversed_head = _reverse(slow)
    second_half_head_copy = second_half_reversed_head

    while head and second_half_reversed_head:
        if head.value != second_half_reversed_head.value:
            break  # Not a palindrome

        head = head.next
        second_half_reversed_head = second_half_reversed_head.next

    _reverse(second_half_head_copy)

    if not head or not second_half_reversed_head:
        return True  # Found a palindrome

    return False


def _reverse(node: Node) -> Node:
    """Helper function to reverse a linked list from node."""
    previous = None
    current = node
    next = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def interleave_linked_list(head: Node) -> None:
    """
    Given the head of a Singly LinkedList, write a method to modify the
    LinkedList such that the nodes from the second half of the LinkedList
    are inserted alternately to the nodes from the first half in reverse order.

    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null


    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

    If fast is not null, move to before slow and reverse from there
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = _reverse(slow)
    first_half = head

    while first_half and second_half:
        first_half_next = first_half.next
        first_half.next = second_half
        first_half = first_half_next

        second_half_next = second_half.next
        second_half.next = first_half
        second_half = second_half_next

    if first_half:
        first_half.next = None
