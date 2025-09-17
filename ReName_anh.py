import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_input_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder.set(folder)

def rename_files():
    in_folder = input_folder.get()
    out_folder = output_folder.get()

    if not in_folder or not out_folder:
        messagebox.showerror("Lỗi", "Vui lòng chọn thư mục đầu vào và thư mục lưu!")
        return

    try:
        for filename in os.listdir(in_folder):
            old_path = os.path.join(in_folder, filename)

            # Bỏ qua thư mục, chỉ xử lý file
            if not os.path.isfile(old_path):
                continue

            # Lấy tên mới (loại bỏ từ _AnhThe trở đi)
            name, ext = os.path.splitext(filename)
            new_name = name.split("_AnhThe")[0] + ext

            new_path = os.path.join(out_folder, new_name)

            # Copy sang thư mục đích với tên mới
            shutil.copy2(old_path, new_path)

        messagebox.showinfo("Thành công", "Đổi tên và sao chép file thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# GUI
root = tk.Tk()
root.title("Đổi tên file ảnh")

input_folder = tk.StringVar()
output_folder = tk.StringVar()

tk.Label(root, text="Thư mục chứa file ảnh:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=input_folder, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Chọn...", command=select_input_folder).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Thư mục lưu file mới:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=output_folder, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Chọn...", command=select_output_folder).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Đổi tên và Lưu", command=rename_files, bg="lightblue").grid(row=2, column=1, pady=20)

root.mainloop()
