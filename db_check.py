import sqlite3
import datetime
import sys
import tkinter as tk
class Registering:
	def __init__(self, username, password ):
		self.username=username
		self.password=password

	def check(self):
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Checking if username taken or not .... ")
		c.execute("SELECT user_id FROM users WHERE user_id = (?)" , (self.username,))
		aux=c.fetchone()
		conn.commit()
		conn.close()
		print("Database closed successfully")
		return (aux)

	def add(self):
		conn= sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Adding username and password to DB ....")
		c.execute("INSERT INTO users VALUES (:user_id, :user_password, :user_cash, :user_last_login_date)" \
			,{'user_id' :self.username , 'user_password' : self.password,  'user_cash' : 0.0, 'user_last_login_date': 'NULL'})


		print("Username and password added successfully.")
		conn.commit()
		conn.close()
		print("Database closed successfully")

class Logging:
	def __init__(self, username, password):
		self.username=username
		self.password=password


	def exist(self):
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Checking if username exists or not .... ")
		c.execute("SELECT user_id FROM users WHERE user_id = (?)" , (self.username,))
		aux=c.fetchone()
		conn.commit()
		conn.close()
		print("Database closed successfully")
		return (aux)

	def passverif(self):
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Verifying if password is correct or not....")
		c.execute("SELECT user_password FROM users WHERE user_id = (?)", (self.username,))
		aux=c.fetchone()[0]    #USED [0] because fetchone returs a tuple (password,)
		conn.commit()
		conn.close()
		print("Database closed succefully")
		return aux==self.password

