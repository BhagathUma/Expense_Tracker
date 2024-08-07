import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bhag123",
  database="expense_tracker"
)
cur=mydb.cursor()

def add_to_credit(from_value,description_value,amount_value):
    credit_val=[0,0,0,0]
    
    credit_val[0]=from_value
    credit_val[1]=description_value
    credit_val[2]=amount_value
    amount_list=[amount_value]
    credit_val[3]=6
    cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Credit'",amount_list)
    mydb.commit()
    cur.execute("INSERT INTO credit(c_From,Description,Credit_amount,W_No) VALUES(%s,%s,%s,%s)",credit_val)
    mydb.commit()
    

def submit():
    from_value = from_var.get()
    description_value = description.get()
    amount_value = amount.get()

    if not description_value or not amount_value:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    if from_value not in ["Salary", "Other"]:
        messagebox.showerror("Error", "Please select any one checkbox")
        return
    

    try:
        amount_value = int(amount_value)
        if amount_value <= 0:
            messagebox.showerror("Error", "Amount must be a positive integer")
            return
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid integer")
        return
    add_to_credit(from_value,description_value,amount_value)
    print("From:", from_value)
    print("Description:", description_value)
    print("Amount:", amount_value)

root = tk.Tk()
root.geometry("500x400")
root.title("Credit Tracker")


from_var = tk.StringVar(root)
from_var.set(None)
from_label = tk.Label(root, text="From:")
from_label.pack()
options = ["Salary", "Other"]
for option in options:
    rb = tk.Radiobutton(root, text=option, variable=from_var, value=option)
    rb.pack()


description_label = tk.Label(root, text="Description (max 50 characters):")
description_label.pack()
description = tk.Entry(root, width=50)
description.pack()


amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount = tk.Entry(root)
amount.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
