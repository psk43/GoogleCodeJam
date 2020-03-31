T = int(input())
while(T>0):
    N = str(input())
    A = B = 0
    for i in range(0,len(N)):
        if(N[i]=='4'):
            B = B+10**i
    A = int(N) - B   
    print("Case #{}: {} {}".format(T,A,B))
    T = T-1
