import unittest
from collections import Counter

def solution(A):
    total = len(A)
    R = Counter(A)
    count = 0
    lead, r = R.most_common(1)[0]
    l = 0
    if ( r <= total/2 ):
        return 0
    for i, a in enumerate(A):
        if a == lead:
            l +=1
            r -=1
        if l > (i+1)/2 and r > (total-i-1)/2:
            count += 1        
    return count

S=[]
S.append([[[4,3,4,4,4,2]],2])
S.append([[[0,0]],1])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()