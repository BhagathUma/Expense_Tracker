
import tkinter as tk
deb_count,cred_count,stat_count,target_count=0,0,0,0 

def debit_call(deb_count):
    import debit
    deb_count+=1
    if(deb_count>1):
        debit.submit(deb_count)

    
def credit_call(cred_count):
    import credit
    cred_count+=1
    if(cred_count>1):
        credit.submit(cred_count)

def stat_call(stat_count):
    import calculate
    stat_count+=1
    if(stat_count>1):
        calculate.calculate(stat_count)

def target_call(target_count):
    import target

def report_call():
    import file
    file.File()
    
    


root = tk.Tk()

root.geometry("700x400")
root.title("Credit Tracker")
lable1=tk.Label(root,text="Welcome!! From YOUR",font=("Arial",18))
lable2=tk.Label(root,text="Monthly Expense Tracker",font=("Arial",18))
lable1.pack(padx=10,pady=10)
lable2.pack(padx=10,pady=10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)

bt1=tk.Button(buttonframe,text="ADD CREDIT",font=("Arial",18),command=lambda:credit_call(cred_count))
bt1.grid(row=0,column=0,sticky=tk.W+tk.E)

bt4=tk.Button(buttonframe,text="ADD TARGET",font=("Arial",18),command=lambda:target_call(target_count))
bt4.grid(row=0,column=1,sticky=tk.W+tk.E)

bt2=tk.Button(buttonframe,text="STATISTICS",font=("Arial",18),command=lambda:stat_call(stat_count))
bt2.grid(row=0,column=2,sticky=tk.W+tk.E)

bt3=tk.Button(buttonframe,text="ADD DEBIT",font=("Arial",18),command=lambda:debit_call(deb_count))
bt3.grid(row=0,column=3,sticky=tk.W+tk.E)

buttonframe1=tk.Frame(root)
buttonframe1.columnconfigure(0,weight=1)
bt5=tk.Button(buttonframe1,text="GET MONTHLY REPORT",font=("Arial",18),command=lambda:report_call())
bt5.grid(row=0,column=0,padx=10,pady=50,sticky=tk.W+tk.E)


buttonframe.pack()
buttonframe1.pack()

root.mainloop()
