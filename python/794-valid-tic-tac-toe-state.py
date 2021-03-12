class Solution:
    def validTicTacToe(self, board):
        # counting 
        cnt = diag = anti = 0
        row, col = [0]*3, [0]*3
        mp = {"O": -1, " ": 0, "X": 1} # increment & decrement 
        for i in range(3):
            for j in range(3):
                x = mp[board[i][j]]
                cnt = cnt + x
                row[i] = row[i] + x
                col[j] = col[j] + x
                if i == j: 
                    diag += x
                if i+j == 2: 
                    anti += x
        # consequence 
        xwin = 3 in row or 3 in col or diag == 3 or anti == 3
        owin = -3 in row or -3 in col or diag == -3 or anti == -3
        if xwin and owin:
            return False
        if xwin and cnt != 1 or owin and cnt != 0: 
            return False 
        return 0 <= cnt <= 1

Solution.validTicTacToe(Solution, ["XXX", "O O", "OOX"])