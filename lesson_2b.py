import unittest

def solution(A, K):
    O=[]
    N = len(A)
    for n in range(N-K,2*N-K):
        O.append(A[(n)%N])
    return O
        

S = []
S.append([[[3, 8, 9, 7, 6],2], [7, 6, 3, 8, 9]])
S.append([[[1],5], [1]])
S.append([[[1,2,3],5], [2,3,1]])
S.append([[[1,2,3],6], [1,2,3]])


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()