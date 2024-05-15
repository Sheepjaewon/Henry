import tkinter as tk
import subprocess
import json
import os

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

def save_to_desktop():
    text = text_entry.get("1.0", tk.END)  # 사용자 입력 가져오기
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 바탕화면 경로
    file_path = os.path.join(desktop_path, "memo.json")  # 저장할 파일 경로
    
    # JSON 데이터 생성
    data = {"text": text.strip()}
    json_data = json.dumps(data)

    # 파일에 JSON 데이터 저장
    with open(file_path, "w") as file:
        file.write(json_data)
    
    print("Data saved to desktop.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Memo GUI")

# 초기 윈도우 크기 설정
root.geometry("600x400")

# 윈도우 크기 조절 가능하도록 설정
root.resizable(True, True)

# "메모장 열기" 버튼 생성
open_button = tk.Button(root, text="메모장 열기", command=open_notepad)
open_button.pack(pady=5)

# "저장" 버튼 생성
save_button = tk.Button(root, text="저장", command=save_to_notepad)
save_button.pack(pady=5)

# "불러오기" 버튼 생성
load_button = tk.Button(root, text="불러오기", command=load_from_notepad)
load_button.pack(pady=5)

# 파일 이름 입력 위젯 생성
file_name_entry = tk.Entry(root)
file_name_entry.pack(pady=5)

# 텍스트 입력 위젯 생성
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# "바탕화면에 저장" 버튼 생성
save_to_desktop_button = tk.Button(root, text="바탕화면에 저장", command=save_to_desktop)
save_to_desktop_button.pack(pady=5)

# 윈도우 실행
root.mainloop()
