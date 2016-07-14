"""
依次遍历行、列、单元格

核心算法 is_valid ，利用了python的set，方便查找 i 是否在 set 里
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        
        def is_valid(arr):
            s = set()
            for i in arr:
                if i == '.':
                    continue
                if i not in s:
                    s.add(i)
                else:
                    return False
            return True

        def is_row_valid(row, board):
            return is_valid([board[row][j] for j in xrange(9)])

        def is_col_valid(col, board):
            return is_valid([board[i][col] for i in xrange(9)])

        def is_block_valid(row, col, board):
            return is_valid([board[r][c] \
                             for r in xrange(row * 3, (row + 1) * 3) \
                             for c in xrange(col * 3, (col + 1) * 3)])

        for i in xrange(9):
            if not is_row_valid(i, board):
                return False
            if not is_col_valid(i, board):
                return False

        for i in xrange(3):
            for j in xrange(3):
                if not is_block_valid(i, j, board):
                    return False

        return True


# test
print Solution().isValidSudoku([[5,3,'.','.',7,'.','.','.','.'],
                                [6,'.','.',1,9,5,'.','.','.'],
                                ['.',9,8,'.','.','.','.',6,'.'],
                                [8,'.','.','.',6,'.','.','.',3],
                                [4,'.','.',8,'.',3,'.','.',1],
                                [7,'.','.','.',2,'.','.','.',6],
                                ['.',6,'.','.','.','.',2,8,'.'],
                                ['.','.','.',4,1,9,'.','.',5],
                                ['.','.','.','.',8,'.','.',7,9]])
