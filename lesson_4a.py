def solution(A):
    A.sort()
    for i, a in enumerate(A):
        if (i+1 != a):
            return 0
    return 1
    
def solution_(A):
    m = A.sort()
    if A[-1] == len(A):
        return 1
    else:
        return 0
S=[]
S.append([[4,1,3,2],1])
S.append([[4,1,2,2],0])
S.append([[4,1,2],0])
S.append([[4,1,2],0])

for s in S:
    sol = solution(s[0])
    if(sol != s[1]):
        print "{0} gave {1}, expecting {2}".format(s[0], sol, s[1])
    