import unittest

def solution(A):
    A.sort()
    for i, a in enumerate(A):
        if (i+1 != a):
            return 0
    return 1
    
S=[]
S.append([[[4,1,3,2]],1])
S.append([[[4,1,2,2]],0])
S.append([[[4,1,2]],0])
S.append([[[3,1,2]],1])
S.append([[[3,4,2,5]],0])
S.append([[[1]],1])
S.append([[[1,1]],0])
S.append([[[2]],0])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()