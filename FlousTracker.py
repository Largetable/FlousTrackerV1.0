import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from db_check import Registering, Logging
from home_page import HomePage
from account_page import Account


green='#229954'
blue='#2980b9'
blue_marine='#283747'
red='#b03a2e'
yellow='#f1c40f'
orange='#dc7633'
gray='#85929e'
azra9_feta7='		'
LARGE_FONT = ("Verdana", 10)

class FlousTracker(tk.Tk):	
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self._frame = None				
		tk.Tk.title(self , "Flous tracker")
		tk.Tk.geometry(self ,"900x500")	
		self.switch_frame(HomePage, None)
	def switch_frame(self, frame_class, attr):
		"""Destroys current frame and replaggggces it with a new one."""
		new_frame = frame_class(self, attr)
		if self._frame is not None and attr is not None:					
			self._frame.destroy()
			self.attr=attr
		self._frame = new_frame
		#self._frame.configure(width=500, height=900)'#aaf7f7'
		self._frame.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":	
	app = FlousTracker()
	app.mainloop()