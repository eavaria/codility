import unittest

def solution(A,B,K):
    first_offset = A%K
    last_offset = (B+1)%K
    if (first_offset != 0):
        first = A + K - first_offset
    else:
        first = A
    if(last_offset == 0):
        return (B+1-first)/K
    else:
        return (B+1-first)/K+1
   

S=[]
S.append([[6,11,2],3])
S.append([[11,345,17],20])
S.append([[1,9999999,2],4999999])
S.append([[1,9999999,99999],100])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()