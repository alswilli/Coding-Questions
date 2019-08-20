# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         # Step 1: Find the first letter
#         i = 0
#         boardRange = []
#         hashmap = {}
#         for array in board:
#             print(array)
#             for letter in array:
#                 print(letter)
#                 if word[i] == letter:
#                     boardRange.append(board.index(array))
#                     hashmap[letter] = [(board.index(array), array.index(letter))]
#                     i += 1
#                     if board.index(array) + 1 < len(array):
#                         boardRange.append(board.index(array) + 1)
#                     if board.index(array) - 1 > -1:
#                         boardRange.append(board.index(array) - 1)
#                     break
#             if len(boardRange) > 0:
#                 break
                    
#         print(boardRange)
#         # Step 2: check to see if all letters are possible from that point in board range. Add to range as needed
#         # Make sure to keep track of letter slots already in use via hash map
#         # Also update boardRange as needed
#         j = boardRange[0]
#         k = boardRange[len(boardRange)-1]
#         if j == k:
#             k += 1
#         while i < len(word):
#             # Search for word[i]
#             found = False
#             for array in board[j:k]:
#                 print(array)
#                 for letter in array:
#                     if word[i] == letter:
#                         # boardRange.append(board.index(array))
#                         if hashmap[letter] and (board.index(array), array.index(letter)) in hashmap[letter]:
#                             found = True
#                             val = hashmap[letter]
#                             if val is not None:
#                                 hashmap[letter] = hashmap[val, (board.index(array), array.index(letter))]
#                             else:
#                                 hashmap[letter] = [(board.index(array), array.index(letter))]
#                             i += 1
#                             if (board.index(array) + 1) < len(array) and (board.index(array) + 1) not in boardRange:
#                                 boardRange.append(board.index(array) + 1)
#                                 k += 1
#                             if (board.index(array) - 1) > -1 and (board.index(array) - 1) not in boardRange:
#                                 boardRange.append(board.index(array) - 1)
#                                 j -= 1
#                             break
#                 if found == True:
#                     break
#             if found == False:
#                 return False
        
#         return True
      
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        used = []
        for _ in range(rows):
            used.append([False] * cols)

        def search_around(row, col, char):
            if row < rows-1 and not used[row+1][col] and board[row+1][col] == char:
                yield row+1, col
            if col < cols-1 and not used[row][col+1] and board[row][col+1] == char:
                yield row, col+1
            if row > 0 and not used[row-1][col] and board[row-1][col] == char:
                yield row-1, col
            if col > 0 and not used[row][col-1] and board[row][col-1] == char:
                yield row, col-1

        def bt(i, last_row, last_col):
            if i == len(word):
                # All word matches
                return True

            for row, col in search_around(last_row, last_col, word[i]):
                used[row][col] = True
                if bt(i+1, row, col):
                    return True
                used[row][col] = False

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    used[row][col] = True
                    if bt(1, row, col) is True:
                        return True
                    used[row][col] = False

        return False