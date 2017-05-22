import unittest

def solution(A):
    EAST = 0
    WEST = 1
    count = 0
    inc = 1
    for i, a in enumerate(A):
        if(a == EAST):
            break
    for a in A[i+1:]:
        if a == WEST:
            count +=inc
        else:
            inc += 1      
    if (count > 1000000000):
        return -1
    return count
   

S=[]
S.append([[[0,1,0,1,1]],5])
S.append([[[0,1,0,1,1,0]],5])
S.append([[[0,1]],1])
S.append([[[0,0]],0])
S.append([[[1,1]],0])
S.append([[[1,0]],0])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()