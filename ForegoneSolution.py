T = int(input())
Q=0
while(T>0):
    Q=Q+1
    T=T-1
    N = str(input())
    A = B = 0
    for i in range(0,len(N)):
        if(N[i]=='4'):
            B = B+10**(len(N)-i-1)
    A = int(N) - B   
    print("Case #{}: {} {}".format(Q,A,B))
