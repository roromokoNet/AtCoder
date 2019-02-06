num1 = input()
num1 = num1.split()
if(num1[1] <= num1[2]):
    print(num1[1]+" ", end="")
else:
    print(num1[2]+" ", end="")
if(int(num1[1])+int(num1[2])-int(num1[0]) <= 0):
    print("0")
else:
    print(int(num1[1])+int(num1[2])-int(num1[0]))