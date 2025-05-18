import tkinter as tk
from tkinter import messagebox
import random
import time

# === Global Variables ===
data = []
stop_flag = False

# === Binary Search Algorithm with Visualization ===
def binary_search_visual(array, target):
    global stop_flag
    left, right = 0, len(array) - 1

    while left <= right and not stop_flag:
        mid = (left + right) // 2
        color_array = []

        for i in range(len(array)):
            if i == mid:
                color_array.append("yellow")
            elif i == left or i == right:
                color_array.append("blue")
            else:
                color_array.append("lightgray")

        draw_bars(array, color_array)
        time.sleep(0.6)
        window.update()

        if array[mid] == target:
            color_array[mid] = "green"
            draw_bars(array, color_array)
            messagebox.showinfo("Result", f"Found {target} at index {mid}")
            return
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    draw_bars(array, ["red"] * len(array))
    messagebox.showinfo("Result", f"{target} not found.")

# === Draw Bars ===
def draw_bars(array, color_array):
    canvas.delete("all")
    width = 800
    height = 300
    bar_width = width / len(array)
    max_val = max(array)

    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = height - (val / max_val * 250)
        x1 = (i + 1) * bar_width
        y1 = height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(val), font=("Segoe UI", 8))

# === Generate Sorted List ===
def generate_list():
    global data
    data = sorted(random.sample(range(10, 100), 20))
    draw_bars(data, ["lightgray"] * len(data))

# === Start Search ===
def start_search():
    global stop_flag
    stop_flag = False
    if not data:
        messagebox.showwarning("No Data", "Please generate a list first.")
        return
    try:
        target = int(entry.get())
        binary_search_visual(data, target)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# === Stop Search ===
def stop_search():
    global stop_flag
    stop_flag = True

# === GUI Setup ===
window = tk.Tk()
window.title("Binary Search Visualizer")
window.geometry("900x500")
window.config(bg="#1e1e2f")

canvas = tk.Canvas(window, width=800, height=300, bg="white", highlightthickness=0)
canvas.pack(pady=20)

controls = tk.Frame(window, bg="#1e1e2f")
controls.pack()

entry = tk.Entry(controls, width=10, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=10)

tk.Button(controls, text="Generate Sorted List", command=generate_list,
          bg="#0984e3", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

tk.Button(controls, text="Start Search", command=start_search,
          bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

tk.Button(controls, text="⏹ Stop", command=stop_search,
          bg="#d63031", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

window.mainloop()
