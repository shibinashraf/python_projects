#Program to find whether a given number is prime or not

num = int(input("Enter a number:"))
flag = False
if num >1:
 for i in range(2,num):
  if num%i == 0:
   flag = True
   break

if flag == True:
 print(f'{num} is not a prime Number!')
else:
 print(f'{num} is a prime Number!')