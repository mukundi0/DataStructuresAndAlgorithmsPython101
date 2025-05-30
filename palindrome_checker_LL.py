class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

def is_palindrome(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    for char in s:
        if char != stack.pop():
            return False
    return True

print("Enter a string:")
s = input().strip()
if is_palindrome(s):
    print(f"The word, {s}, is a palindrome")
else:
    print(f"The word, {s}, is not a palindrome")