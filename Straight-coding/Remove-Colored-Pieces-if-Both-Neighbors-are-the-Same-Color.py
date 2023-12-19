class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        def removeColor(color, colors):
            N = len(colors)
            result = []
            for i in range(0,N):
                if i >= 1 and i < N-1 and colors[i] == color and colors[i-1] == color and colors[i+1] == color:
                    nc = colors[0:i-1]+colors[i:]
                    return nc
        
            return colors
        # 1:A, -1:B
        player = 'A' # Alice starts the game
        while True:
            n = len(colors)
            colors = removeColor(player, colors)
            player = 'B' if player == 'A' else 'A'
            if len(colors) == n: # game is over
                break
        
        return True if player == 'A' else False


class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        def tripletCounter(color):
            N = len(colors)
            count = 0
            for i in range(0,N):
                if i >= 1 and i < N-1 and colors[i] == color and colors[i-1] == color and colors[i+1] == color:
                    count+=1
        
            return count
        # 1:A, -1:B
        aaaCount = tripletCounter('A')
        bbbCount = tripletCounter('B')
      
        return True if aaaCount > bbbCount else False



class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        N = len(colors)
        aCount = 0
        for i in range(1,N-1):
            if  colors[i] == 'A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                aCount+=1
            if  colors[i] == 'B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                aCount -=1        
      
        return True if aCount > 0 else False
