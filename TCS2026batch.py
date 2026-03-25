"""A person has a balloon that can carry a maximum weight of Y kg.

There are N people, and each person has a certain weight given in an array W[].

The balloon can carry multiple people at once, but the total weight must not exceed Y kg.

Your task is to find the maximum number of people that can be carried in the balloon."""

n = int(input())
w = list(map(int, input().split()))
y = int(input())
w = w[:n]

count = 0
total = 0

w.sort()

for i in range(n):
    if total + w[i] <= y:
        total += w[i]
        count += 1
    else: 
        break

print(count)