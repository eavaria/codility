import unittest

def solution(S):
    if(len(S)%2 != 0):
        return 0
    L = []
    openings = set("[{(")
    closings = set("]})")
    d = {']':'[', '}':'{', ')':'('}
    for s in S:
        if s in openings:
            L.append(s)
        elif s in closings:
            if d[s] != L.pop():
                return 0                
    return 1
    


S=[]
S.append([["{[()()]}"],1])
S.append([["([)()]"],0])
S.append([[""],1])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()