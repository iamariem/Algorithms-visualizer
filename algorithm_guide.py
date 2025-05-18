import tkinter as tk

# === Bubble Sort Explanation ===
def bubble_sort_explanation():
    explanation = """
    Bubble Sort Algorithm:

    1. Start at the first element of the list.
    2. Compare the current element with the next one.
    3. If the current element is greater than the next, swap them.
    4. Repeat the process for all elements, excluding the last sorted element.
    5. Repeat until the list is sorted.

    Time Complexity:
    - Best Case: O(n) (Already Sorted List)
    - Worst Case: O(n^2) (Reverse Sorted List)
    - Average Case: O(n^2)
    """
    explanation_label.config(text=explanation)

# === GUI Setup ===
window = tk.Tk()
window.title("Algorithm Guide | Bubble Sort")
window.geometry("800x500")
window.config(bg="#1e1e2f")

# Explanation Button
button = tk.Button(window, text="Show Bubble Sort Explanation", command=bubble_sort_explanation,
                   bg="#00b894", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
button.pack(pady=20)

# Explanation Label
explanation_label = tk.Label(window, text="", fg="white", bg="#1e1e2f", font=("Segoe UI", 12))
explanation_label.pack(pady=20)

window.mainloop()
