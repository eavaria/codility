import unittest

def solution(H):
    S=[]
    count = 0
    for h in H:
        while(len(S) > 0 and h < S[-1]):
            S.pop()
        if len(S) == 0 or h != S[-1]:
            S.append(h)
            count += 1
    return count

S=[]
S.append([[[8,8,5,7,9,8,7,4,8]],7])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()