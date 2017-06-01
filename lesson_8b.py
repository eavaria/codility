import unittest
from collections import Counter

def solution(A):    
    total = len(A)
    if total == 0:
        return -1
    R = Counter(A)
    lead, r = R.most_common(1)[0]
    if ( r <= total/2 ):
        return -1
    return A.index(lead)

S=[]
S.append([[[3,4,3,2,3,-1,3,3]],3])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()