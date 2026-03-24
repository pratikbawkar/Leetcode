N = int(input())
arr = [input()for i in range(N)]

found = False
	
for colour in arr:
    if arr.count(colour) % 2 !=0:
        print(colour)
        found = True
        break

if not found:
   print("All are even")
        