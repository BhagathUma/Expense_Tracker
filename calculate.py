import mysql.connector
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bhag123",
  database="expense_tracker"
)

cur = mydb.cursor()

def Total():
  deb=0
  cre=0
  
  sql=" select sum( Give_and_Take) from wallet where Name <> 'credit'"
  cur.execute(sql)
  row=cur.fetchall()
  for r in row:
      deb=r[0]


  sql=" select sum( Give_and_Take) from wallet where Name = 'credit'"
  cur.execute(sql)
  row=cur.fetchall()
  for r in row:
      cre=r[0]

  total=cre-deb
  target=0

  sql="select * from target"
  cur.execute(sql)
  row=cur.fetchall()
  row.sort(reverse=True, key=lambda x: x[1])
  for r in row:
      target+=r[1]

  root = tk.Tk()

  root.geometry("700x500")
  root.title("Credit Tracker")

  if(total<0):
      lable=tk.Label(root,text="Oops!! your Expense is was more this time ",font=("Arial",18))
      lable1=tk.Label(root,text="Total Savings: "+str(total)+"  Better Luck Next month!!",font=("Arial",18))
      
      lable.pack(padx=10,pady=10)
      lable1.pack(padx=10,pady=10)
     

  else:
      lable=tk.Label(root,text="WOW!! You have spent less than your income ths month",font=("Arial",18))
      lable1=tk.Label(root,text="Total Savings: "+str(total)+"  Good Luck Next month!!",font=("Arial",18))
    
      lable.pack(padx=10,pady=10)
      lable1.pack(padx=10,pady=10)
  
  lable=tk.Label(root,text="Your targets",font=("Arial",18))
  lable.pack(padx=10,pady=10)
  for i in range(len(row)):
      lable=tk.Label(root,text="Target "+str(i)+" -> "+str(row[i][0])+"-"+str(row[i][1])+"Rs",font=("Arial",12))
      lable.pack(padx=10,pady=10)
  if target < total:
      
      lable=tk.Label(root,text="WOW!! all your target is achieved this month",font=("Arial",18),foreground="Green")
      lable.pack(padx=10,pady=10)
  else:
      lable=tk.Label(root,text="OH NO!! your targets are not achieved this time",font=("Arial",18),foreground="Red")
      lable.pack(padx=10,pady=10)



  root.mainloop()

def calculate():

  cur.execute("SELECT Name, Give_and_Take FROM wallet")
  result = cur.fetchall()

  names = []
  values = []

  for record in result:
      names.append(record[0])
      values.append(record[1])


  bar=plt.bar(names, values)
  bar[5].set_color('Red')
  plt.xlabel('Name')
  plt.ylabel('Give_and_Take')
  plt.title('Monthly Expense Graph')
  plt.show()


  cur.execute("SELECT Name, Give_and_Take FROM wallet")
  result = cur.fetchall()

  labels = []
  sizes = []

  for record in result:
      labels.append(record[0])
      sizes.append(record[1])


  plt.pie(sizes, labels=labels, autopct='%1.1f%%')
  plt.axis('equal') 
  plt.title('Monthly Expense Distribution')
  plt.show()
  Total()

calculate()



