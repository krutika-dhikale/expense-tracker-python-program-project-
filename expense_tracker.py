from tkinter import *
from tkinter import messagebox

expenses = []

# Add Expense
def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()

    if item == "" or amount == "":
        messagebox.showwarning("Warning", "Enter item and amount!")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    expenses.append([item, amount])
    update_list()

    item_entry.delete(0, END)
    amount_entry.delete(0, END)
def edit_expense():
    try:
        selected = listbox.curselection()[0]

        item = item_entry.get()
        amount = amount_entry.get()

        if item == "" or amount == "":
            messagebox.showwarning("Warning", "Enter item and amount!")
            return

        amount = float(amount)

        expenses[selected] = [item, amount]
        update_list()

        item_entry.delete(0, END)
        amount_entry.delete(0, END)

        messagebox.showinfo("Success", "Expense updated!")

    except:
        messagebox.showwarning("Warning", "Select an expense first!")
# Delete Expense
def delete_expense():
    try:
        selected = listbox.curselection()[0]
        expenses.pop(selected)
        update_list()
    except:
        messagebox.showwarning("Warning", "Select an expense!")

# Update Listbox
def update_list():
    listbox.delete(0, END)

    total = 0

    for item, amount in expenses:
        listbox.insert(END, f"{item} - ₹{amount}")
        total += amount

    total_label.config(text=f"Total Expense: ₹{total}")
def select_expense(event):
    try:
        selected = listbox.curselection()[0]

        item_entry.delete(0, END)
        amount_entry.delete(0, END)

        item_entry.insert(0, expenses[selected][0])
        amount_entry.insert(0, expenses[selected][1])

    except:
        pass
# GUI
root = Tk()
root.title("Expense Tracker")
root.geometry("500x450")

Label(root, text="Expense Name", font=("Arial", 12)).pack(pady=5)

item_entry = Entry(root, width=30)
item_entry.pack(pady=5)

Label(root, text="Amount", font=("Arial", 12)).pack(pady=5)

amount_entry = Entry(root, width=30)
amount_entry.pack(pady=5)

Button(root, text="Add Expense", command=add_expense).pack(pady=5)

Button(root, text="Edit Expense",command=edit_expense).pack(pady=5)

Button(root, text="Delete Expense", command=delete_expense).pack(pady=5)

listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=10)

total_label = Label(root, text="Total Expense: ₹0", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

listbox.bind("<<ListboxSelect>>",select_expense)
root.mainloop()




