T = int(input())
case = 0
while(T>0):
    T = T-1
    case = case+1
    #S = list(map(int, input().split()))
    S = list(map(int, str(input())))
    #print(S)
    op = []
    op2 = ''
    difference = []
    for i in range(len(S)-1):
        difference.append(S[i]-S[i+1])
    difference.insert(0,-1*S[0])
    difference.insert(len(S),S[-1])
    for i in range(len(S)):
        if difference[i]<0:
            op.append(abs(difference[i])*'(')
            op.append(S[i])
        else:
            op.append(difference[i]*')')
            op.append(S[i])
    op.append(difference[-1]*')')
    while '' in op:
        op.remove('')
    for i in op:
        op2 = op2+str(i)
    print("Case #{}: {}".format(case, op2))
    
    
