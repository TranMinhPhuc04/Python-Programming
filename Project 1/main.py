import tkinter as tk
from tkinter import messagebox, ttk
import math

# Hàm giải phương trình bậc 2
def giai_pt_bac_2():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Tính toán
        delta = b**2 - 4*a*c
        if delta > 0:
            nghiem_1 = (-b + math.sqrt(delta)) / (2 * a)
            nghiem_2 = (-b - math.sqrt(delta)) / (2 * a)
            ket_qua = f"Hai nghiệm phân biệt:\nx₁ = {nghiem_1:.2f}, x₂ = {nghiem_2:.2f}"
        elif delta == 0:
            nghiem_kep = -b / (2 * a)
            ket_qua = f"Nghiệm kép:\nx = {nghiem_kep:.2f}"
        else:
            phan_thuc = -b / (2 * a)
            phan_ao = math.sqrt(-delta) / (2 * a)
            ket_qua = (f"Nghiệm phức:\nx₁ = {phan_thuc:.2f} + {phan_ao:.2f}i, "
                       f"x₂ = {phan_thuc:.2f} - {phan_ao:.2f}i")
        
        label_ket_qua.config(text=ket_qua, fg="#333")
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập số hợp lệ cho các hệ số.")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi toán học", "Hệ số 'a' phải khác 0 trong phương trình bậc hai.")

# Hàm tính BMI
def tinh_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        
        # Phân loại BMI
        if bmi < 18.5:
            ket_qua_bmi = f"BMI = {bmi:.2f} (Gầy)"
        elif 18.5 <= bmi < 24.9:
            ket_qua_bmi = f"BMI = {bmi:.2f} (Bình thường)"
        elif 25 <= bmi < 29.9:
            ket_qua_bmi = f"BMI = {bmi:.2f} (Thừa cân)"
        else:
            ket_qua_bmi = f"BMI = {bmi:.2f} (Béo phì)"
        
        label_ket_qua_bmi.config(text=ket_qua_bmi, fg="#333")
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập số hợp lệ cho chiều cao và cân nặng.")

# Tạo cửa sổ
root = tk.Tk()
root.title("Ứng dụng đa chức năng")
root.geometry("500x450")

# Tạo thanh menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menu File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Mở")
file_menu.add_command(label="Lưu")
file_menu.add_command(label="Lưu dưới dạng")
file_menu.add_separator()
file_menu.add_command(label="Thoát", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Menu Edit
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Hoàn tác")
edit_menu.add_command(label="Cắt")
edit_menu.add_command(label="Sao chép")
edit_menu.add_command(label="Dán")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Menu View
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Thu nhỏ")
view_menu.add_command(label="Phóng to")
menu_bar.add_cascade(label="View", menu=view_menu)

# Menu Report
report_menu = tk.Menu(menu_bar, tearoff=0)
report_menu.add_command(label="Báo cáo hàng tháng")
report_menu.add_command(label="Báo cáo hàng năm")
report_menu.add_command(label="Xuất báo cáo")
menu_bar.add_cascade(label="Report", menu=report_menu)

# Menu Help
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hướng dẫn sử dụng")
help_menu.add_command(label="Thông tin ứng dụng")
menu_bar.add_cascade(label="Help", menu=help_menu)

# Tạo tab
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tab 1: Giải phương trình bậc 2
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Giải PT Bậc Hai")

frame_main = tk.Frame(tab1, bg="#FFFFFF", bd=5, relief="groove")
frame_main.place(relx=0.5, rely=0.5, anchor="center", width=380, height=330)

label_tieu_de = tk.Label(frame_main, text="Giải Phương Trình Bậc Hai", font=("Helvetica", 16, "bold"), bg="#FFFFFF", fg="#2d3436")
label_tieu_de.pack(pady=10)

def tao_o_nhap(frame, label_text):
    frame = tk.Frame(frame, bg="#FFFFFF")
    frame.pack(pady=5)
    label = tk.Label(frame, text=label_text, font=("Helvetica", 12), bg="#FFFFFF", fg="#2d3436")
    label.pack(side="left", padx=5)
    entry = tk.Entry(frame, font=("Helvetica", 12), width=15, bd=2, relief="solid")
    entry.pack(side="left", padx=5)
    return entry

entry_a = tao_o_nhap(frame_main, "Hệ số a:")
entry_b = tao_o_nhap(frame_main, "Hệ số b:")
entry_c = tao_o_nhap(frame_main, "Hệ số c:")

button_giai = tk.Button(frame_main, text="Giải", command=giai_pt_bac_2, bg="#0984e3", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=20, pady=5)
button_giai.pack(pady=10)

frame_ket_qua = tk.Frame(frame_main, bg="#FFFFFF")
frame_ket_qua.pack(pady=10)

label_ket_qua_title = tk.Label(frame_ket_qua, text="Kết quả:", font=("Helvetica", 12, "bold"), bg="#FFFFFF", fg="#2d3436")
label_ket_qua_title.pack(anchor="w")

label_ket_qua = tk.Label(frame_ket_qua, text="", font=("Helvetica", 12), bg="#FFFFFF", fg="#2d3436", justify="left")
label_ket_qua.pack(anchor="w")

# Tab 2: Tính chỉ số BMI
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tính BMI")

frame_bmi = tk.Frame(tab2, bg="#FFFFFF", bd=5, relief="groove")
frame_bmi.place(relx=0.5, rely=0.5, anchor="center", width=380, height=250)

label_bmi_title = tk.Label(frame_bmi, text="Tính chỉ số BMI", font=("Helvetica", 16, "bold"), bg="#FFFFFF", fg="#2d3436")
label_bmi_title.pack(pady=10)

entry_weight = tao_o_nhap(frame_bmi, "Cân nặng (kg):")
entry_height = tao_o_nhap(frame_bmi, "Chiều cao (cm):")

button_tinh_bmi = tk.Button(frame_bmi, text="Tính BMI", command=tinh_bmi, bg="#0984e3", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=20, pady=5)
button_tinh_bmi.pack(pady=10)

label_ket_qua_bmi = tk.Label(frame_bmi, text="", font=("Helvetica", 12), bg="#FFFFFF", fg="#2d3436")
label_ket_qua_bmi.pack(pady=10)

root.mainloop()
