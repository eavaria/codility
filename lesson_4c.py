import unittest

def solution(A):
    S=set(filter(lambda x: x > 0, A))
    for i, s in enumerate(S):
        if (i+1 != s):
            return i + 1
    return len(S)+1
    

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