#Print all numbers upto n using for loop

limit = int(input("Enter the limit :"))
print(f"Printing numbers upto {limit}")
for i in range(1,limit+1):
    print(i,end = ' ')
print("\n")
