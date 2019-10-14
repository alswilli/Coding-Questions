def shortestCellPath(grid, sr, sc, tr, tc):
	"""
	@param grid: int[][]
	@param sr: int
	@param sc: int
	@param tr: int
	@param tc: int
	@return: int
	"""  
  # First we should find the neighbors
  # 4 cases

  end = (tr, tc)
  bestCount = -1

  queue = []
  queue.append((sr, sc, 0))     
  visited = {}
  while len(queue) > 0:
    currentNode = queue[-1] #grabs last elem
    
    del queue[-1]
    arrayNum = currentNode[0]
    index = currentNode[1]
    step = currentNode[2]

    if currentNode == end:
      bestCount = max(bestCount, step)
      break

    neighbors = []
    neighbors.append((arrayNum + 1, index))
    neighbors.append((arrayNum - 1, index))
    neighbors.append((arrayNum, index + 1))
    neighbors.append((arrayNum, index - 1))

    # Find Neighbors and add to queue
    for (x, y) in neighbors:
      # Check if valid
      if (x < len(grid) - 1 and x >= 0) and (y < len(grid[0]) - 1 and y >= 0) and !(currentNode in visited):
        # Now add if neighbor is 1
        if grid[x][y] == 1:
          neighbors.append((x, y, step + 1))
          visited.append(currentNode)

  return bestCount