import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Add Task", command=add_task)
button.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()