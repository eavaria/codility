import unittest

def solution(S):
    if(len(S)%2 != 0):
        return 0
    L = []

    for s in S:
        if s == '(':
            L.append(s)
        elif s == ')':
            if len(L) == 0 or '(' != L.pop():
                return 0
        else:
            return 0
    if len(L) != 0:
        return 0
    else:
        return 1
    


S=[]
S.append([["(()(())())"],1])
S.append([["())"],0])




class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()