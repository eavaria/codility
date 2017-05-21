import unittest

def solution(A):  
    A.sort()
    while(True):
        a=A.pop()
        if len(A) == 0 or a != A.pop():
            return a
        

S = []
S.append([[[9,3,9,3,3,7,3]], 7])
S.append([[[0]], 0])
S.append([[[1,5,4,8,8,6,5,6,4]], 1])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()