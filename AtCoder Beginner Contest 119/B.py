num = input()
en = 0.0
for x in range(int(num)):
    num1 = input().split()
    if(num1[1] == "JPY"):
        en += float(num1[0])
    else:
        en += float(num1[0])*380000.0
print(en)