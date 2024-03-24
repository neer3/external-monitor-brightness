import tkinter as tk
from tkinter import ttk
import subprocess

def execute_command(event=None):
    try:
        selected_number = int(number_entry.get())
        if selected_number < 1 or selected_number > 100:
            raise ValueError("Number must be between 1 and 100")
        command_to_execute = f'ddcutil setvcp 10 {selected_number} --display 1'

        splash_screen = tk.Toplevel(root)
        splash_screen.title("Splash Screen")
        splash_label = tk.Label(splash_screen, text="Executing command...", padx=20, pady=10)
        splash_label.pack()
        
        splash_screen.lift()
        splash_screen.update()
        
        subprocess.run(command_to_execute, shell=True, check=True)
    except ValueError as ve:
        tk.messagebox.showerror("Error", str(ve))
    except subprocess.CalledProcessError as e:
        tk.messagebox.showerror("Error", f"Command execution failed: {e}")
    finally:
        splash_screen.destroy()

root = tk.Tk()
root.title("Number Selector")
root.geometry("400x200")

number_entry = ttk.Entry(root)
number_entry.pack(pady=10)
number_entry.bind("<Return>", execute_command)

execute_button = ttk.Button(root, text="Execute Command", command=execute_command)
execute_button.pack(pady=5)

root.mainloop()
