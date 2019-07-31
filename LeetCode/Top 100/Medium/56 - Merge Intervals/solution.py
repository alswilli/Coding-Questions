# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         i = 0
#         overlap = False
#         newStart = None
#         newEnd = None
#         # intervals.sort(key=operator.itemgetter(0))
#         intervals.sort(key=lambda x: x[0])
#         while i+1 < len(intervals):
#             # print(intervals)
#             # print(intervals[i])
#             # Assuming they come sorted by start time
#             currStart = intervals[i][0]
#             currEnd = intervals[i][1]
#             j = i + 1
#             nextStart = intervals[j][0]
#             nextEnd = intervals[j][1]
#             while currEnd >= nextStart and j < len(intervals):
#                 print("while")
#                 print(newStart)
#                 if newStart is None:
#                     overlap = True
#                     newStart = currStart
#                 newEnd = max(currEnd, nextEnd)
#                 # Adjust for next iteration
#                 if j < len(intervals):
#                     currStart = intervals[j][0]
#                     currEnd = intervals[j][1]
#                 j = j + 1
#                 if j < len(intervals):
#                     nextStart = intervals[j][0]
#                     nextEnd = intervals[j][1]
                
#             if overlap == True:
#                 print("overlap")
#                 del intervals[i:j]
#                 newInterval = [newStart, newEnd]
#                 intervals.insert(0, newInterval)
#                 print(intervals)
#                 # Reset vars
#                 overlap = False
#                 newStart = None
#                 newEnd = None
#             else:
#                 i += 1       
#         return intervals

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
            