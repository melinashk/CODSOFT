import tkinter as tk
import tkinter.simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.todos = []
        
        self.add = tk.Button(self.master, text="Add To-Do", command=self.add_todo)
        self.add.pack()
        
        self.delete = tk.Button(self.master, text="Delete Todo", command=self.delete_todo)
        self.delete.pack()
        
        self.edit = tk.Button(self.master, text="Edit Todo", command=self.edit_todo)
        self.edit.pack()
                
        self.todo_listbox = tk.Listbox(self.master, width=50)
        self.todo_listbox.pack(pady=10)
        
        self.update_listbox()
        
    def add_todo(self):
        new_todo = tkinter.simpledialog.askstring("Add To-do", "Enter new todo:", initialvalue="")
        # todo = self.todo_entry.get()
        if new_todo:
            self.todos.append(new_todo)
            self.update_listbox()
            self.todo_entry.delete(0, tk.END)
        
    def delete_todo(self):
        selection = self.todo_listbox.curselection()
        if selection:
            index = selection[0]
            del self.todos[index]
            self.update_listbox()
        
    def edit_todo(self):
        selection = self.todo_listbox.curselection()
        if selection:
            index = selection[0]
            old_todo = self.todos[index]
            edited_todo = tkinter.simpledialog.askstring("Edit To-do", "Enter new todo:", initialvalue=old_todo)
            if edited_todo:
                self.todos[index] = edited_todo
                self.update_listbox()
        
    def update_listbox(self):
        self.todo_listbox.delete(0, tk.END)
        for todo in self.todos:
            self.todo_listbox.insert(tk.END, todo)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
