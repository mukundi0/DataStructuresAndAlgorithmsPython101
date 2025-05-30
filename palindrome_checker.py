print("Enter a string: ")
s = input().strip()

stack = []

#Push all characters onto the stack
for char in s:
    stack.append(char)

#compare characters by popping from stack with original string
is_palindrome = True
for i in range(len(s)):
    if s[i] != stack.pop():
        is_palindrome = False
        break

if is_palindrome:
    print(f"The word, {s}, is a palindrome")
else:
    print(f"The word, {s}, is not a palindrome")