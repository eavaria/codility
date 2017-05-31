import unittest


def solution(H):
    blocks = 0
    S = set()
    for h in H:
        if h not in S:
            blocks += 1
        S = set(x for x in S if x <= h)
        S.add(h)
    return blocks
    
    
S=[]
S.append([[[8,8,5,7,9,8,7,4,8]],7])
S.append([[[2, 3, 2, 1]],3])

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()