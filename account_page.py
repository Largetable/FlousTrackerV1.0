import tkinter as tk
from tkinter import E,W,S,N
class Account(tk.Frame):
	def __init__(self, parent, attr):
		tk.Frame.__init__(self, parent)
		self.parent=parent
		self.attr=attr
		self.config(bg='#aaf7f7')
		#main_frame=tk.Frame(self, width=900, height=500, bg='red')
		#main_frame.place(x=0,y=0)
		frame1=tk.Frame(self, width=450, height=500, bg='black')
		frame2=tk.Frame(self, width=450, height=500, bg='blue')
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		frame1.grid(row=0, column=0, sticky=N+S+W+E)
		frame2.grid(row=0, column=1, sticky=N+S+W+E)

		last_login_frame=tk.Frame(frame1, width=350, height=300,bg='white')
		welcome_label=tk.Label(frame1, text='Welcome {} ! '.format(attr), font=("Courier", 18), fg='blue')
		estim_cash_label=tk.Label(frame1, text='Estimated cash: $$$$$', fg='green', font=("Courier",18))
		#cash_value_label=tk.Label(frame1, text= "CASHDT",bg='green', font=("Courier",18))

		expense_add_frame=tk.Frame(frame2, width = 400, height= 300, bg='white' )
		add_expense_label=tk.Label(last_login_frame, text="Add expense here!", font=("Courier",15), bg="red")
		test=tk.Label(self, text="TEST")

		#self.grid_columnconfigure(0, weight=1)
		#self.grid_columnconfigure(1, weight=1)
		#self.grid_columnconfigure(2, weight=1)
		#self.grid_rowconfigure(1, weight=2)'
		welcome_label.pack(pady=20)
		estim_cash_label.pack(pady=10)
		last_login_frame.pack(pady=30)


		#expense_add_frame.grid(row=3, column=0)

		#add_expense_label.pack()
		#test.grid(row=2, column=0)