import tkinter as tk
from tkinter import ttk
import random
import time

# ==== Global Variables ====
data = []
stop_flag = False

# ==== GUI Setup ====
root = tk.Tk()
root.title("AlgoVisual | Sorting Playground")
root.geometry("900x600")
root.config(bg="#1e1e2f")

canvas = tk.Canvas(root, width=800, height=300, bg="white", highlightthickness=0)
canvas.pack(pady=20)

# ==== Draw Bars Function ====
def draw_bars(data, color_array):
    canvas.delete("all")
    c_width = 800
    c_height = 300
    bar_width = c_width / len(data) if data else 1
    max_val = max(data) if data else 1

    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - (val / max_val * (c_height - 20))
        x1 = (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(val), font=("Segoe UI", 8))

    root.update_idletasks()

# ==== Sorting Algorithms ====
def bubble_sort(data):
    global stop_flag
    comparisons, swaps = 0, 0
    n = len(data)
    start = time.time()
    for i in range(n):
        for j in range(n - i - 1):
            if stop_flag:
                return
            comparisons += 1
            draw_bars(data, ["#f39c12" if x == j or x == j+1 else "#bdc3c7" for x in range(n)])
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
            time.sleep(speed.get())
    end = time.time()
    draw_bars(data, ["#27ae60"] * n)
    show_stats(comparisons, swaps, end - start)

def insertion_sort(data):
    global stop_flag
    comparisons, swaps = 0, 0
    start = time.time()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            if stop_flag:
                return
            comparisons += 1
            data[j + 1] = data[j]
            draw_bars(data, ["#f39c12" if x == j or x == j+1 else "#bdc3c7" for x in range(len(data))])
            j -= 1
            time.sleep(speed.get())
        data[j + 1] = key
        swaps += 1
    end = time.time()
    draw_bars(data, ["#27ae60"] * len(data))
    show_stats(comparisons, swaps, end - start)

def selection_sort(data):
    global stop_flag
    comparisons, swaps = 0, 0
    n = len(data)
    start = time.time()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if stop_flag:
                return
            comparisons += 1
            draw_bars(data, ["#f39c12" if x == j or x == min_idx else "#bdc3c7" for x in range(n)])
            if data[j] < data[min_idx]:
                min_idx = j
            time.sleep(speed.get())
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps += 1
    end = time.time()
    draw_bars(data, ["#27ae60"] * n)
    show_stats(comparisons, swaps, end - start)

def merge_sort(data, left, right, draw, delay, stats):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid, draw, delay, stats)
        merge_sort(data, mid + 1, right, draw, delay, stats)
        merge(data, left, mid, right, draw, delay, stats)

def merge(data, left, mid, right, draw, delay, stats):
    merged = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        stats['comparisons'] += 1
        if stop_flag:
            return
        if data[i] < data[j]:
            merged.append(data[i])
            i += 1
        else:
            merged.append(data[j])
            j += 1
    while i <= mid:
        merged.append(data[i])
        i += 1
    while j <= right:
        merged.append(data[j])
        j += 1
    for i, val in enumerate(merged):
        if stop_flag:
            return
        data[left + i] = val
        draw(data, ["#f39c12" if x == left + i else "#bdc3c7" for x in range(len(data))])
        time.sleep(delay)

def quick_sort(data, low, high, draw, delay, stats):
    if low < high:
        pi = partition(data, low, high, draw, delay, stats)
        quick_sort(data, low, pi - 1, draw, delay, stats)
        quick_sort(data, pi + 1, high, draw, delay, stats)

def partition(data, low, high, draw, delay, stats):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        stats['comparisons'] += 1
        if stop_flag:
            return high
        draw(data, ["#f39c12" if x == j or x == high else "#bdc3c7" for x in range(len(data))])
        time.sleep(delay)
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            stats['swaps'] += 1
    data[i + 1], data[high] = data[high], data[i + 1]
    stats['swaps'] += 1
    return i + 1

# ==== Heap Sort ====
def heapify(data, n, i):
    largest = i
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    if left < n and data[largest] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data):
    global stop_flag
    swaps = 0
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        swaps += 1
        heapify(data, i, 0)
    
    return data

# ==== Generate Lists ====
def generate_list(type_):
    global data
    length = 30
    if type_ == "Random":
        data = random.sample(range(10, 100), length)
    elif type_ == "Sorted":
        data = list(range(10, 10 + length))
    elif type_ == "Reversed":
        data = list(range(10 + length, 10, -1))
    draw_bars(data, ["#3498db"] * len(data))

# ==== Start Sorting ====
def start_sort():
    global stop_flag
    stop_flag = False
    algo = algo_choice.get()
    temp_data = data.copy()
    stats = {"comparisons": 0, "swaps": 0}
    start = time.time()

    if algo == "Bubble Sort":
        bubble_sort(temp_data)
        return
    elif algo == "Insertion Sort":
        insertion_sort(temp_data)
        return
    elif algo == "Selection Sort":
        selection_sort(temp_data)
        return
    elif algo == "Merge Sort":
        merge_sort(temp_data, 0, len(temp_data) - 1, draw_bars, speed.get(), stats)
    elif algo == "Quick Sort":
        quick_sort(temp_data, 0, len(temp_data) - 1, draw_bars, speed.get(), stats)
    elif algo == "Heap Sort":
        heap_sort(temp_data)

    end = time.time()
    draw_bars(temp_data, ["#27ae60"] * len(temp_data))
    show_stats(stats['comparisons'], stats['swaps'], end - start)

def stop_sort():
    global stop_flag
    stop_flag = True

def show_stats(comp, swaps, time_elapsed):
    stats_label.config(
        text=f"Comparisons: {comp}    Swaps: {swaps}    Time: {time_elapsed:.4f}s"
    )

# ==== Controls Frame ====
controls_frame = tk.Frame(root, bg="#1e1e2f")
controls_frame.pack()

algo_choice = tk.StringVar()
algo_menu = ttk.Combobox(controls_frame, textvariable=algo_choice, state="readonly")
algo_menu['values'] = ("Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort", "Heap Sort")
algo_menu.set("Choose Algorithm")
algo_menu.pack(side=tk.LEFT, padx=10)

tk.Button(controls_frame, text="Random List", command=lambda: generate_list("Random"),
          bg="#00cec9", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)
tk.Button(controls_frame, text="Sorted", command=lambda: generate_list("Sorted"),
          bg="#0984e3", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)
tk.Button(controls_frame, text="Reversed", command=lambda: generate_list("Reversed"),
          bg="#6c5ce7", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)
tk.Button(controls_frame, text="Start", command=start_sort,
          bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)
tk.Button(controls_frame, text="⏹ Stop", command=stop_sort,
          bg="#d63031", fg="white", font=("Segoe UI", 10, "bold"), bd=0).pack(side=tk.LEFT, padx=5)

# ==== Speed Control ====
speed = tk.DoubleVar(value=0.05)
tk.Scale(root, from_=0.01, to=0.3, resolution=0.01, variable=speed,
         label="Speed (slower → faster)", orient=tk.HORIZONTAL, length=200,
         bg="#1e1e2f", fg="white", troughcolor="#636e72").pack(pady=10)

# ==== Stats Label ====
stats_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#1e1e2f", fg="#00ffff")
stats_label.pack(pady=5)

# ==== Mainloop ====
root.mainloop()

