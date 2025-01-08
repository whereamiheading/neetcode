class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    print('rows')
                    return False
                elif item != '.':
                    s.add(item)

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    print('cols')
                    return False
                elif item != '.':
                    s.add(item)
        
        cell_idx = [ (0,0), (0,3) , (0, 6), 
                    (3,0), (3,3) , (3, 6),
                    (6,0), (6,3) , (6, 6),]

        for i, j in cell_idx:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        print('box')
                        return False
                    elif item != '.':
                        s.add(item)
        
        return True