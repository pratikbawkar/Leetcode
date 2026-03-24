# TCS NQT Practic Qestion

# n = int(input())
# arr = [int(input())for i in range(n)]

arr = list(map(int,input().split()))
store=1
max_now=arr[0]

for i in range(1,len(arr)):
    if arr[i] > max_now:
       store+=1
       max_now = arr[i]

print(store)