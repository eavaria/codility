import unittest

def solution(A):
    buff=[A[0],A[1]]
    m = 2147483647
    ix = 0
    last = 0
    for i, a in enumerate(A[2:]):
        s = sum(buff)
        cur_m = min(s/2., (s+a)/3.)
        if m > cur_m:
            m = cur_m
            ix = i
        buff[last] = a
        last = (last+1)%2
    if m > sum(A[-2:])/2.:
        return len(A)-2
    return ix

S=[]
S.append([[[4,2,2,5,1,5,8]],1])
S.append([[[-4, -1, -9, -11, -4]],2])
S.append([[[2,-5,4,2,-3,4,-7,8,-5,9,-3,-8,4,6,-7,-21]],14])




class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()