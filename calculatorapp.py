"""
calculator_app.py
S.T.R Pandiyan
21/10/2017
"""

from Tkinter import *
from tkMessageBox import *
import os
import ttk
import sqlite3
import operator
import webbrowser

op=None
root=None
	
class calculator:
	
	def gui(self):
		
		"""
		This is the Graphical User Interface function.
		It is initialised first of all other functions, using this class's object
		"""
		
		root=Tk() 
		root.title("Calculator")
		root.resizable(width=False, height=False)
		
		self.first_var=StringVar()		# StringVar function holder of the first variable
		self.second_var=StringVar()	# StringVar function holder of the second variable
		self.text=StringVar()				# StringVar function holder of the answer holding variable
	
		menubar=Menu(root)
		mainmenu=Menu(menubar)
		
		menubar.add_cascade(label='More',menu=mainmenu)
		mainmenu.add_command(label='Help',command=self.help)
		
		submenu1=Menu(mainmenu)
		submenu1.add_command(label="About this software",command=self.about_sw)
		submenu1.add_command(label="About the developer",command=self.about_dev)
		submenu1.add_command(label="About our company",command=self.about_company)
		mainmenu.add_cascade(label='About',menu=submenu1)
		
		submenu2=Menu(mainmenu)
		submenu2.add_command(label="Contact developer",command=self.contact_dev)
		submenu2.add_command(label="Contact Aptusweb",command=self.contact_aptusweb)
		mainmenu.add_cascade(label='Contact us',menu=submenu2)
		
		parent_frame=Frame(root)
		parent_frame.grid(padx=10,pady=10,sticky=E+W+N+S)
		
		Entry_box_frame=Frame(parent_frame,relief=GROOVE,borderwidth=2,bg="black")
		L1=Label(Entry_box_frame,text="Enter the First number :",bg="black",fg="white")
		self.first_input_box=Entry(Entry_box_frame,textvariable=self.first_var)		
		self.first_input_box.focus()
		L2=Label(Entry_box_frame,text="Enter the Second number :",bg="black",fg="white")
		self.second_input_box=Entry(Entry_box_frame,textvariable=self.second_var)
		L3=Label(Entry_box_frame,text="\t",bg="black")
		L4=Label(Entry_box_frame,text="\t",bg="black")
		L5=Label(Entry_box_frame,text=" the answer is :",bg="black",fg="white")
		self.answer_box= Entry(Entry_box_frame,textvariable=self.text,state=DISABLED)
		
		L1.grid(row=0,column=0,sticky=W)
		self.first_input_box.grid(padx=10,pady=10,row=1,column=0)
		L2.grid(row=2,column=0,sticky=W)
		self.second_input_box.grid(padx=10,pady=10,row=3,column=0)
		L3.grid(row=4,column=0,sticky=W)
		L4.grid(row=5,column=0,sticky=W)
		L5.grid(row=6,column=0,sticky=W)
		self.answer_box.grid(padx=10,pady=10,row=7,column=0)
		
		
		Button_frame=Frame(parent_frame)
		addition=Button(Button_frame,text="Add",command=self.add,relief=SOLID,borderwidth=3)
		subtraction=Button(Button_frame,text="Subtract",command=self.sub,relief=SOLID,borderwidth=3)
		multiplication=Button(Button_frame,text="Multiply",command=self.mul,relief=SOLID,borderwidth=3)
		division=Button(Button_frame,text="Divide",command=self.div,relief=SOLID,borderwidth=3)
		modulo=Button(Button_frame,text="Modulo",command=self.mod,relief=SOLID,borderwidth=3)
		addition.grid(padx=10,pady=10,row=1,column=1) 
		subtraction.grid(padx=10,pady=10,row=3,column=1)
		multiplication.grid(padx=10,pady=10,row=5,column=1) 
		division.grid(padx=10,pady=10,row=7,column=1) 
		modulo.grid(padx=10,pady=10,row=9,column=1)
		
		Entry_box_frame.grid(row=0,column=1,padx=5,pady=5)
		Button_frame.grid(row=0,column=2,padx=5,pady=5)
		clear=Button(parent_frame,text="Clear Boxes",command=self.clean_it,relief=GROOVE,borderwidth=3)
		clear.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
		s = ttk.Separator(parent_frame, orient=HORIZONTAL)
		s.grid(row=2,column=1,columnspan=2,sticky=E+W)
		sty=ttk.Style(parent_frame)
		sty.configure("TSeparator",background="red")
		bottom_label=Label(parent_frame, text="Powered by Aptusweb Incorp.",fg="blue",cursor="hand2")
		bottom_label.grid(row=3,column=1,columnspan=2)
		bottom_label.bind("<Button-1>",self.callback)
		root.config(menu=menubar)
		root.iconbitmap(r'favicon.ico')
		root.mainloop()
	
	def help(self):
		showinfo("Help","Just enter any two numebers of your choice, and click the button on the side as per the operations that you want to perform.")
	
	def about_sw(self):
		showinfo("About this application"," This is a simple Calculator Application coded completely in Python .\n\nIt can perform operations like :-\n\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Modulo")
		
	def about_dev(self):
		showinfo("About the Developer","This Calculator Aplication is coded by S.T.R Pandiyan from Aptusweb")
	
	def about_company(self):
		showinfo("About Company","We are providing IT services from 2016 to present")
	
	def contact_dev(self):
		showinfo("Contact Developer","Phone no. :  8220994448\nGmail ID : becool.pandiyan@gmail.com")
		
	def contact_aptusweb(self):
		showinfo("Contact Atusweb","Phone no. : 1234567890\nGmail ID : aptusweb2016@gmail.com")
		
	def callback(self,event):
		webbrowser.open_new(r"www.aptusweb.com")
	
	def add(self):	
		op='ADDITION'
		try:
			self.a=float(self.first_var.get())
			self.b=float(self.second_var.get())
			cal.printer(operator.add(self.a,self.b))
			cal.SQLite_database_operaton_performer(op,operator.add(self.a,self.b))
		except ValueError:
			showerror("Invalid Input","The Input you have entered is Invalid.\n Please enter a integer or fractional number.")
			cal.clean_it()

	def sub(self):
		op='SUBTRACTION'
		try:
			self.a=float(self.first_var.get())
			self.b=float(self.second_var.get())
			cal.printer(operator.sub(self.a,self.b))
			cal.SQLite_database_operaton_performer(op,operator.sub(self.a,self.b))
		except ValueError:
			showerror("Invalid Input","The Input you have entered is Invalid. \nPlease enter a integer or fractional number.")
			cal.clean_it()
			
	def mul(self):
		op='MULTIPLICATION'
		try:
			self.a=float(self.first_var.get())
			self.b=float(self.second_var.get())
			cal.printer(operator.mod(self.a,self.b))
			cal.SQLite_database_operaton_performer(op,operator.mod(self.a,self.b))
		except ValueError:
			showerror("Invalid Input","The Input you have entered is Invalid. \nPlease enter a integer or fractional number.")
			cal.clean_it()
			
	def mod(self):
		op='MODULO'
		try:
			self.a=float(self.first_var.get())
			self.b=float(self.second_var.get())
			cal.printer(operator.mod(self.a,self.b))
			cal.SQLite_database_operaton_performer(op,operator.mod(self.a,self.b))
		except ValueError:
			showerror("Invalid Input","The Input you have entered is Invalid. \nPlease enter a integer or fractional number.")
			cal.clean_it()
		
	def div(self):
		op='DIVISION'
		try:
			self.a=float(self.first_var.get())
			self.b=float(self.second_var.get())
			cal.printer(operator.div(self.a,self.b))
			cal.SQLite_database_operaton_performer(op,operator.div(self.a,self.b))
		except ValueError:
			showerror("Invalid Input","The Input you have entered is Invalid. Please enter a integer or fractional number.")
			cal.clean_it()
		
	def printer(self,answer):
		self.answer_box.config(state=NORMAL)
		self.answer_box.delete(0,'end')
		self.answer_box.insert('end',answer)
		self.answer_box.config(state=DISABLED)

	def clean_it(self):
		self.first_input_box.delete(0,'end')
		self.second_input_box.delete(0,'end')
		self.answer_box.config(state=NORMAL)
		self.answer_box.delete(0,'end')
		self.answer_box.config(state=DISABLED)
		
	def SQLite_database_operaton_performer(self,op,answer):		
		if os.path.isdir("C:\Aptusweb Incorp\Desktop application\Calculator"):
			connection=sqlite3.connect("appdb")
			cursor=connection.cursor()
			if not os.path.isfile("C:\Aptusweb Incorp\Desktop application\Calculator\\appdb"):				
				os.chdir("C:\Aptusweb Incorp\Desktop application\Calculator")
				cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, first_input_value FLOAT,second_input_value FLOAT,operation_performed TEXT, Output FLOAT)''')
				cursor.execute('''INSERT INTO users(first_input_value,second_input_value,operation_performed,Output)VALUES(?,?,?,?)''', (self.a,self.b,op,answer))
			else:
				cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, first_input_value FLOAT,second_input_value FLOAT,operation_performed TEXT, Output FLOAT)''')
				cursor.execute('''INSERT INTO users(first_input_value,second_input_value,operation_performed,Output)VALUES(?,?,?,?)''', (self.a,self.b,op,answer))
		else:
			if not os.path.isdir("C:\Aptusweb Incorp"):
				os.mkdir("C:\Aptusweb Incorp")
			if not os.path.isdir("C:\Aptusweb Incorp\Desktop Application"):
				os.mkdir("C:\Aptusweb Incorp\Desktop Application")
			if not os.path.isdir("C:\Aptusweb Incorp\Desktop Application\Calculator"):
				os.mkdir("C:\Aptusweb Incorp\Desktop Application\Calculator")
			os.chdir("C:\Aptusweb Incorp\Desktop Application\Calculator")
			connection=sqlite3.connect("appdb")
			cursor=connection.cursor()
			cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, first_input_value FLOAT,second_input_value FLOAT,operation_performed TEXT, Output FLOAT)''')
			cursor.execute('''INSERT INTO users(first_input_value,second_input_value,operation_performed,Output)VALUES(?,?,?,?)''', (self.a,self.b,op,answer))
		connection.commit()
		connection.close()

if __name__ == "__main__":
	cal=calculator()
	cal.gui()

# this is the end of the calculator_app python program. happy coding....!!