# comments
# immutable data types
# str
# int
# float
# bool
# bytes
# tuples

# mutable data types
# list,
# set
# dic

name: str = "John Doe"
age: int  = 29
aggregate: float = 77.9
is_raining: bool = False

x: tuple = (1, 2, 3)
list_names: list = ("John", "Mary")
nums = [2,3,4,1,34,123,321,1]


data: dict = {'name': 'Bob', 'age': 20}
print(data)

print(nums)


def get_largest(numbers, n):
    numbers.sort()

    return numbers[-n:]

sorted_list = get_largest(nums, 5)
#print(sorted_list)

# for x in "John":
#     print(x)

# for x in range(10):
#     print(x)

fruits = ["apple", "banana", "cherry", "kiwi"]

for i in fruits:
    print(i)
    if i == "kiwi":
        break

for i in range(2, 30):
    print(i)

i = 1

while i < 7:
    print(i)
# else:
#     print("i is no longer less than 7")








