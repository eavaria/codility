import unittest

def solution(A):
    if (len(A) < 3):
        return 0    
    A.sort()
    buff = [A.pop(),A.pop(),A.pop()]
    ix = 0
    while True:
        if buff[ix] < buff[(ix+1)%3] + buff[(ix+2)%3]:
            return 1
        elif (len(A) == 0):
            return 0
        else:
            buff[ix] = A.pop()
            ix = (ix+1)%3

S=[]
S.append([[[10,50,5,1]],0])
S.append([[[10,2,5,1,8,20]],1])
S.append([[[5,3,3]],1])
S.append([[[2,5,6,7,4,5,5,3,3]],1])
S.append([[[2,2,2,2,2,2,2,2,2]],1])
S.append([[[]],0])
S.append([[[1]],0])
S.append([[[1,1]],0])
S.append([[[1,1,1]],1])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()