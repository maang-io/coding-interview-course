#https://leetcode.com/problems/design-tic-tac-toe/description/

class TicTacToe(object):


    def __init__(self, n):
        """
        :type n: int
        """
        self.board=  [[0 for _ in range(n)] for _ in range(n)]
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.board)
        # place the player
        self.board[row][col] = player
        
        # now check if this player is winning or not

        # check the row
        count = 0
        for c in range(n):
            if self.board[row][c] == player:
                count+=1
        if count == n:
            return player

        #check the col
        count = 0
        for r in range(n):
            if self.board[r][col] == player:
                count+=1
        if count == n:
            return player

        # check the upward diagonal
        count = 0
        for i in range(n):
            if self.board[i][i] == player:
                count+=1
        if count == n:
            return player
            
        #check the downward diagonal
        count = 0
        for i in range(n):
            if self.board[i][n-1-i] == player:
                count+=1

        if count == n:
            return player

        return 0        
        




"""
Similar to above but using a single loop
"""
class TicTacToe(object):


    def __init__(self, n):
        """
        :type n: int
        """
        self.board=  [[0 for _ in range(n)] for _ in range(n)]
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.board)
        # place the player
        self.board[row][col] = player
        
        # now check if this player is winning or not
        rowCount = colCount = diagUpCount = diagDownCount = 0
        for i in range(n):
            if self.board[row][i] == player: # check the row
                rowCount+=1

            if self.board[i][col] == player: # check the row
                colCount+=1
        
            if self.board[i][i] == player:
                diagUpCount+=1

            if self.board[i][n-1-i] == player:
                diagDownCount+=1

        if rowCount == n or colCount == n or diagUpCount == n or diagDownCount == n:
            return player

        return 0        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)