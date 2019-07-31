# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         i = 0
#         j = 0
#         print('a')
#         print(people)
#         print()
#         for pair in people:
#             myH = people[i][0]
#             myK = people[i][1]
#             if i < myK:
#                 # Swap to min location, but check if already contains a min
#                 if people[myK][1] < myK:
#                     # self.swap(people, people[myK][1], myK)
#                     self.swap(people, people.index(people[myK]), i)
#                     print('b')
#                     print(people[myK])
#                     print(people[i])
#                     print(people)
#                     print()
#                 else:
#                     k = myK + 1
#                     while k < len(people):
#                         if people[k][1] < myK:
#                             # self.swap(people, people[k][1], myK)
#                             self.swap(people, people.index(people[k]), i)
#                             print('c')
#                             print(people)
#                             print()
#             j -= 1
#             firstSwap = None
#             k = myK
#             tempI = i
#             while j != -1:
#                 prevH = people[j][0]
#                 prevK = people[j][1]
#                 if prevH >= myH:
#                     k -= 1
#                     if firstSwap == None:
#                         firstSwap = people.index(people[j])
#                 # else:
#                 print(k)
#                 if k < 0:
#                     self.swap(people, firstSwap, people.index(people[tempI]))
#                     tempI = firstSwap
#                     k = myK
#                     print('d')
#                     print(people)
#                     print(j)
#                     print()
#                     j = tempI
#                     print(j)
#                     print(k)
#                     print()
#                     firstSwap = None
#                 j -= 1      
#             i += 1
#             j = i
#         return people
        
        
#     def swap(self, people, i, j):
#         temp = people[i]
#         people[i] = people[j]
#         people[j] = temp
#         return people

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
      # O(n*logn) time for sortting
      ordered = sorted(people, key=operator.itemgetter(0, 1))
      N = len(people)
      ans = [None for i in range(N)]
      for p, m in ordered: # this loop takes worst case O(n^2)
        m_ = m
        for i in range(N):
          if not ans[i] or ans[i][0] >= p:
            m -= 1
          if m < 0:
            break
        ans[i] = [p, m_]
      return ans