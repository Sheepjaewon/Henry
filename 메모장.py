import tkinter as tk
import subprocess

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def save_to_notepad():
    text = text_entry.get("1.0", tk.END)  # 입력된 텍스트 가져오기
    file_name = file_name_entry.get()
    file_extension = file_name.split(".")[-1].lower()
    
    if file_extension == "txt":
        with open(file_name, "w") as file:
            file.write(text)
    elif file_extension == "html":
        with open(file_name, "w") as file:
            file.write("<html><body>\n")
            file.write(text)
            file.write("\n</body></html>")
    elif file_extension == "bat":
        with open(file_name, "w") as file:
            file.write("@echo off\n")
            file.write(text)
            
        subprocess.Popen([file_name])  # 생성한 배치 파일 실행
    else:
        print("지원되지 않는 확장자입니다.")

def load_from_notepad():
    try:
        file_name = file_name_entry.get()
        with open(file_name, "r") as file:
            text = file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", text)
    except FileNotFoundError:
        print(f"{file_name} 파일이 존재하지 않습니다.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Memo GUI")

# "메모장 열기" 버튼 생성
open_button = tk.Button(root, text="메모장 열기", command=open_notepad)
open_button.pack(pady=10)

# 파일 이름 입력 위젯 생성
file_name_entry = tk.Entry(root)
file_name_entry.pack(pady=5)

# 텍스트 입력 위젯 생성
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# "저장" 버튼 생성
save_button = tk.Button(root, text="저장", command=save_to_notepad)
save_button.pack(pady=5)

# "불러오기" 버튼 생성
load_button = tk.Button(root, text="불러오기", command=load_from_notepad)
load_button.pack(pady=5)

# 윈도우 실행
root.mainloop()