class Account_db:
	def __init__(self, parent,  username):
		self.username=username
		self.parent=parent
	def create_expense_table(self):
		print("Creating Expense table..")
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Attempting to create an expenses table")
		c.execute("""CREATE TABLE IF NOT EXISTS expenses(
			EXPENSE_ID TEXT PRIMARY KEY ,
			EXPENSE_VALUE TEXT NOT NULL ,
			EXPENSE_CATEGORY TEXT NOT NULL ,
			EXPENSE_DATE TEXT NOT NULL,
			EXPENSE_DESCRIPTION TEXT
			);""")
		print("Expenses table created successfully")
		conn.commit()
		conn.close()
		print("Database closed successfully")

	def create_users_expenses_table(self):
		print("Creating users_expenses table..")
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Attempting to create users_expenses")
		c.execute(""" CREATE TABLE IF NOT EXISTS users_expenses (
				user_id TEXT NOT NULL ,
				EXPENSE_ID TEXT NOT NULL ,
				FOREIGN KEY (user_id) REFERENCES users(user_id) ,
				FOREIGN KEY (EXPENSE_ID) REFERENCES expenses(EXPENSE_ID) ,	
				PRIMARY KEY (user_id, EXPENSE_ID)
			);""")
		print(" table created successfully")
		conn.commit()
		conn.close()
		print("Database closed successfully")
	def create_session_table(self):
		print("Creating sessions table..")
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Attempting to create sessions")
		c.execute(""" CREATE TABLE IF NOT EXISTS sessions (
				session_id TEXT PRIMARY KEY ,
				EXPENSE_ID TEXT NOT NULL ,
				FOREIGN KEY (user_id) REFERENCES users(user_id) ,
				FOREIGN KEY (EXPENSE_ID) REFERENCES expenses(EXPENSE_ID) ,	
				PRIMARY KEY (user_id, EXPENSE_ID)
			);""")
		print(" table created successfully")
		conn.commit()
		conn.close()
	print("Database closed successfully")

	def add_expense(self, value, category, description, date):

		if (len(value)==0):
			tk.messagebox.showerror("Error", "Please fill in with an expense value first.")
		else:
			print("Adding an expense..")
			conn=sqlite3.connect('money_tracker.db')
			print("Database opened successfully")

			c=conn.cursor()
			categories_numbers={"Food":'1', "Transport":'2', "Education":'3', "Phone/Internet bill":'4', "Clothes":'5', "Entertainment/Sport":'6', \
	 			"Gifts":'7', "Going out":'8', "Coffee shop":'9', "Other":'10'}
			num=self.total_number_expen()
			expense_id_v2=categories_numbers[category]+date+str(num)

			print('category nummber ={}'.format(categories_numbers[category]))
			print("ID = {}".format(categories_numbers[category]+date+str(num)))


			c.execute("""INSERT INTO expenses VALUES (:EXPENSE_ID, :EXPENSE_VALUE, :EXPENSE_CATEGORY,
				:EXPENSE_DATE, :EXPENSE_DESCRIPTION)""",{'EXPENSE_ID':(expense_id_v2), 'EXPENSE_VALUE':value, \
					'EXPENSE_CATEGORY':category, 'EXPENSE_DATE':date, 'EXPENSE_DESCRIPTION':description})

			c.execute("INSERT INTO users_expenses VALUES (:user_id, :EXPENSE_ID)", {'user_id':(self.username), 'EXPENSE_ID':(expense_id_v2)})
			print("Expense added successfully")
			c.execute("UPDATE users SET user_cash = user_cash - (?) WHERE user_id = (?) ", (value, self.username))
			conn.commit()
			conn.close()
			tk.messagebox.showinfo("Success!", "Expense added successfully!")
			print("Database closed successfully")
			self.parent.refresh_page()
			
	def add_expense_desc(self):
		print("ADDING EXPENSES DESCIRPTION")
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()
		c.execute("ALTER TABLE expenses ADD COLUMN EXPENSE_DESCRIPTION TEXT ")
		print("COLUMN ADDDDED")
		conn.commit()
		conn.close()

	def total_number_expen(self):
		print("Calculating total number of expenses:")
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()
		c.execute("SELECT * FROM expenses")
		n=len(c.fetchall())
		print("TOTAL NUMBER OF EXPENSE = {}".format(n))
		conn.commit()
		conn.close()
		return n

	def get_cash(self):
		print("Getting cash's value for this user : {}".format(self.username))
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()
		c.execute("SELECT user_cash FROM users WHERE user_id=(?)", (self.username, ))
		aux=c.fetchone()[0]
		print("USER CASH = {}".format(aux))
		conn.commit()
		conn.close()
		return aux

	def reset_cash(self, value):
		print("Reseting cash value!")
		if (len(value)==0):
			tk.messagebox.showerror("Error", "Please specify your cash value first.")
		else:
			conn=sqlite3.connect('money_tracker.db')
			c=conn.cursor()
			c.execute("UPDATE users SET user_cash = (?) WHERE user_id = (?)", (value, self.username))
			conn.commit()
			tk.messagebox.showinfo("Success!", "Your cash has been reset successfully!")
			print("cash reset.")
			conn.close()
		self.parent.refresh_page()

	def add_cash(self, value):
		print("Adding cash value!")
		if (len(value)==0):
			tk.messagebox.showerror("Error", "Please specify your cash value first.")
		else:
			conn=sqlite3.connect('money_tracker.db')
			c=conn.cursor()
			c.execute("UPDATE users SET user_cash = user_cash + (?) WHERE user_id= (?)", (value, self.username))
			conn.commit()
			tk.messagebox.showinfo("Success!", "{} DT has been added to your account.".format(value))
			print("Value added.")
			#self.username_get.delete(0,'end')
			#self.parent.parent.switch_frame(self.parent, self.username)
			conn.close()
		self.parent.refresh_page()

	def get_last_categories_values(self):
		print("getting dictionnary for categories and values")
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()

		c.execute("SELECT user_last_login_date FROM users WHERE user_id = (?)", (self.username, ))
		last_login_date=c.fetchall()[0][0]	
		c.execute("SELECT EXPENSE_ID FROM expenses WHERE EXPENSE_DATE=(?)", (last_login_date,))
		last_expense_ids=[ id[0]for id in c.fetchall()]
		c.execute("SELECT EXPENSE_ID FROM users_expenses WHERE user_id=(?) ", (self.username, ))
		ids=[id[0] for id in c.fetchall()]
		valid_expense_id=list (set(last_expense_ids) & set(ids))

		sql="SELECT EXPENSE_VALUE FROM expenses WHERE EXPENSE_ID IN ({seq})".format(
		    seq=','.join(['?']*len(valid_expense_id)))
		c.execute(sql, valid_expense_id)
		last_expense_values=[value[0] for value in c.fetchall()]

		sql="SELECT EXPENSE_CATEGORY FROM expenses WHERE EXPENSE_ID IN ({seq})".format(
		    seq=','.join(['?']*len(valid_expense_id)))
		c.execute(sql, valid_expense_id)
		last_expense_categories=[categ[0] for categ in c.fetchall()]

		categories_values=dict()
		for i in range(len(last_expense_categories)):
			categories_values[last_expense_categories[i]]=last_expense_values[i]

		conn.commit()
		conn.close()	
		print("PRINTING DICTIONNARY = {}".format(categories_values))	
		return categories_values
	def get_last_login_date(self):
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()
		c.execute("SELECT user_last_login_date FROM users WHERE user_id = (?)", (self.username, ))
		aux=c.fetchall()[0][0]
		conn.commit()
		conn.close()	
		return aux
	def save_last_login_date(self):
		conn=sqlite3.connect('money_tracker.db')
		c=conn.cursor()
		c.execute("UPDATE users SET user_last_login_date = (?) WHERE user_id = (?)", (datetime.datetime.today().strftime('%d%m%y'), self.username))
		print("last login date saved!")
		conn.commit()
		conn.close()	
		sys.exit()