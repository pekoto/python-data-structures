from typing import Any


class Stack:
    """A LIFO queue. Could also be implemented with a linked list.

    Operations:
        Push: O(1), O(n) amortized if using an array.
        Peek/Pop: O(1), O(n) amortized if using an array.

    Uses:
    - Browser back function.
    - Undo function.
    - Interpreter
        * Pop values on value stack.
        * Pop operators on operator stack.
        * At right parenthesis, pop two values and an operator.
        * Push the value back on the stack.
    """
    def __init__(self) -> None:
        self._stack = []
        self.size = 0

    def push(self, val: Any) -> None:
        """Pushes a value on to the stack.

        Args:
            val: The value to push onto the stack.
        """
        self._stack.append(val)
        self.size += 1

    def peek(self) -> Any:
        """Returns the value on the top of the stack.

        Returns:
            The value on the top of the stack.
        """
        if self.size == 0:
            raise Exception('Stack is empty.')

        return self._stack[-1]

    def pop(self) -> Any:
        """Pops and returns the value on top of the stack.

        Returns:
            The value on the top of the stack.
        """
        if self.size == 0:
            raise Exception('Stack is empty.')

        self.size -= 1

        return self._stack.pop()