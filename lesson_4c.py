import unittest

def solution(A):
    S=set(filter(lambda x: x > 0, A))
    L = list(S)
    L.sort()
    for i, l in enumerate(L):
        if (i+1 != l):
            return i + 1
    return len(L)+1
    

S=[]
S.append([[[1,3,1,4,2,3,5,4]],6])
S.append([[[1,3,1,6,2,4]],5])
S.append([[[5]],1])
S.append([[[1,2,1,6,9]],3])
S.append([[[1,2,-1,6,9]],3])
S.append([[[-1000,1,2,-1,6,9]],3])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()