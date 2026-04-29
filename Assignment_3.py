#Task 1 (two sum)
nums = [2, 7, 9, 17]
target = 9
myMap = {}
for i in range(len(nums)):
    num = nums[i]
    need = target - num
    if need in myMap:
        print(myMap[need], i)
    myMap[num] = i

#Task 2 (first non-repeating character)
str = "loveleetcode"
count = {}
for ch in str:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
for i in range(len(str)):
    if count[str[i]] == 1:
        print(i)
        break
else:
    print(-1)

#Task 3 (isomorphic strings)
s = "egg"
t = "add"
mapST = {}
mapTS = {}
if len(s) != len(t):
    print(False)
else:
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
            print(False)
            break
        mapST[c1] = c2
        mapTS[c2] = c1
    else:
        print(True)

#Task 4
n = 19
visited = set()
while n != 1:
    if n in visited:
        print(False)
        break
    visited.add(n)
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** 2
        temp = temp // 10
    n = total
if n == 1:
    print(True)

# Task 5
from collections import deque
root = [3,9,20,None,None,15,7]
queue = deque([0])
result = []
while queue:
    level = []
    size = len(queue)
    for i in range(size):
        index = queue.popleft()
        level.append(root[index])
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(root) and root[left] is not None:
            queue.append(left)
        if right < len(root) and root[right] is not None:
            queue.append(right)
    result.append(level)
print(result)

# Task 6
from collections import deque
root = [3,9,20,None,None,15,7]
queue = deque([0])
depth = 0
while queue:
    size = len(queue)
    for i in range(size):
        index = queue.popleft()
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(root) and root[left] is not None:
            queue.append(left)
        if right < len(root) and root[right] is not None:
            queue.append(right)
    depth += 1
print(depth)

#Task 7
from collections import deque
root = [1,2,2,3,4,4,3]
queue = deque([(1,2)])
symmetric = True
while queue:
    left, right = queue.popleft()
    if left >= len(root) and right >= len(root):
        continue
    if left >= len(root) or right >= len(root):
        symmetric = False
        break
    if root[left] is None and root[right] is None:
        continue
    if root[left] is None or root[right] is None:
        symmetric = False
        break
    if root[left] != root[right]:
        symmetric = False
        break
    queue.append((2*left+1, 2*right+2))
    queue.append((2*left+2, 2*right+1))
print(symmetric)


#Task 8
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = Node(1)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.right.right = Node(5)
longest_path = 1
def dfs(cur_node, prev_val, cur_length):
    global longest_path
    if cur_node is None:
        return
    if cur_node.val == prev_val + 1:
        cur_length += 1
    else:
        cur_length = 1
    if cur_length > longest_path:
        longest_path = cur_length
    dfs(cur_node.left, cur_node.val, cur_length)
    dfs(cur_node.right, cur_node.val, cur_length)
dfs(root, root.val - 1, 0)
print(longest_path)

#Task 9
nums = [2,0,2,1,1,0]
count0 = nums.count(0)
count1 = nums.count(1)
count2 = nums.count(2)
for i in range(count0):
    nums[i] = 0
for i in range(count0, count0 + count1):
    nums[i] = 1
for i in range(count0 + count1, len(nums)):
    nums[i] = 2
print(nums)

#Task 10
nums = [5,2,8,1,3]
def quicksort(left, right):
    if left >= right:
        return
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    quicksort(left, i - 1)
    quicksort(i + 1, right)
quicksort(0, len(nums) - 1)
print(nums)

#Task 11
nums = [5,2,8,1,3]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
nums = merge_sort(nums)
print(nums)

#Task 12
nums = [5,2,8,1,3]
def heapify(n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(n, largest)
def heap_sort():
    n = len(nums)
    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
heap_sort()
print(nums)