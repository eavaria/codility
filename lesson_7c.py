import unittest

def solution(A,B):
    F = zip(B,A)
    S = []
    count = 0
    for f in F:
        if(f[0] == 1):
            S.append(f[1])     
        elif(len(S) == 0):
                count += 1
        else:
            while(len(S) > 0):
                if(S[-1] < f[1]):
                    S.pop()
                else:
                    count +=1
                    break
    return count + len(S)
    
S=[]
S.append([[[4,3,2,1,5],[0,1,0,0,0,0]],2])



class TestSolution(unittest.TestCase):
    def test_solution(self):
        for s in S: 
            self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
    unittest.main()