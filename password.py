password = input("Enter your password :")

numbers = '0123456789'
special_chars = '!@#$%^&*()_'
length = len(password)

res1= False
res2= False
res3 = False
res4 = False

if length >= 9 :
    for i in password:
        if i.isupper():
            res1 = True
            
        if i.islower():
            res2 = True
            
    for i in password:
        for j in special_chars:
            if i == j:
                res3 = True
        for k in numbers:
            if i == k:
                res4 = True
                

if res1 and res2 and res3 and res4 == True:
    print("Valid password!")
else:
    print('Invalid Pasword!')