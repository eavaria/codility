import unittest

def solution(A):
    A.sort()
    r = lambda n: reduce(lambda x,y: x*y, n)
    return max(r(A[-3:]), r(A[0:2]+[A[-1]]))
    


S=[]
S.append([[[-3,1,2,-2,5,6]],60])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()