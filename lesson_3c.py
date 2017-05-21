def solution(N):
    total=sum(N)
    best = 99999999
    accum = 0
    for n in N[:-1]:
        accum += n
        diff = abs(2*accum - total)
        if (diff < best):
            best = diff
        if best == 0:
            break
    return best
    
S=[]
S.append([[3,1,2,4,3],1])
S.append([[1,1,2,4],0])
S.append([[1,1],0])
S.append([[0,0],0])
S.append([[0,0,1],1])
S.append([[0,1],1])
S.append([[1000,-1000,1000,1000],0])
S.append([[1000,-1000,1000,1000,1],1])
S.append([[-1000,1000],2000])

for s in S:
    sol = solution(s[0])
    if(sol != s[1]):
        print "{0} gave {1}, expecting {2}".format(s[0], sol, s[1])
    