import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get()) # 入力値を取得
    # 1868 明治
    # 1912 大正
    # 1926 昭和
    # 1989 平成
    # 2019 令和
    if 1912 > seireki:
        gengo = "明治"
        wareki = seireki - 1868 + 1 
    elif 1926 > seireki:
        gengo = "大正"
        wareki = seireki - 1912 + 1
    elif 1989 > seireki:
        gengo = "昭和"
        wareki = seireki - 1926 + 1
    elif 2019 > seireki:
        gengo = "平成"
        wareki = seireki - 1989 + 1
    else :
        gengo = "令和"
        wareki = seireki - 2019 + 1

    if wareki == 1:
        wareki = "元"                
        label1.config(text=f"西暦{seireki}年は{gengo}{wareki}年です")  # 画面に出力qaz




# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="Submit", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
