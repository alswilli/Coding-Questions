def index_equals_value_search(arr):
  
  left = 0
  right = len(arr) 

  validIndex = -1
  while left <= right:
    #casue integer overflow -> mid = (left+right) / 2
    mid = left + (((right - left) / 2)) #mid = 1
    if mid > arr[mid]:
      # Update left
      left = mid+1
    elif mid < arr[mid]:
      right = mid-1
    else: #mid == arr(mid)
      validIndex = mid
      right = mid-1
  #Swap K group of nodes - leetcode hard
  #Reverse first k nodes - leetcode medium
  #Convert infix to postfix (c-a*b) -> ab*c-
  #codility.com
  #Min Deletions for Str Match
  #algoexpert.io, code: joma gets 15% off
  return validIndex
  
  Alex Williamson