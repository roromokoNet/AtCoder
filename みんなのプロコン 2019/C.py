K,A,B = input().split()
K = int(K)
A = int(A)
B = int(B)
bi = 1
 
if(B-A<=2):
    bi+=K
else:
    bi=A
    K1=K-(A-1)
    bi+=((K1)//2)*(B-A)
    bi+=((K1)%2)
print(bi)