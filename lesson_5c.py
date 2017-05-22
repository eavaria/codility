import unittest

def solution(S,P,Q):
    F = {'A':1, 'C':2, 'G':3, 'T':4}
    ret = [4]*len(P)
    Z = zip(P,Q)
    print Z
    T = [[0]*len(P) for _ in range(len(S))]
    for i, z in enumerate(Z):
        for r in range(z[0],z[1]+1):
            T[r][i] = 1
    print T
    for i, s in enumerate(S):
        print str(i) + " " + str(s)
    return [2,4,1]
   

S=[]
S.append([[['C','A','G','C','C','T','A'],[2,5,0],[4,5,6]],[2,4,1]])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()