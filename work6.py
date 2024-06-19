import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("まるばつゲーム")
        
        # ボタンのリスト
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        # ボタンを作成し、グリッドに配置
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=("Arial", 60), width=5, height=2, command=lambda row=i, col=j: self.player_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        # ゲーム終了フラグ
        self.game_over = False

    def player_move(self, row, col):
        if not self.game_over and self.board[row][col] is None:
            self.buttons[row][col].config(text="○")
            self.board[row][col] = "O"
            if self.check_winner("O"):
                self.show_winner("○の勝ちです！")
                return
            self.computer_move()
            if self.check_winner("X"):
                self.show_winner("×の勝ちです！")

    def computer_move(self):
        # NPCの動きを実装する
        best_move = None
        best_score = -float('inf')

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = "X"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = None
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            row, col = best_move
            self.buttons[row][col].config(text="×")
            self.board[row][col] = "X"

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": 1, "O": -1, "Tie": 0}
        
        result = self.check_winner_minimax(board)
        if result:
            return scores[result]
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = None
                        best_score = min(score, best_score)
            return best_score

    def check_winner_minimax(self, board):
        # 横、縦、斜めのいずれかがすべて同じプレイヤーなら勝ち
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]
        
        # 引き分け
        if all(board[i][j] is not None for i in range(3) for j in range(3)):
            return "Tie"
        
        return None

    def check_winner(self, player):
        # 横、縦、斜めのいずれかがすべて同じプレイヤーなら勝ち
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False
    
    def show_winner(self, message):
        self.game_over = True
        winner_label = tk.Label(self.root, text=message, font=("Arial", 24))
        winner_label.grid(row=3, column=0, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
