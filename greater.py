#Program to find greatest number among 3 numbers


x = int(input('Enter num1 :'))
y = int(input('Enter num2 :'))
z = int(input('Enter num3 :'))

if x > y:
    if z > x :
        print(f'{z} Greater than {x},{y}')
    else:
        print(f'{x} Greater than {z},{y}')
else:
    if z > y:
        print(f'{z} Greater than {y},{x}')
    else:
        print(f'{y} Greater than {z},{x}')
