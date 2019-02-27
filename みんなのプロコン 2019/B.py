s = input()
s += input()
s += input()

q = [0,0,0,0]
q[0] = s.count("1")
q[1] = s.count("2")
q[2] = s.count("3")
q[3] = s.count("4")
q.sort()

if(q == [1,1,2,2]):
    print("YES")
else:
    print("NO")