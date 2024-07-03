import tkinter as tk
import random

# メインウィンドウを作成
window = tk.Tk()
window.title("まるばつゲーム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)

# フレームを作成し、メインウィンドウに配置
frame = tk.Frame(window, bg=bg_color)
frame.pack(expand=True, anchor='n')

# ボードの状態を保持するリスト
board = [["" for _ in range(3)] for _ in range(3)]

# 勝利条件をチェックする関数
def check_winner():
    # 行をチェック
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    
    # 列をチェック
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    # 対角線をチェック
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def button_action1():
    if board[0][0] == "":
        board[0][0] = "⚪︎"
        button1.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action2():
    if board[0][1] == "":
        board[0][1] = "⚪︎"
        button2.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action3():
    if board[0][2] == "":
        board[0][2] = "⚪︎"
        button3.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action4():
    if board[1][0] == "":
        board[1][0] = "⚪︎"
        button4.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action5():
    if board[1][1] == "":
        board[1][1] = "⚪︎"
        button5.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action6():
    if board[1][2] == "":
        board[1][2] = "⚪︎"
        button6.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action7():
    if board[2][0] == "":
        board[2][0] = "⚪︎"
        button7.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action8():
    if board[2][1] == "":
        board[2][1] = "⚪︎"
        button8.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

def button_action9():
    if board[2][2] == "":
        board[2][2] = "⚪︎"
        button9.config(text="⚪︎")
        winner = check_winner()
        if winner:
            label1.config(text=f"{winner}の勝ちです！", font=("Arial", 24))

button1 = tk.Button(frame, text="　", command=button_action1)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tk.Button(frame, text="　", command=button_action2)
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = tk.Button(frame, text="　", command=button_action3)
button3.grid(row=2, column=2, padx=10, pady=10)

button4 = tk.Button(frame, text="　", command=button_action4)
button4.grid(row=3, column=0, padx=10, pady=10)

button5 = tk.Button(frame, text="　", command=button_action5)
button5.grid(row=3, column=1, padx=10, pady=10)

button6 = tk.Button(frame, text="　", command=button_action6)
button6.grid(row=3, column=2, padx=10, pady=10)

button7 = tk.Button(frame, text="　", command=button_action7)
button7.grid(row=4, column=0, padx=10, pady=10)

button8 = tk.Button(frame, text="　", command=button_action8)
button8.grid(row=4, column=1, padx=10, pady=10)

button9 = tk.Button(frame, text="　", command=button_action9)
button9.grid(row=4, column=2, padx=10, pady=10)

# ラベルを作成し、3列にまたがるように配置
label2 = tk.Label(frame, text="あなたは⚪︎です", font=("Arial", 24), bg=bg_color, fg=fg_color)
label2.grid(row=0, column=0, columnspan=3, pady=10)

# リセットボタンを作成し、label2の下に配置
reset_button = tk.Button(frame, text="リセット", command=lambda: reset_game())
reset_button.grid(row=1, column=0, columnspan=3, pady=10)

# 状況表示ラベルを配置
label1 = tk.Label(frame, text="", bg=bg_color, fg=fg_color)
label1.grid(row=5, column=0, columnspan=3, pady=10)

# ゲームをリセットする関数
def reset_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
        button.config(text="　", state="normal")
    label1.config(text="")

# メインウィンドウのループ
window.mainloop()
