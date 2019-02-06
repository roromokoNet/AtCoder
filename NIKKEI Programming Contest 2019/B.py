num1 = int(input())
num2 = input()
num3 = input()
num4 = input()

num2 = list(num2)
num3 = list(num3)
num4 = list(num4)

_num = 0
for num in range(num1):
    if(num2[num] == num3[num]):
        if(num2[num] == num4[num]):
            _num += 0
        else:
            _num += 1
    else:
        if(num2[num] == num4[num]):
            _num += 1
        else:
            if(num3[num] == num4[num]):
                _num += 1
            else:
                _num += 2

print(_num)