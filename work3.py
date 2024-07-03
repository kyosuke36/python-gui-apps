import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

name_list = []
def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    name_list.append(entry1.get())
    name_out = ""
    for i in name_list:
        name_out+=f"{i}\n"
    label1.config(text=f"{name_out}\n")  # 画面に出力
# user_input = entry1.get()
# name_list.append(user_input)
# formatted_str = ""
# for name in mame list:
#     formatted_str += "\n".join(name_list)
#     label1.config(text=formatted_str)

# 入力フィールドの作成
label = tk.Label(window,text="名前を入力してください", bg=fg_color, fg=bg_color)
label.pack()

entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
