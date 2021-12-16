#Program to find sum of squares upto n

n = int(input("Enter the limit :"))
sum = 0
for i in range(1,n+1):
    sum = sum + i*i
print(f"Sum of squares of all numbers upto {n} = {sum} ")