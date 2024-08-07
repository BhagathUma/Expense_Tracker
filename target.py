import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhag123",
    database="expense_tracker"
)

mycursor = mydb.cursor()

def validate_input(targeton, amount):
    if not targeton or not amount:
        messagebox.showerror("Error", "Please enter all inputs")
        return False
    try:
        int(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be an integer")
        return False
    return True

def insert_data():
    targeton = entry_targeton.get()
    amount = entry_amount.get()

    if not validate_input(targeton, amount):
        return

    sql = "INSERT INTO target (targeton, amount) VALUES (%s, %s)"
    val = (targeton, amount)

    mycursor.execute(sql, val)
    mydb.commit()

    


# Create a tkinter window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")

# Create input fields and labels
tk.Label(root, text="Target On:").pack()
entry_targeton = tk.Entry(root)
entry_targeton.pack()

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# Create the insert button
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

root.mainloop()
