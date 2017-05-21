import unittest

def solution(X,A):
    S = set()
    for i, a in enumerate(A):
        if (a <= X):
            S.add(a)
        if (len(S) == X):
            return i
    return -1
    

S=[]
S.append([[5, [1,3,1,4,2,3,5,4]],6])
S.append([[1, [1]],0])
S.append([[2, [1]],-1])
S.append([[2, [1,1,1,1]],-1])


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()