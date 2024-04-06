import tkinter as tk
from tkinter import ttk
import subprocess

def execute_command():
    try:
        root_password = password_entry.get()
        selected_brightness = int(brightness_entry.get())
        selected_contrast = int(contrast_entry.get())

        if selected_brightness < 1 or selected_brightness > 100 or selected_contrast < 0 or selected_contrast > 100:
            raise ValueError("Brightness must be between 1 and 100, and contrast between 0 and 100")
        
        brightness_command = f'echo "{root_password}" | sudo -S ddcutil setvcp 10 {selected_brightness} --display 1'
        contrast_command = f'echo "{root_password}" | sudo -S ddcutil setvcp 12 {selected_contrast} --display 1'

        splash_screen = tk.Toplevel(root)
        splash_screen.title("Splash Screen")
        splash_label = tk.Label(splash_screen, text="Executing command...", padx=20, pady=10)
        splash_label.pack()
        
        splash_screen.lift()
        splash_screen.update()
        
        subprocess.run(brightness_command, shell=True, check=True)
        subprocess.run(contrast_command, shell=True, check=True)
    except ValueError as ve:
        tk.messagebox.showerror("Error", str(ve))
    except subprocess.CalledProcessError as e:
        tk.messagebox.showerror("Error", f"Command execution failed: {e}")
    finally:
        splash_screen.destroy()

        # Hide only the password section after execution
        password_label.pack_forget()
        password_entry.pack_forget()

root = tk.Tk()
root.title("Monitor Settings Control")
root.geometry("400x250")

password_label = ttk.Label(root, text="Enter root password:")
password_label.pack(pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=5)

brightness_label = ttk.Label(root, text="Enter brightness (1-100):")
brightness_label.pack(pady=5)

brightness_entry = ttk.Entry(root)
brightness_entry.pack(pady=5)

contrast_label = ttk.Label(root, text="Enter contrast (0-100):")
contrast_label.pack(pady=5)

contrast_entry = ttk.Entry(root)
contrast_entry.pack(pady=5)

execute_button = ttk.Button(root, text="Apply Settings", command=execute_command)
execute_button.pack(pady=5)

root.mainloop()
