import tkinter as tk
from tkinter import messagebox
import random

class 뽑기프로그램:
    def __init__(self, master):
        self.master = master
        self.master.title("뽑기 프로그램")

        self.label = tk.Label(master, text="뽑기 결과:", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="뽑기", command=self.뽑기)
        self.button.pack(pady=20)

    def 뽑기(self):
        # 1부터 100 사이의 무작위 숫자 뽑기 (원하는 범위로 수정 가능)
        뽑힌숫자 = random.randint(1, 32)

        # 결과를 메시지 박스로 표시
        messagebox.showinfo("뽑기 결과", f"뽑힌 숫자: {뽑힌숫자}")
        # 결과를 라벨에도 표시
        self.label.config(text=f"뽑기 결과: {뽑힌숫자}")

if __name__ == "__main__":
    root = tk.Tk()
    app = 뽑기프로그램(root)
    root.mainloop()
