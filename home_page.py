import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_check import Registering, Logging
from account_page import Account


green='#229954'
blue='#2980b9'
blue_marine='#283747'
red='#b03a2e'
yellow='#f1c40f'
orange='#dc7633'
gray='#85929e'
azra9_feta7='#aaf7f7'
LARGE_FONT = ("Verdana", 10)

class HomePage(tk.Frame):
	def __init__(self, parent, attr=None):
		tk.Frame.__init__(self, parent)
		self.parent=parent

		#DECLARATION OF BOTH FRAMES FOR LOGIN AND REGISTRATION
		register_frame = tk.Frame(self,  bg= '#f7f3aa' , width=450, height=500)
		register_frame.grid(row=0, column=0)
		login_frame = tk.Frame(self,  bg='#e9ff8f', width=450, height=500)
		login_frame.grid(row=0, column=1)
		#



		#REGISTRATION PAGE 
		register_label = tk.Label(register_frame, text='Registration page', width=23, font = LARGE_FONT, fg='BLACK', bg='#f7f3aa')
		register_label.config(font=("Courier", 20))
		register_label.place(x=50, y=50)
		#username used in registration
		username_label=tk.Label(register_frame, text='Username :', width=15,fg= 'GREEN', bg='#f7f3aa')
		username_label.config(font=("Courier", 15))
		username_label.place(x=60, y=200)

		username_get=ttk.Entry(register_frame)
		self.username_get=username_get
		username_get.place(x=250, y=205)
		#password used in regisration 
		password_label=tk.Label(register_frame, text='Password :', width=15,fg= 'GREEN', bg='#f7f3aa')
		password_label.config(font=("Courier", 15))
		password_label.place(x=60, y=250)

		password_get=ttk.Entry(register_frame)
		self.password_get=password_get
		password_get.place(x=250, y=255)

		#confirmation password used in regisration
		passconfirm_label=tk.Label(register_frame, text='Confirm Password :', width=18,fg= 'GREEN', bg='#f7f3aa')
		passconfirm_label.config(font=("Courier", 15))
		passconfirm_label.place(x=60, y=300)

		passconfirm_get=ttk.Entry(register_frame)
		self.passconfirm_get=passconfirm_get
		passconfirm_get.place(x=300, y=305)
		#

		register_button = ttk.Button(register_frame, text='Submit', command = lambda : self.regist(username_get.get(), password_get.get(), passconfirm_get.get()))
		register_button.place(x=200, y=375)



		##############LOGIN PAGE (frame)#######################
		login_label = tk.Label(login_frame, text='Login Page', font = LARGE_FONT, width=23, fg='BLACK', bg='#e9ff8f')
		login_label.config(font=("Courier",20))
		login_label.place(x=50, y=50)

		#username used in login
		userlogin_label=tk.Label(login_frame, text='Username :', width=15,fg='#000cff', bg='#e9ff8f')
		userlogin_label.config(font=("Courier", 15))
		userlogin_label.place(x=60, y=200)

		userlogin_get=ttk.Entry(login_frame)
		self.userlogin_get=userlogin_get
		userlogin_get.place(x=250, y=205)

		#password used in login

		passlog_label=tk.Label(login_frame, text='Password :', width=15,fg= '#000cff', bg='#e9ff8f')
		passlog_label.config(font=("Courier", 15))
		passlog_label.place(x=60, y=250)

		passlog_get=ttk.Entry(login_frame)
		self.passlog_get=passlog_get
		passlog_get.place(x=250, y=255)
		#
 
		login_button = ttk.Button(login_frame, text='Login', command = lambda : self.login_db(userlogin_get.get(), passlog_get.get())) # adding controller is importanth here
		login_button.place(x=200, y=330)
		########################END##############################

	def regist(self, username, password, confirm_password):   # REGISTRATION BUTTON 
		if (len(username)==0) or (len(password)==0) or (len(confirm_password)==0):
			messagebox.showerror("Error!!", "All empty spaces must be filled!")
		else:
			if (len(username)<5):
				messagebox.showerror("Error", "Username must be atleast made from 5 caracters!")
			elif (len(password)<8):
				messagebox.showerror("Error", "Password must be made from atleast 8 caracters!")
			elif (password!=confirm_password):
				messagebox.showerror("Error", "Passwords doesn't match!")
			else:
				account_data=Registering(username, password )   # REGISTERING CLASS HERE THAT INTERACTS WITH THE DATABSE
				#account_data.create()
				if (account_data.check()!=None):
					messagebox.showerror("Error!", "Username already taken!")
				else:
					account_data.add()
					messagebox.showinfo("Success", "Account created successfully!")
					self.username_get.delete(0,'end')
					self.password_get.delete(0, 'end')
					self.passconfirm_get.delete(0, 'end')


	def login_db(self, username, password):  # THIS IS THE LOGIN BUTTON 
		if (len(username)==0) or (len(password)==0):
			messagebox.showerror("Error!!", "All empty spaces must be filled!")
		else:
			if (len(username)<5):
				messagebox.showerror("Error", "Username must be atleast made from 5 caracters!")
			elif (len(password)<8):
				messagebox.showerror("Error", "Password must be made from atleast 8 caracters!")
			else:
				login_try=Logging(username, password)     # LOGIN CLASS THAT INTERACTS WITH THE DATABASE
				if (login_try.exist()==None):
					messagebox.showerror("Error!", "Username doesn't exist!")
				else:
					if (login_try.passverif()==False):
						messagebox.showerror("Error", "Wrong password!")
					else: 
						self.parent.switch_frame(Account, username)
						messagebox.showinfo("Succes", "Login successful")