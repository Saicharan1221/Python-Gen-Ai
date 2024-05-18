import tkinter as tk
from tkinter import ttk

def display_citations(citations):
    root = tk.Tk()
    root.title("Identified Citations")

    tree = ttk.Treeview(root)
    tree["columns"] = ("1", "2")
    tree.column("#0", width=100)
    tree.column("1", width=200)
    tree.column("2", width=200)
    tree.heading("#0", text="ID")
    tree.heading("1", text="Link")
    tree.heading("2", text="Context")

    for citation in citations:
        tree.insert("", "end", text=citation["id"], values=(citation["link"], citation["context"]))

    tree.pack()
    root.mainloop()
