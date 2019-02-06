base = int(input())
 
data = [[0 for i in range(3)] for j in range(base)]
 
for num in range(base):
    _num = input()
    _num = _num.split()
    data[num][0] = int(_num[0])+int(_num[1])
    data[num][1] = int(_num[0])
    data[num][2] = int(_num[1])
 
takahashi = 0
aoki = 0
data.sort()
data.reverse()
 
_num = 0
for num in range(base):
    if(_num == 0):
        takahashi += data[num][1]
        _num = 1
 
    elif(_num == 1):
        aoki += data[num][2]
        _num = 0
 
print(takahashi-aoki)