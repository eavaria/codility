import unittest

def solution(A):
    A.sort()
    for i, n in enumerate(A):
        if (i+1 != n):
            return i+1
    return len(A)+1
        

S = []
S.append([[[2,3,1,5]], 4])
S.append([[[2]], 1])
S.append([[[5,4,3,2]], 1])
S.append([[[1,2,3,4]], 5])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()