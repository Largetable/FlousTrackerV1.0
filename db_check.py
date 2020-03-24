import sqlite3

class Registering:
	def __init__(self, username, password ):
		self.username=username
		self.password=password

	def create(self):
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()

		c.execute('''CREATE TABLE users(
			ID TEXT PRIMARY KEY ,
			PASSWORD TEXT NOT NULL
			);''')
		print("Table created successfully")
		conn.commit()
		conn.close()
		print("Database closed successfully")

	def check(self):
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()
		print("Checking if username taken or not .... ")
		c.execute("SELECT ID FROM users WHERE ID = (?)" , (self.username,))
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
		c.execute("INSERT INTO users VALUES (:id, :password)",{'id' :self.username , 'password' : self.password})
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
		c.execute("SELECT ID FROM users WHERE ID = (?)" , (self.username,))
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
		c.execute("SELECT PASSWORD FROM users WHERE ID = (?)", (self.username,))
		aux=c.fetchone()[0]
		conn.commit()
		conn.close()
		print("Database closed succefully")
		return aux==self.password

class Account_db:
	def __init__(self, username):
		self.username=username

	def create_expense_table(self):
		print("Creating Expense table..")
		conn = sqlite3.connect('money_tracker.db')
		print("Database opened successfully")
		c=conn.cursor()

		c.execute('''CREATE TABLE expenses(
			EXPENSE_ID TEXT PRIMARY KEY ,
			EXPENSE_VALUE TEXT NOT NULL ,
			EXPENSE_CATEGORY TEXT NOT NULL ,
			EXPENSE_DATE TEXT NOT NULL
			);''')
		print("Expenses table created successfully")
		conn.commit()
		conn.close()
		print("Database closed successfully")
