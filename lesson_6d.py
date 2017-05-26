import unittest

def solution(A):
    S=[0]*len(A)
    for i, a in enumerate(A):
        S[max(0,i-a)] += 1
    def accumu(lis):
        total = 0
        for x in lis:
            total += x
            yield total
    S = list(accumu(S))
    count = 0
    for i in range(len(S)):
        count += S[min(len(A)-1,i+A[i])] - (i+1)
        if count > 10000000:
            return -1
    return count
    


S=[]
S.append([[[1,5,2,1,4,0]],11])
S.append([[[]],0])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()