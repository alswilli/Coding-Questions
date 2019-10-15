def find_pairs_with_given_difference(arr, k):
  dict = {}
  output = []
  for i, val in enumerate(arr):
      #dict[k + val] = val
      dict[val - k] = val

  for j, val in enumerate(arr):
      if val in dict:
          output.append([dict[val], val])
          
  #output.sort(key = lambda x: x[1])
  return output