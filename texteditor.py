import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Menubar:
	def __init__(self,parent):
		fonts = ('ubuntu', 12)
		menubar = tk.Menu(parent.tedit, font=fonts)#determines position of menubar
		parent.tedit.config(menu = menubar)#creates menubar
		dropdown = tk.Menu(menubar, tearoff=0, font=fonts)#tearoff used to separate menus from menubar
		menubar.add_cascade(label="File", menu=dropdown)#add name to the dropdownmenu
		dropdown.add_command(label="New file", command = parent.new_file,accelerator='Ctrl+N')
		dropdown.add_command(label="Open file", command = parent.open_file,accelerator='Ctrl+O')
		dropdown.add_command(label="Save", command = parent.save_file,accelerator='Ctrl+S')
		dropdown.add_command(label="Save As", command = parent.save_as_file,accelerator='Ctrl+Shift+S')
		dropdown.add_separator()
		dropdown.add_command(label="Exit", command = parent.tedit.destroy,accelerator='Ctrl+W')
		about_dropdown = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="About", menu=about_dropdown)
		about_dropdown.add_command(label='Release notes', command = self.release_message)
		about_dropdown.add_separator()
		about_dropdown.add_command(label='About',command = self.about_message)
		
	def about_message(self):
		box_title="About texteditor"
		box_message="A simple python texteditor"
		messagebox.showinfo(box_title, box_message)

	def release_message(self):
		box_title="About texteditor"
		box_message="A simple python texteditor"
		messagebox.showinfo(box_title, box_message)
	
class Statusbar:
	def __init__(self,parent):
		self.status = tk.StringVar()
		self.status.set("Construction Ahead!")				
		label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="grey", anchor="sw")
#		label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="grey", anchor="se")
		label.pack(side=tk.BOTTOM, fill=tk.BOTH)
		

class Textarea:
	def __init__(self,tedit):
		tedit.title("SHUBH's text Editor")
		tedit.geometry("1200x700")#defines size of text editor	
		fonts = ('ubuntu', 12) #font specification
		
		self.tedit = tedit
		self.filename = None
		self.textarea = tk.Text(tedit, font = fonts) #initialize textarea
		self.scrollbar = tk.Scrollbar(tedit, command = self.textarea.yview) #initialize scrollbar in Ydirec
		self.textarea.configure(yscrollcommand = self.scrollbar.set) #initialize scrollbar using mouse in Ydirec
		self.textarea.pack(side = tk.LEFT, expand=True, fill=tk.BOTH) #fill:size of textarea, exapnd:covers entire screen
		self.scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
		self.shortcuts()
		self.menubar = Menubar(self)
		self.statusbar = Statusbar(self)
		
		
	def window_title(self,name=None,*args):
		if name:
			self.tedit.title(name+"My text Editor")
		else:
			self.tedit.title("My text Editor")

               
	def new_file(self,*args):
		self.textarea.delete(1.0, tk.END)
		self.window_title()


	def open_file(self,*args):
		self.filename = filedialog.askopenfilename(
		defaultextension=".txt",
		filetypes=[("All files","*.*"),
			("Java files","*.java"),
			("C files","*.c"),
		    	("Python scripts","*.py"),
		    	("CSS documents","*.css"),
		    	("Html documents","*.html")])
		if self.filename:
			self.textarea.delete(1.0,tk.END)
			with open(self.filename,'r') as fn:	
				self.textarea.insert(1.0,fn.read())
			self.window_title(self.filename)
			
			
	def save_file(self,*args):
		if self.filename:
			try:
				text_content = self.textarea.get(1.0, tk.END)	
				with open(self.filename, 'w') as fh:
					fh.write(text_content)
				self.statusbar.update_status(True)
			except Exception as e:
				print(e)
		else:
			self.save_as_file()
	
	def save_as_file(self,*args):
		try:
			new_file = filedialog.asksaveasfilename(
			initialfile = "Untitled.txt",
			defaultextension=".txt",
			filetypes=[("All files","*.*"),
				("Java files","*.java"),
				("C files","*.c"),
			    	("Python scripts","*.py"),
			    	("CSS documents","*.css"),
			    	("Html documents","*.html")])
			text_content = self.textarea.get(1.0, tk.END)
			with open(new_file,'w') as f:
				f.write(text_content)
			self.window_title(new_file)
			self.filename = new_file
			self.statusbar.update_status(True)
		except Exception as e:
			print(e)
		
	def exit(self,*args):
		answer = messagebox.askyesno('Question','Do you really want to quit?')
		if answer == True:
			self.tedit.destroy()
		
		
	def shortcuts(self):	
		self.textarea.bind('<Control-n>', self.new_file)
		self.textarea.bind('<Control-o>', self.open_file)
		self.textarea.bind('<Control-s>', self.save_file)
		self.textarea.bind('<Control-S>', self.save_as_file)
		self.textarea.bind('<Control-w>', self.exit)
#		self.textarea.bind('<Key>', self.statusbar.update_status)

		
if __name__ == '__main__':
	tedit = tk.Tk()
	pt = Textarea(tedit)
	tedit.mainloop()
	
	
	
