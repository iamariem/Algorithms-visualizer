import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        draw_table(fib_table, "lightgray")
        time.sleep(0.5)  # Control speed of visualization
        
    return fib_table[n]

# === Knapsack Algorithm with Dynamic Programming Visualization ===
def knapsack(weights, values, capacity):
    global stop_flag
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build dp table for knapsack
    for i in range(n + 1):
        for w in range(capacity + 1):
            if stop_flag:
                return
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
            draw_knapsack_table(dp, n, capacity)
            time.sleep(0.5)

    return dp[n][capacity]

# === Draw Table (For Both Fibonacci and Knapsack) ===
def draw_table(table, color):
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
        color_choice = color if val != table[-1] else "green"  # Highlight last value in green
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_choice, outline="")
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(val), font=("Segoe UI", 8))

# === Draw Knapsack DP Table Visualization ===
def draw_knapsack_table(dp, n, capacity):
    canvas.delete("all")
    width = 800
    height = 300
    bar_width = width / (capacity + 1)
    for i in range(n + 1):
        for j in range(capacity + 1):
            x0 = j * bar_width
            y0 = height - (dp[i][j] / 10)  # Scale values to fit on the canvas
            x1 = (j + 1) * bar_width
            y1 = height
            color = "lightgray" if i != n else "blue"
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
            canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(dp[i][j]), font=("Segoe UI", 8))

# === Start Algorithm Calculation ===
def start_algorithm():
    global stop_flag
    stop_flag = False
    try:
        if algo_choice.get() == "Fibonacci":
            n = int(entry.get())
            if n <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive integer.")
                return
            fibonacci(n)
        elif algo_choice.get() == "Knapsack":
            weights = list(map(int, weight_entry.get().split(',')))
            values = list(map(int, value_entry.get().split(',')))
            capacity = int(capacity_entry.get())
            if capacity <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive capacity.")
                return
            knapsack(weights, values, capacity)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")

# === Stop Algorithm Calculation ===
def stop_algorithm():
    global stop_flag
    stop_flag = True

# === GUI Setup ===
window = tk.Tk()
window.title("Dynamic Programming Visualizer")
window.geometry("900x500")
window.config(bg="#1e1e2f")

canvas = tk.Canvas(window, width=800, height=300, bg="white", highlightthickness=0)
canvas.pack(pady=20)

controls = tk.Frame(window, bg="#1e1e2f")
controls.pack()

# === Dropdown for Algorithm Selection ===
algo_choice = tk.StringVar()
algo_menu = ttk.Combobox(controls, textvariable=algo_choice, state="readonly")
algo_menu['values'] = ("Fibonacci", "Knapsack")
algo_menu.set("Choose Algorithm")
algo_menu.pack(side=tk.LEFT, padx=10)

# === Fibonacci UI ===
entry = tk.Entry(controls, width=10, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=10)

# === Knapsack UI ===
weight_label = tk.Label(controls, text="Enter Weights (comma separated):", bg="#1e1e2f", fg="white")
weight_label.pack(side=tk.LEFT, padx=10)
weight_entry = tk.Entry(controls, font=("Segoe UI", 10))
weight_entry.pack(side=tk.LEFT, padx=10)

value_label = tk.Label(controls, text="Enter Values (comma separated):", bg="#1e1e2f", fg="white")
value_label.pack(side=tk.LEFT, padx=10)
value_entry = tk.Entry(controls, font=("Segoe UI", 10))
value_entry.pack(side=tk.LEFT, padx=10)

capacity_label = tk.Label(controls, text="Enter Capacity:", bg="#1e1e2f", fg="white")
capacity_label.pack(side=tk.LEFT, padx=10)
capacity_entry = tk.Entry(controls, font=("Segoe UI", 10))
capacity_entry.pack(side=tk.LEFT, padx=10)

# === Buttons ===
tk.Button(controls, text="Start Algorithm", command=start_algorithm,
          bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

tk.Button(controls, text="⏹ Stop", command=stop_algorithm,
          bg="#d63031", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

window.mainloop()
