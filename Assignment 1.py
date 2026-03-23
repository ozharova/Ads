#Task 1
def from_one_to_n(n):
    if n == 0:
        return
    from_one_to_n(n - 1)
    print(n, end=" ")
n = int(input())
from_one_to_n(n)

#Task 2
def from_n_to_one(n):
    if n == 0:
        return
    print(n, end=" ")
    from_n_to_one(n - 1)
from_n_to_one(n)

#Task 3
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)
n = int(input())
print(sum(n))

#Task 4
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
n = int(input())
print(fact(n))

#Task 5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
a = int(input())
b = int(input())
print(power(a, b))

#Task 6
def sum_of_digets(n):
    if n < 10:
        return n
    if n == 0:
        return 0
    last = n % 10
    return last + sum_of_digets(n // 10)
n = int(input())
print(sum_of_digets(n))

#Task 7
def count(n):
    if n < 10:
        return 1
    a = 1
    if n // 10:
        return a + count(n // 10)
n = int(input())
print(count(n))

#Task 8
def reverse(n):
    if n == 0:
        return
    last = n % 10
    print(last, end="")
    return reverse(n // 10)
n = int(input())
reverse(n)

#Task 9
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
#Task 10
def  palindrome(s):
    if len(s) <= 1:
        return print("palindrome")
    if s[0] != s[-1]:
        return print("Not palindrome")
    return palindrome(s[1:-1])
s = str(input())
palindrome(s)

#Task 11
def sum_array(arr):
    if len(arr) == 0
        return 0
    else:
        return arr[0] + sum_array(arr[1:])
arr = list(map(int, input().split()))
print(sum_array(arr))

#Task 12
def max_array(arr):
    if len(arr) == 1:
        return arr[0]
    max_ = max_array(arr[1:])
    if arr[0] > max_:
        return arr[0]
    else:
        return max_
arr = list(map(int, input().split()))
print(max_array(arr))

#Task 13
def count_target(arr, target):
    if len(arr) == 0:
        return 0
    count = count_target(arr[1:], target)
    if arr[0] == target:
        return count + 1
    else:
        return count
arr = list(map(int, input().split()))
target = int(input())
print(count_target(arr, target))

#Task 14
def find_target(arr, target):
    if len(arr) == 0:
        return print("Not Found")
    if arr[0] == target:
        return print("Found")
    else:
        return find_target(arr[1: ], target)
arr = list(map(int, input().split()))
target = int(input())
find_target(arr, target)

#Task 15
def is_sorted(arr):
    if len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        return is_sorted(arr[1: ])
    return True
arr = list(map(int, input().split()))
if is_sorted(arr) == True:
    print("Sorted")
else:
    print("Not sorted")

#Task 16
def find_target(arr, target, start, end):
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return find_target(arr, target, mid + 1, end)
    if arr[mid] > target:
        return find_target(arr, target, start, mid - 1)
arr = list(map(int, input().split()))
target = int(input())
result = find_target(arr,target, 0, len(arr) - 1)
print(f"Element found at index {result}")