import mysql.connector
import tkinter as tk
from tkinter import scrolledtext
import os

def File():
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="bhag123",
      database="expense_tracker"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT D_No,category,item,Amount,ret,timestamp FROM debit ")
  result = mycursor.fetchall()
  mycursor.execute("SELECT C_No,c_From,Description,Credit_amount,c_timestamp  FROM credit")
  result1 = mycursor.fetchall()


  with open("D:/expense_tracker.txt", "w") as file:
      file.write("\t\t\t\t\t\t\tAll Expenses" + "\n\n")
      file.write("D_No\t\t  category\t\t\titem\t\t\tAmount\t\t  ret\t\t\ttimestamp\n")
      for row in result:
          row_data = " ".join([str(item).ljust(20) for item in row]) 
          file.write(row_data + "\n")
      
      file.write("\n\n\t\t\t\t\t\t\tAll Incomes" + "\n\n")
      file.write("C_No\t\tc_From\t\t\t  Description\t\t\t Credit_amount\t\t c_timestamp\n")
      for row in result1:
          row_data = " ".join([str(item).ljust(20) for item in row]) 
          file.write(row_data + "\n")

  root = tk.Tk()
  root.geometry("1200x700")
  root.title("Text File Viewer")


  file_path = "D:\\expense_tracker.txt"

  if os.path.exists(file_path):
    
      with open(file_path, "r") as file:
          file_content = file.read()

          text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
          text_area.insert(tk.INSERT, file_content)
          text_area.pack(fill="both", expand=True)
  else:
      
      label = tk.Label(root, text="File not found!!")
      label.pack()

  root.mainloop()

  mycursor.close()
  mydb.close()


