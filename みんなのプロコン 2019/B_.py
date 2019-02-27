s = input()
s += input()
s += input()

if(
    not(s.count("1")==1 or s.count("1")==2) or 
    not(s.count("2")==1 or s.count("2")==2) or
    not(s.count("3")==1 or s.count("3")==2) or
    not(s.count("4")==1 or s.count("4")==2)
    ) :
    print("NO")
else:
    print("YES")