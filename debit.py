import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import date
import debit2

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bhag123",
  database="expense_tracker"
)
cur=mydb.cursor()





def submit():
    category_value = category.get()
    item_value = item.get()
    amount_value = amount.get()
    return_value = return_var.get()
   

    
    

    if not item_value or not amount_value or not return_value:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    if category_value not in ["Transportation", "Grocery", "Medical", "Food", "Other"]:
        messagebox.showerror("Error", "please choose a category")
        return
    try:
        amount_value = int(amount_value)
        if amount_value <= 0:
            messagebox.showerror("Error", "Amount must be a positive integer")
            return
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid integer")
        return

    if return_value not in ['Y', 'N']:
        messagebox.showerror("Error", "Return value must be 'Y' or 'N'")
        return
    
    if len(item_value)>50:
        messagebox.showerror("Error", "Item must be less than 50 characters")
        return
    
    print("Category:", category_value)
    
    print("Item:", item_value)
    print("Amount:", amount_value)
    print("Return:", return_value)
    debit2.add_to_debit(category_value,item_value,amount_value,return_value)

root = tk.Tk()
root.geometry("500x400")
root.title("Expense Tracker")


category = tk.StringVar(root)
category.set(None)
category_label = tk.Label(root,font=('Arial',18), text="Category:")
category_label.pack()
options = ["Transportation", "Grocery", "Medical", "Food", "Other"]
for option in options:
    rb = tk.Radiobutton(root, text=option, variable=category, value=option)
    rb.pack()

item_label = tk.Label(root,font=('Arial',18), text="Description of your Expense Made: ")
item_label.pack()
item = tk.Entry(root ,width=50)
item.pack()


amount_label = tk.Label(root,font=('Arial',18), text="Amount Spent:")
amount_label.pack()
amount = tk.Entry(root)
amount.pack()


return_label = tk.Label(root,font=('Arial',18), text="Return (Y/N):")
return_label.pack()
return_var = tk.Entry(root)
return_var.pack()

submit_button = tk.Button(root, text="Submit", command=submit)

submit_button.pack()


root.mainloop()