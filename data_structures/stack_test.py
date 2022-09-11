import unittest

from stack import Stack


class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEquals(3, stack.size)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEquals(3, stack.pop())
        self.assertEquals(2, stack.pop())
        self.assertEquals(1, stack.pop())
        self.assertEquals(0, stack.size)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEquals(3, stack.peek())

    def test_pop_empty_stack_raises_exception(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.pop()

    def test_peek_empty_stack_raises_exception(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.peek()


if __name__ == '__main__':
    unittest.main()
