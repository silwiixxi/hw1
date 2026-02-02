#201
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

#202
n = int(input())
print(n * (n + 1) // 2)

#203
n = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers))

#204
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)

#205
n = int(input())
x = 1
while x < n:
    x *= 2
if x == n:
    print("YES")
else:
    print("NO")

#206
n = int(input())
numbers = list(map(int, input().split()))
print(max(numbers))

#207
n = int(input())
numbers = list(map(int, input().split()))
max_value = numbers[0]
pos = 1
for i in range(1, n):
    if numbers[i] > max_value:
        max_value = numbers[i]
        pos = i + 1 
print(pos)

#208
n = int(input())
x = 1
while x <= n:
    print(x, end=" ")
    x *= 2

#209 
n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
min_value = min(arr)
for i in range(n):
    if arr[i] == max_value:
        arr[i] = min_value
print(*arr)

#210
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(*arr)

#211
n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
arr[l-1:r] = arr[l-1:r][::-1]
print(*arr)

#212
n = int(input())
arr = list(map(int, input().split()))
arr = [x**2 for x in arr]
print(*arr)

#213
n = int(input())
if n < 2:
    print("No")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")

#214
n = int(input())
arr = list(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
max_freq = max(freq.values())
candidates = [k for k, v in freq.items() if v == max_freq]
print(min(candidates))

#215
n = int(input())
s = set()
for _ in range(n):
    s.add(input())
print(len(s))

#216
n = int(input())
arr = list(map(int, input().split()))
seen = set()
for x in arr:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)

#217
n = int(input())
d = {}
for _ in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
cnt = 0
for v in d.values():
    if v == 3:
        cnt += 1
print(cnt)

#218
n = int(input())
arr = [input() for _ in range(n)]
first = {}
for i, s in enumerate(arr):
    if s not in first:
        first[s] = i + 1
for s in sorted(first):
    print(s, first[s])

#219
n = int(input())
d = {}
for _ in range(n):
    s, k = input().split()
    k = int(k)
    d[s] = d.get(s, 0) + k
for s in sorted(d):
    print(s, d[s])

#220
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
document = {} 
line = 1
while line < len(data):
    cmd = data[line].split()
    if cmd[0] == "set":
        key = cmd[1]
        value = " ".join(cmd[2:])
        document[key] = value
    elif cmd[0] == "get":
        key = cmd[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key} found in the document")
    line += 1