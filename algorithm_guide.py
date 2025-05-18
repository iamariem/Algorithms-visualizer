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

# === Insertion Sort Explanation ===
def insertion_sort_explanation():
    explanation = """
    Insertion Sort Algorithm:

    1. Start from the second element of the list.
    2. Compare the current element with the previous one.
    3. If the current element is smaller, shift the larger elements one position to the right.
    4. Insert the current element into the correct position.
    5. Repeat the process for all elements.

    Time Complexity:
    - Best Case: O(n) (Already Sorted List)
    - Worst Case: O(n^2) (Reverse Sorted List)
    - Average Case: O(n^2)
    """
    explanation_label.config(text=explanation)

# === Selection Sort Explanation ===
def selection_sort_explanation():
    explanation = """
    Selection Sort Algorithm:

    1. Start by finding the minimum element in the list.
    2. Swap the minimum element with the first element.
    3. Repeat this process for the remaining unsorted portion of the list.
    4. Continue until the entire list is sorted.

    Time Complexity:
    - Best Case: O(n^2)
    - Worst Case: O(n^2)
    - Average Case: O(n^2)
    """
    explanation_label.config(text=explanation)

# === Quick Sort Explanation ===
def quick_sort_explanation():
    explanation = """
    Quick Sort Algorithm:

    1. Choose a 'pivot' element from the array.
    2. Partition the array into two sub-arrays: one with elements smaller than the pivot, and one with elements greater.
    3. Recursively apply the same steps to the sub-arrays.
    4. The base case is when the sub-array has fewer than two elements.

    Time Complexity:
    - Best Case: O(n log n)
    - Worst Case: O(n^2)
    - Average Case: O(n log n)
    """
    explanation_label.config(text=explanation)

# === Binary Search Explanation ===
def binary_search_explanation():
    explanation = """
    Binary Search Algorithm:

    1. Start with a sorted array and find the middle element.
    2. If the target is equal to the middle element, return the index.
    3. If the target is smaller, repeat the process on the left half of the array.
    4. If the target is larger, repeat the process on the right half of the array.
    5. Repeat until the element is found or the array cannot be divided further.

    Time Complexity:
    - Best Case: O(1)
    - Worst Case: O(log n)
    - Average Case: O(log n)
    """
    explanation_label.config(text=explanation)

# === Heap Sort Explanation ===
def heap_sort_explanation():
    explanation = """
    Heap Sort Algorithm:

    1. Build a max heap from the input data.
    2. Swap the root (max value) with the last element of the heap.
    3. Restore the heap property for the reduced heap.
    4. Repeat the process until the heap is empty.

    Time Complexity:
    - Best Case: O(n log n)
    - Worst Case: O(n log n)
    - Average Case: O(n log n)
    """
    explanation_label.config(text=explanation)

# === Linear Search Explanation ===
def linear_search_explanation():
    explanation = """
    Linear Search Algorithm:

    1. Start from the first element and compare it with the target.
    2. If it matches, return the index.
    3. If it does not match, continue with the next element.
    4. Repeat until the target is found or the list ends.

    Time Complexity:
    - Best Case: O(1)
    - Worst Case: O(n)
    - Average Case: O(n)
    """
    explanation_label.config(text=explanation)

# === GUI Setup ===
window = tk.Tk()
window.title("Algorithm Guide")
window.geometry("800x600")
window.config(bg="#1e1e2f")

# Explanation Button for different algorithms
bubble_sort_button = tk.Button(window, text="Show Bubble Sort Explanation", command=bubble_sort_explanation,
                               bg="#00b894", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
bubble_sort_button.pack(pady=10)

insertion_sort_button = tk.Button(window, text="Show Insertion Sort Explanation", command=insertion_sort_explanation,
                                   bg="#0984e3", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
insertion_sort_button.pack(pady=10)

selection_sort_button = tk.Button(window, text="Show Selection Sort Explanation", command=selection_sort_explanation,
                                   bg="#6c5ce7", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
selection_sort_button.pack(pady=10)

quick_sort_button = tk.Button(window, text="Show Quick Sort Explanation", command=quick_sort_explanation,
                              bg="#e74c3c", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
quick_sort_button.pack(pady=10)

binary_search_button = tk.Button(window, text="Show Binary Search Explanation", command=binary_search_explanation,
                                 bg="#f39c12", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
binary_search_button.pack(pady=10)

heap_sort_button = tk.Button(window, text="Show Heap Sort Explanation", command=heap_sort_explanation,
                             bg="#9b59b6", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
heap_sort_button.pack(pady=10)

linear_search_button = tk.Button(window, text="Show Linear Search Explanation", command=linear_search_explanation,
                                 bg="#34495e", fg="white", font=("Segoe UI", 12, "bold"), bd=0)
linear_search_button.pack(pady=10)

# Explanation Label
explanation_label = tk.Label(window, text="", fg="white", bg="#1e1e2f", font=("Segoe UI", 12))
explanation_label.pack(pady=20)

window.mainloop()

