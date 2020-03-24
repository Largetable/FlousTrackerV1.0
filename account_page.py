import tkinter as tk

class Account(tk.Frame):
	def __init__(self, parent, attr):
		tk.Frame.__init__(self, parent)
		self.parent=parent
		self.attr=attr
		#self.user_var=user_var
		print('hello')
		print('USERNAME = '+attr)
		#print(user_var['name'])
		#frame1=tk.Frame(self, width=900, height=600, bg='#eafaf1')
		#frame1.configure(bg='WHITE')
		#frame1.place(x=0,y=0)
		label=tk.Label(self, text='USEERNAME = ', bg='BLACK')
		label.place(x=50, y=100)



