import unittest

def solution(N):
    max_count = 0
    count = 0
    inside = False
    while(N != 0):
        if (N & 1 == 0 and inside):
            count += 1
        elif (N & 1 == 1):
            inside = True
            count = 0
        if count > max_count:
            max_count = count
        N = N >> 1
    return max_count

S = []
S.append([[9], 2])
S.append([[529], 4])
S.append([[1041], 5])
S.append([[51712], 2])  

class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()