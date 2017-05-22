import unittest

def solution(S,P,Q):
    Z = zip(P,Q)
    Zs = set(Z)
    Zd = dict.fromkeys(Zs, 4)
    for z in Zs:
        if 'A' in S[z[0]:z[1]+1]:
            Zd[z] = 1
        elif 'C' in S[z[0]:z[1]+1]:
            Zd[z] = 2
        elif 'G' in S[z[0]:z[1]+1]:
            Zd[z] = 3
    ret = []
    for z in Z:
        ret.append(Zd[z]) 
    return ret

S=[]
S.append([[['C','A','G','C','C','T','A'],[2,5,0],[4,5,6]],[2,4,1]])
S.append([[['C','A','G','C','C','T','A'],[2,5,0,0,5],[4,5,6,6,5]],[2,4,1,1,4]])
S.append([[['C','A','G','C','C','T','A'],[2,5,0,0,5,2,5,0,0,5,2,5,0,0,5,2,5,0,0,5],[4,5,6,6,5,4,5,6,6,5,4,5,6,6,5,4,5,6,6,5]],[2,4,1,1,4,2,4,1,1,4,2,4,1,1,4,2,4,1,1,4]])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()