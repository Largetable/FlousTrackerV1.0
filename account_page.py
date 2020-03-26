import tkinter as tk
from tkinter import E,W,S,N
from tkinter import ttk

class Account(tk.Frame):
	def __init__(self, parent, attr):
		tk.Frame.__init__(self, parent)
		self.parent=parent
		self.attr=attr
		self.config(bg='#aaf7f7')
		#main_frame=tk.Frame(self, width=900, height=500, bg='red')
		#main_frame.place(x=0,y=0)

		##################
		frame1=tk.Frame(self, width=450, height=500, bg='black')
		frame2=tk.Frame(self, width=450, height=500, bg='blue')
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		frame1.grid(row=0, column=0, sticky=N+S+W+E)
		frame2.grid(row=0, column=1, sticky=N+S+W+E)
#		######################### FRAME 1

		last_login_frame=tk.Frame(frame1, width=350, height=300,bg='white')
		welcome_label=tk.Label(frame1, text='Welcome {} ! '.format(attr), font=("Courier", 18), fg='blue')
		estim_cash_label=tk.Label(frame1, text='Estimated cash: $$$$$', fg='green', font=("Courier",18))
		#cash_value_label=tk.Label(frame1, text= "CASHDT",bg='green', font=("Courier",18))

		expense_add_frame=tk.Frame(frame2, width = 400, height= 300, bg='white' )
		test=tk.Label(self, text="TEST")
		#self.grid_columnconfigure(0, weight=1)
		#self.grid_columnconfigure(1, weight=1)
		#self.grid_columnconfigure(2, weight=1)
		#self.grid_rowconfigure(1, weight=2)'
		welcome_label.pack(pady=20)
		estim_cash_label.pack(pady=10)
		last_login_frame.pack(pady=30)
		######################## FRAME 2
		add_cash_frame=tk.Frame(frame2, width=300, height=100, bg='white' )
		add_expense_frame=tk.Frame(frame2, width=400, height= 300, bg='white')

		add_cash_frame.pack(pady=20)
		add_expense_frame.pack(pady=10)
		####################### ADD_CASH_FRAME
		add_cash_label=tk.Label(add_cash_frame, text="Add your cash here:", font=("Courier",15))
		add_cash_entry=ttk.Entry(add_cash_frame)
		add_cash_button=ttk.Button(add_cash_frame, text="Add cash!")


		add_cash_label.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
		add_cash_entry.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
		add_cash_button.grid(row=2,column=0, sticky=E, pady=5)
		####################### ADD_EXPENSE_FRAME
		categories=["Food", "Transport", "Education", "Phone/Internet bill", "Clothes",
						"Entertainment/Sport", "Gifts", "Going out", "Other.." ]

		variable=tk.StringVar(self)
		variable.set(categories[0])

		add_expense_label=tk.Label(add_expense_frame, text="Add expense here!", font=("Courier",13), bg="red")
		category_option_menu=tk.OptionMenu(add_expense_frame, variable, *categories)
		expense_value_entry=tk.Entry(add_expense_frame, width="13")
		description_text=tk.Text(add_expense_frame, width=20, height=10, font=("Courier",12))
		description_text.insert(tk.INSERT, "Please insert a brief description here..")
		add_expense_button=tk.Button(add_expense_frame, text="Add expense!")

		add_expense_label.grid(row=0, column=0, sticky=E, padx=50, pady=20)
		category_option_menu.grid(row=1, column=0, padx=10, pady=5, sticky=W)
		expense_value_entry.grid(row=1, column=0, padx=10, pady=5, sticky=E)
		description_text.grid(row=2, column=0, padx=20, pady=20)
		add_expense_button.grid(row=3,pady=5)


		'''col_count, row_count = self.grid_size()
		for col in range(col_count):
			self.grid_columnconfigure(col, minsize=20)
		for row in range(row_count):
			self.grid_rowconfigure(row, minsize=20)'''




		#expense_add_frame.grid(row=4)
		#expense_add_frame.grid(row=3, column=0)

		#add_expense_label.pack()
		#test.grid(row=2, column=0)