#!/usr/bin/env python
"""
tktest.py

A simple Tkinter test.

"""

from tkinter import *
from tkinter.ttk import *

class App(Frame):
	def __init__(self, master=None):
		super(App, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.quit_button = Button(self, text="Quit", command=self.quit)
		self.quit_button.grid()


app = App()
app.master.title("Sample Application")
app.mainloop()
