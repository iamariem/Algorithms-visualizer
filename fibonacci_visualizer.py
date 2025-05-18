import tkinter as tk
from tkinter import messagebox
import time

# === Global Variables ===
fib_table = []
stop_flag = False

# === Fibonacci Algorithm with Dynamic Programming Visualization ===
def fibonacci(n):
    global stop_flag
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    
    for i in range(2, n + 1):
        if stop_flag:
            return
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        draw_fib_table(fib_table)
        time.sleep(0.5)  # Control speed of visualization
        
    return fib_table[n]

# === Draw Fibonacci Table ===
def draw_fib_table(table):
    canvas.delete("all")
    width = 800
    height = 300
    bar_width = width / len(table)
    max_val = max(table)

    for i, val in enumerate(table):
        x0 = i * bar_width
        y0 = height - (val / max_val * 250)
        x1 = (i + 1) * bar_width
        y1 = height
        color = "lightgray" if val != table[-1] else "green"  # Last value is highlighted in green
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(val), font=("Segoe UI", 8))

# === Start Fibonacci Calculation ===
def start_fibonacci():
    global stop_flag
    stop_flag = False
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")
            return
        fibonacci(n)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# === Stop Fibonacci Calculation ===
def stop_fibonacci():
    global stop_flag
    stop_flag = True

# === GUI Setup ===
window = tk.Tk()
window.title("Fibonacci Visualizer")
window.geometry("900x500")
window.config(bg="#1e1e2f")

canvas = tk.Canvas(window, width=800, height=300, bg="white", highlightthickness=0)
canvas.pack(pady=20)

controls = tk.Frame(window, bg="#1e1e2f")
controls.pack()

entry = tk.Entry(controls, width=10, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=10)

tk.Button(controls, text="Start Fibonacci", command=start_fibonacci,
          bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

tk.Button(controls, text="⏹ Stop", command=stop_fibonacci,
          bg="#d63031", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

window.mainloop()
