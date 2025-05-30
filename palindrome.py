class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeued_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_data

    def is_empty(self):
        return self.head is None


def is_palindrome_using_stack(s: str) -> bool:
    stack = Stack()
    queue = Queue()

    # push characters onto the stack and enqueue them into the queue
    for char in s:
        stack.push(char)
        queue.enqueue(char)

    # compare characters by popping from stack and dequeuing from queue
    while not stack.is_empty() and not queue.is_empty():
        stack_char = stack.pop()
        queue_char = queue.dequeue()
        if stack_char != queue_char:
            return False
    return True
print(is_palindrome_using_stack("racecar"))

