import unittest

def solution(N,A):
    C = [0]*N
    min_count, max_count = 0, 0
    for a in A:
        if (a <= N):
            if (C[a-1] < min_count):
                C[a-1] = min_count + 1
            else:
                C[a-1] += 1
            if (C[a-1] > max_count):
                max_count = C[a-1]
        else:
            min_count = max_count
    return [c if c >= min_count else min_count for c in C]
    

S=[]
S.append([[5,[3,4,4,6,1,4,4]],[3, 2, 2, 4, 2]])
S.append([[2,[1,1,2,3,2,2,1]],[3, 4]])
S.append([[1,[1,1,2,1,1,2,1]],[5]])


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()