import tkinter as tk
from tkinter import ttk

def open_courses_window(parent=None):
    # Use Toplevel if opened from another window
    courses_window = tk.Toplevel(parent)
    courses_window.title("Common Courses")
    courses_window.geometry("600x400")
    courses_window.config(bg="white")

    tk.Label(
        courses_window,
        text="📚 Course: B.Tech (Data Science)   Batch: 2025-2029",
        font=('Arial', 16, 'bold'),
        bg='white',
        pady=10
    ).pack()

    # Example course data
    course_data = [
        ("BACHY105", "Applied Chemistry", "4 Credits"),
        ("BACSE101", "Problem Solving using Python", "2 Credits"),
        ("BAEEE101", "Basic Engineering", "4 Credits"),
        ("BAMAT101", "Multivariable Calculus and Differential Equation", "4 Credits"),
        ("BACSE103", "Computation Structures", "4 Credits"),
    ]

    # Treeview for course listing
    tree_courses = ttk.Treeview(
        courses_window,
        columns=("code", "name", "credits"),
        show="headings"
    )
    tree_courses.heading("code", text="Course Code")
    tree_courses.heading("name", text="Course Name")
    tree_courses.heading("credits", text="Credits")
    tree_courses.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    # Insert course data
    for course in course_data:
        tree_courses.insert("", tk.END, values=course)

    # Close button
    tk.Button(
        courses_window,
        text="Close",
        command=courses_window.destroy,
        bg='lightcoral',
        font=('Arial', 12, 'bold')
    ).pack(pady=10)
open_courses_window()