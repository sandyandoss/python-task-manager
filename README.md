# 🧠 Task Manager Simulator

Welcome to the **Task Manager Simulator**! This project is a beginner-friendly Python application that simulates how a task manager might handle tasks using queues, sorting, and searching.

---

## ✨ Features

- 📋 Add tasks with a **title**, **duration**, and **priority**
- ⏳ Complete the next task based on **highest priority** (lowest number)
- 🔍 Search for a task by its **title** using **binary search**
- 🔃 Sort tasks by **duration** using **merge sort**
- 🧺 All tasks are managed using a custom-built **queue**

---

## 🧩 Concepts Covered

- Queues (FIFO) implemented with lists
- Custom queue operations: `insert`, `extract`, `peek`, `is_empty`
- Priority selection logic
- Merge Sort (for sorting by duration)
- Binary Search (for task lookup by title)
- Dictionaries for representing tasks

---

## 🚀 How to Run

1. Clone or download the project
2. Open the Python file in any editor (e.g., VS Code, PyCharm)
3. Run it using:
   ```bash
   python task_manager.py

Enter number of tasks: 2
Enter task title: Homework
Enter duration (in minutes): 60
Enter priority (lower number = higher priority): 1
Enter task title: Exercise
Enter duration (in minutes): 30
Enter priority (lower number = higher priority): 2

All tasks:
{'title': 'Homework', 'duration': 60, 'priority': 1}
{'title': 'Exercise', 'duration': 30, 'priority': 2}

Completing Next Task
Completed Task:
{'title': 'Homework', 'duration': 60, 'priority': 1}


💡 Tip
Try experimenting by adding more tasks and watching how sorting and searching behave! It's a great way to practice your Python fundamentals.

🐍 Built With
Python 3.x

No external libraries – 100% beginner-friendly!

