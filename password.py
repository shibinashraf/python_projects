password = input("Enter your password :") # input user password
numbers = '0123456789' # Storing all numbers possible
special_chars = '!@#$%^&*()_' # all special characters
length = len(password) #finding length of user password

res1= False
res2= False
res3 = False
res4 = False

if length >= 9 :  #checking if length of password is greater than 9

    for i in password: 
        if i.isupper(): #checking if the password contains any uppercase chars
            res1 = True
            
        if i.islower(): #checking if the password contains any lowercase chars
            res2 = True
            
        for j in special_chars: #checking if the password contains any spcl chars
            if i == j:
                res3 = True
            
        for k in numbers: #checking if the password contains any numbers
            if i == k:
                res4 = True
    if res1 and res2 and res3 and res4 == True: # if all the requirements are satisfies then valid else invalid
     print("Valid password!")
    else:
        if res1 == False:
            print("Password should contain atleast one UpperCase Character !")
        if res2 == False:
            print("Password should contain atleast one LowerCase Character !")
        if res3 == False:
            print("Password should contain atleast one Special Character !")
        if res4 == False:
            print("Password should contain atleast one Number!")            
else:
 print("Invalid passsword! must contain atleast 9 characters")
