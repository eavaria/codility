import unittest

def solution(A):
    return len(set(A))

S=[]
S.append([[[2,1,1,2,3,1]],3])


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()