import tkinter as tk
import random
import time
import matplotlib.pyplot as plt

# === Global Variables ===
data = []
comparisons = []
swaps = []
times = []

# === Generate Random Data ===
def generate_data(size):
    return random.sample(range(1, size+1), size)

# === Sorting Algorithms ===
def bubble_sort(data):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    start = time.time()
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                swaps += 1
                data[j], data[j + 1] = data[j + 1], data[j]
    end = time.time()
    return end - start

def insertion_sort(data):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    start = time.time()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            comparisons += 1
            data[j + 1] = data[j]
            swaps += 1
            j -= 1
        data[j + 1] = key
    end = time.time()
    return end - start

# === Binary Search Algorithm ===
def binary_search(data, target):
    global comparisons
    comparisons = 0
    start = time.time()
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if data[mid] == target:
            return time.time() - start
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return time.time() - start

# === Plot Performance Comparison ===
def plot_performance():
    plt.figure(figsize=(10, 6))

    # Plot sorting algorithm comparison
    plt.bar(["Bubble Sort", "Insertion Sort"], [times[0], times[1]], color=["#3498db", "#2ecc71"])
    plt.title("Sorting Algorithms Performance")
    plt.ylabel("Time in seconds")
    plt.show()

# === Start Performance Test ===
def start_performance_test():
    global times
    size = int(size_entry.get())
    data = generate_data(size)
    
    times = []
    
    # Bubble Sort
    times.append(bubble_sort(data.copy()))
    
    # Insertion Sort
    times.append(insertion_sort(data.copy()))
    
    # Binary Search (Example)
    target = random.choice(data)  # Pick a random target
    binary_search_time = binary_search(sorted(data), target)
    
    times.append(binary_search_time)

    plot_performance()

# === GUI Setup ===
window = tk.Tk()
window.title("Performance Comparison")
window.geometry("900x600")
window.config(bg="#1e1e2f")

# Controls
controls = tk.Frame(window, bg="#1e1e2f")
controls.pack()

size_label = tk.Label(controls, text="Enter data size:", fg="white", bg="#1e1e2f", font=("Segoe UI", 12))
size_label.pack(side=tk.LEFT, padx=10)

size_entry = tk.Entry(controls, width=10, font=("Segoe UI", 12))
size_entry.pack(side=tk.LEFT, padx=10)

start_button = tk.Button(controls, text="Start Performance Test", command=start_performance_test,
                         bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"), bd=0)
start_button.pack(side=tk.LEFT, padx=10)

window.mainloop()
