import os
import subprocess
import win32file
import tkinter as tk
from tkinter import messagebox

def check_mounted_drives():
    drives = []
    for drive in range(ord("A"), ord("Z") + 1):
        drive_letter = chr(drive)
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            drives.append(drive_path)
    return drives

def is_removable_drive(drive):
    drive_type = win32file.GetDriveType(drive)
    return drive_type == win32file.DRIVE_REMOVABLE

def block_drive_access(drive):
    messagebox.showwarning("USB Blocker", f"Terminal is unavailable! Please remove the {drive} drive.")
    subprocess.call(["mountvol", drive, "/P"])

def handle_block_request():
    selected_drive_type = drive_type_var.get()
    
    if selected_drive_type == "USB":
        drives = [drive for drive in check_mounted_drives() if is_removable_drive(drive)]
    elif selected_drive_type == "DVD/CD":
        drives = [drive for drive in check_mounted_drives() if not is_removable_drive(drive)]
    else:
        drives = check_mounted_drives()
    
    if drives:
        for drive in drives:
            block_drive_access(drive)
    else:
        messagebox.showinfo("USB Blocker", "No drives found to block.")

def show_about_page():
    clear_content()
    title_label.config(text="Teşekkürler")
    drive_type_label.config(text= "Bu bir açık kaynaklı yazılımdır ve gelişime daha da çok açıktır.\n\nGitHub: https://github.com/ugurcomptech\n\nTeşekkürler!")
    drive_type_menu.forget()
def show_main_page():
    clear_content()
    title_label.config(text="Welcome to USB Blocker")
    drive_type_label.config(text="Select drive type:")
    drive_type_menu.pack()  # USB ve DVD seçimi menüsünü görünür hale getiriyoruz
    block_button.config(text="Block")
    block_button.pack(pady=30)

def show_other_block_page():
    clear_content()
    title_label.config(text="Other Blocker Page")
    drive_type_label.config(text= "Klavye, mouse, printer, ağ kartı, harici diskler ve daha fazlasını \n engellemek çalışıyoruz. Bize destek olmak için bu yazılımı geliştirmemize \n yardımcı olunuz. \n \n Teşekkürler!")
    drive_type_menu.forget()

def clear_content():
    title_label.config(text="")
    drive_type_label.config(text="")
    block_button.pack_forget()

window = tk.Tk()
window.title("USB Blocker")
window.geometry("700x325")
window.resizable(False, False)


# Icon
window.iconbitmap("usb.ico")  # İcon dosyasının yolu


# Navbar
navbar_frame = tk.Frame(window, bg="#333")
navbar_frame.pack(fill="x")

navbar_label = tk.Label(navbar_frame, text="USB Blocker", font=("Arial", 16), bg="#333", fg="white")
navbar_label.pack(side="left", padx=10, pady=5)

# Main Content
title_label = tk.Label(window, text="Welcome to USB Blocker", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

drive_type_var = tk.StringVar()
drive_type_var.set("USB")

drive_type_label = tk.Label(window, text="Select drive type:", font=("Arial", 14))
drive_type_label.pack()

drive_type_menu = tk.OptionMenu(window, drive_type_var, "USB", "DVD/CD", "All")
drive_type_menu.config(font=("Arial", 12))
drive_type_menu.pack()

block_button = tk.Button(window, text="Block", font=("Arial", 14), command=handle_block_request, bg="red", fg="white")
block_button.pack(pady=30)



usb_block_button = tk.Button(navbar_frame, text="USB Block", font=("Arial", 12), bg="#333", fg="white", bd=0, command=show_main_page)
usb_block_button.pack(side="left", padx=10, pady=5)

other_block_button = tk.Button(navbar_frame, text="Other Block", font=("Arial", 12), bg="#333", fg="white", bd=0, command=show_other_block_page)
other_block_button.pack(side="left", padx=10, pady=5)

about_menu_button = tk.Button(navbar_frame, text="About", font=("Arial", 12), bg="#333", fg="white", bd=0, command=show_about_page)
about_menu_button.pack(side="right", padx=10, pady=5)

window.mainloop()
