T = int(input())
case = 0
while(T>0):
    T=T-1
    case = case+1
    Trace = 0
    N = int(input())
    matrix = [[j for j in input().split()] for i in range(N)] 
    for i in range(N):
        Trace = Trace+int(matrix[i][i])
    matrix2 =[[row[i] for row in matrix] for i in range(len(matrix[0]))] 
    flag1=flag2=0
    check = list(range(1,N+1))
    for i in matrix:
        if not (sorted(list(map(int, i)))==check):
            flag1 = flag1+1         
    for i in matrix2:
        if not (sorted(list(map(int, i)))==check):
            flag2 = flag2+1
    print("Case #{}: {} {} {}".format(case,Trace,flag1,flag2))
