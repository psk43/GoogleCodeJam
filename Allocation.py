T = int(input())
Q=0
while(T>0):
    T=T-1
    Q=Q+1
    sum=count=0
    N, B=map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    for i in A:
        if sum+i<=B:
            sum+=i
            count+=1
        else:
            break
    
    print("Case #{}: {}".format(Q, count))
