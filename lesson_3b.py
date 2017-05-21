import unittest

def solution(X, Y, D):
   if ((Y-X)%D == 0):
      return (Y-X)/D
   else:
      return (Y-X)/D+1
        

S = []
S.append([[10,85,30], 3])
S.append([[1,1,1], 0])
S.append([[1,5,2], 2])
S.append([[1,4,2], 2])


class TestSolution(unittest.TestCase):
   def test_solution(self):
      for s in S: 
         self.assertEqual(solution(*s[0]), s[1])             

if __name__ == '__main__':
   unittest.main()
