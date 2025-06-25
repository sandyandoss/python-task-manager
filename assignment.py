# You will simulate a task manager.
# The program will generate an X number of tasks (input from the user). Each task will have a title, duration (in mins) and a priority (also input from the user), lower value of priority the higher it is. Use a single list to hold the tasks in it and to be used as a queue.
# You will implement your own functions for the queue (insert, extract, peek, is_empty).
# Your program will have the following functions (other than the queue related ones):
# `complete_next_task`: will take the queue as argument and will print and extract the highest priority task
# `search_for_task`: will take the queue and title as arguments and search for that set title. (you have to use Binary Search Algorithm)
# `sort_tasks`: will take queue as argument and will return a new queue have tasks sorted duration (ascending or descending your coice)

#Queue Operations 
def insert(queue:list, task):
    queue.append(task)

def extract(queue:list):
    if is_empty(queue):
        return None
    return queue.pop(0) 

def peek(queue:list):
    if is_empty(queue):
        return None    
    return queue[0]  

def is_empty(queue:list):
    return len(queue) == 0             

#step 2 do the tasks:
#if empty:

def complete_next_task(queue: list):
    if is_empty(queue):
        print("No tasks to complete.")
        return
    
    # if not, search for lowest priority
    min_priority = queue[0]['priority']
    min_index = 0
    for i in range(1, len(queue)):
        if queue[i]['priority'] < min_priority:
            min_priority = queue[i]['priority']
            min_index = i
    
    task = queue.pop(min_index)
    print("Completed Task:")
    print(task)


def binary_search_by_title(queue: list, title: str):
    sorted_queue = sorted(queue, key=lambda task: task['title'])

    left = 0
    right = len(sorted_queue) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_queue[mid]['title'] == title:
            return sorted_queue[mid]
        elif sorted_queue[mid]['title'] < title:
            left = mid + 1
        else:
            right = mid - 1

    return None


def sort_tasks_by_duration(queue: list, ascending=True):
    def merge_sort(tasks):
        if len(tasks) <= 1:
            return tasks

        mid = len(tasks) // 2
        left = merge_sort(tasks[:mid])
        right = merge_sort(tasks[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if ascending:
                condition = left[i]['duration'] <= right[j]['duration']
            else:
                condition = left[i]['duration'] >= right[j]['duration']

            if condition:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    return merge_sort(queue.copy())

#the main task manager

def run_task_manager():
    task_queue = []

    n = int(input("Enter number of tasks: "))
    for _ in range(n):
        title = input("Enter task title: ")
        duration = int(input("Enter duration (in minutes): "))
        priority = int(input("Enter priority (lower number = higher priority): "))
        task = {'title': title, 'duration': duration, 'priority': priority}
        insert(task_queue, task)

    print("All tasks:")
    for t in task_queue:
        print(t)

    print("Completing Next Task")
    complete_next_task(task_queue)

    print(" Searching for a Task")
    search_title = input("Enter task title to search: ")
    result = binary_search_by_title(task_queue, search_title)
    if result:
        print("Found task:", result)
    else:
        print("Task not found.")

    print("Sorted Tasks by Duration")
    sorted_tasks = sort_tasks_by_duration(task_queue, ascending=True)
    for t in sorted_tasks:
        print(t)

run_task_manager()
