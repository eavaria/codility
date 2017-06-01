import unittest


def solution(A,B):
    if len(A)==1:
        return 1    
    F = zip(B,A)
    S = []
    count = 0
    for f in F:
        if(f[0] == 1):
            S.append(f[1])     
        elif(len(S) == 0):
                count += 1
        else:
            while(True):
                if(len(S) == 0):
                    count += 1
                    break
                elif(S[-1] < f[1]):
                    S.pop()
                else:
                    break
    return count + len(S)
    
S=[]
S.append([[[4,3,2,1,5],[0,1,0,0,0,0]],2])
S.append([[[1,4,6,3,5,2],[0,0,1,0,1,0]],4])
S.append([[[1,4,6,3,2,5],[1,0,0,1,1,0]],3])
S.append([[[3,4,2],[1,0,1]],2])
S.append([[[3],[1]],1])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()