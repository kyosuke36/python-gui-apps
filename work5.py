import tkinter as tk
import random
# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

str_list = ["昨日は雨","今日はいい天気"]
num = random.randint(0,len(str_list)-1)

def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    global num # numをグローバル変数として宣言
    user_input = entry1.get()  # 入力値を取得
    if user_input == str_list[num]:
        num = random.randint(0,len(str_list)-1)
        label.config(text=str_list[num])  # ラベルを更新
        entry1.delete(0, tk.END)  # 入力フィールドをクリア
    else:
        pass
   


# 入力フィールドの作成
label = tk.Label(window,text=str_list[num], bg=fg_color, fg=bg_color)
label.pack()

entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="決定", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
