import unittest

def solution(A):
    A.sort(reverse=True)
    for a in A:
        print a
    return 1

S=[]
S.append([[[10,2,5,1,8,20]],1])


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()