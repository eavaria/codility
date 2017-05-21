import unittest

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
S.append([[[3,1,2,4,3]],1])
S.append([[[1,1,2,4]],0])
S.append([[[1,1]],0])
S.append([[[0,0]],0])
S.append([[[0,0,1]],1])
S.append([[[0,1]],1])
S.append([[[1000,-1000,1000,1000]],0])
S.append([[[1000,-1000,1000,1000,1]],1])
S.append([[[-1000,1000]],2000])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()