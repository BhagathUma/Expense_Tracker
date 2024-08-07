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

def add_to_debit(category_value,item_value,amount_value,return_value):
    debit_val=[0,0,0,0,0]
    
    debit_val[0]=category_value
    debit_val[1]=item_value
    debit_val[2]=amount_value
    debit_val[3]=return_value
    amount_list=[amount_value]
    if(category_value)=="Transportation":
        debit_val[4]=1
        cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Transportation'",amount_list)
    elif(category_value)=="Grocery":
        debit_val[4]=2
        cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Grocery'",amount_list)
    elif(category_value)=="Medical":
        debit_val[4]=3
        cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Medical'",amount_list)
    elif(category_value)=="Food":
        debit_val[4]=4
        cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Food'",amount_list)
    elif(category_value)=="Other":
        debit_val[4]=5
        cur.execute("update wallet set Give_and_Take=Give_and_Take + %s where Name='Other'",amount_list)
    mydb.commit()  
    cur.execute("INSERT INTO debit(category,item,amount,ret,W_No) VALUES(%s,%s,%s,%s,%s)",debit_val)
    mydb.commit()