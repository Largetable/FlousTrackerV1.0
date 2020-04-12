import tkinter as tk
from tkinter import E,W,S,N
from tkinter import ttk
import datetime
import sys
from db_check import Account_db
class Account(tk.Frame):
	def __init__(self, parent, attr):
		tk.Frame.__init__(self, parent)
		self.parent=parent
		self.attr=attr
		self.config(bg='#aaf7f7')
		#####IMPORTANT LINEEE 
		session=Account_db(self, attr)
		session.create_expense_table()
		session.create_users_expenses_table()
		#session.create_session_table()

		##################
		frame1=tk.Frame(self, width=450, height=500, bg='#aaf7f7')
		frame2=tk.Frame(self, width=450, height=500, bg='#aaf7f7')
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		frame1.grid(row=0, column=0, sticky=N+S+W+E)
		frame2.grid(row=0, column=1, sticky=N+S+W+E)
		######################### FRAME 1

		last_login_frame=tk.Frame(frame1, width=350, height=300,bg='white')
		welcome_label=tk.Label(frame1, text='Welcome {} ! '.format(attr), font=("Courier", 18), fg='blue')
		estim_cash_label=tk.Label(frame1, text='Estimated cash: {}'.format(session.get_cash()), fg='green', font=("Courier",16))
		#cash_value_label=tk.Label(frame1, text= "CASHDT",bg='green', font=("Courier",18))

		expense_add_frame=tk.Frame(frame2, width = 400, height= 300, bg='white' )


		welcome_label.pack(pady=20)
		estim_cash_label.pack(pady=10)
		last_login_frame.pack(pady=30)
		######################## FRAME 2
		cash_frame=tk.Frame(frame2, width=300, height=100, bg='white' )
		add_expense_frame=tk.Frame(frame2, width=400, height= 300, bg='white')

		cash_frame.pack(pady=20)
		add_expense_frame.pack(pady=10)
		####################### cash_frame
		add_cash_label=tk.Label(cash_frame, text="Add your cash:", font=("Courier",15))
		add_cash_entry=ttk.Entry(cash_frame)
		add_cash_button=ttk.Button(cash_frame, text="Add cash!", command = lambda : session.add_cash(add_cash_entry.get()))

		reset_cash_label=tk.Label(cash_frame, text="Reset your cash:", font=("Courier",15))
		reset_cash_entry=ttk.Entry(cash_frame)
		reset_cash_button=ttk.Button(cash_frame, text="Reset cash!", command = lambda : session.reset_cash(reset_cash_entry.get()))

		add_cash_label.grid(row=0, column=0, rowspan=2,  padx=5, pady=5)
		add_cash_entry.grid(row=0, column=1,rowspan=2, padx=5, pady=5)
		add_cash_button.grid(row=0,column=2, rowspan=2,sticky=E, pady=5)

		reset_cash_label.grid(row=2, column=0, rowspan=2, padx=5, pady=5)
		reset_cash_entry.grid(row=2, column=1, rowspan=2, padx=5, pady=5)
		reset_cash_button.grid(row=2,column=2,rowspan=2,sticky=E, pady=5)
		####################### ADD_EXPENSE_FRAME


		categories=["Food", "Transport", "Education", "Phone/Internet bill", "Clothes",
						"Entertainment/Sport", "Gifts", "Going out", "Coffee shop", "Other" ]

		variable=tk.StringVar(self)
		variable.set(categories[0])

		add_expense_label=tk.Label(add_expense_frame, text="Add expense here!", font=("Courier",13), bg="red")
		category_option_menu=ttk.OptionMenu(add_expense_frame, variable, categories[0], *categories)  #categories[0] is required in ttk because it will show the default option
		expense_value_entry=ttk.Entry(add_expense_frame, width="13")
		self.expense_value_entry=expense_value_entry
		expense_description=tk.Text(add_expense_frame, width=20, height=10, font=("Courier",12))
		expense_description.insert(tk.INSERT, "Please insert a brief description here..")

		add_expense_button=ttk.Button(add_expense_frame, text="Add expense!", 
		 command = lambda : session.add_expense(expense_value_entry.get(),
		  variable.get(), expense_description.get("1.0",'end-1c'), datetime.datetime.today().strftime('%d%m%y')))

		add_expense_label.grid(row=0, column=0, sticky=E, padx=50, pady=20)
		category_option_menu.grid(row=1, column=0, padx=30, pady=5, sticky=W)
		expense_value_entry.grid(row=1, column=0, padx=10, pady=5, sticky=E)
		expense_description.grid(row=2, column=0, padx=20, pady=20)
		add_expense_button.grid(row=3,pady=5)

		########################### LAST TIME ADDED EXPENSE FRAME
		last_expense_label=tk.Label(last_login_frame, text="Informations about your last session!", font=("Courier",13))
		last_expense_label.grid(row=0, column=0, sticky=E, padx=50, pady=20)
		if (session.get_last_login_date() == 'NULL'):
			tk.Label(last_login_frame, text= """There is currently no informations to display.. \n please fill in with data first \n
				then re-login """, font=("Courier",13)).grid(row=1, sticky=S)

		else:
			print("INSIDE ELSE NOW")
			categories_values=session.get_last_categories_values()
			if (len(categories_values) == 0) :
				tk.Label(last_login_frame, text="Total expenses: 0", font=("Courier",12)).grid(row=1, padx=30, pady=5)
				tk.Label(last_login_frame, text="You didn't add any expense on your last login", font=("Courier",12)).grid(row=2, pady=5)
			else:
				categories=list(categories_values.keys())
				values=list(categories_values.values())

				last_expenses_total=tk.Label(last_login_frame, text="Total expenses: {}".format(sum([float(i) for i in values])), font=("Courier",12))  #ADD METHOD TO GET TOTAL LAST EXPENSES
				last_expenses_total.grid(row=1, padx=30, pady=5 )
				last_expenses_detailed_label=tk.Label(last_login_frame, text="Expenses in details..", font=("Courier",15))
				last_expenses_detailed_label.grid(row=2, pady=5)
				print("Categories = {}".format(categories))
				print("values = {}".format(values))
				for i in range(len(categories_values)):
					tk.Label(last_login_frame, text=categories[i], font=("Courier",13)).grid(row=3+i, column=0, padx=30, pady=5, sticky=W, )
					tk.Label(last_login_frame, text=values[i], font=("Courier",13)).grid(row=3+i, column=0, pady=5, padx=20)
		ttk.Button(frame1, text="Quit", command = lambda : session.save_last_login_date()).pack()

	def refresh_page(self):
		self.destroy()
		self.parent.switch_frame(Account, self.attr)
