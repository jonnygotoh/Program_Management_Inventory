from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import db_conn.db as datab
import system as sys

current_session = sys.Login()

class Main :
	def __init__(self, root) :
		self.root = root
		self.login_page()
		
	def login_page(self) :
		self.clear_window()

		self.root.title("Login Page")
		self.root.geometry("450x270")

		ttk.Label(self.root, text="Username:").pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:").pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Login", command=self.login_process).pack(pady=15)

	def login_process(self) :
		username = self.entry_username.get()
		password = self.entry_password.get()

		if username != "" and password != "" :
			stat_login = current_session.login_user(username,password)

			if stat_login == True :
				messagebox.showinfo("Success", f"Welcome {current_session.user_name}!")
				self.open_main_window()

			else :
				messagebox.showerror("Failed", "Invalid username or password")
		else :
			messagebox.showerror("Failed", "The textbox is empty please login or register first")
		
	def open_main_window(self):
		self.clear_window()

		self.root.title("Dashboard")
		self.root.geometry("650x350")

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('1.TButton',foreground = 'white',background = 'black',padding = 5)
		style.configure('2.TButton',foreground = 'white',background = '',padding = 5)
		style.configure('Warna.TFrame', background = 'black')
		style.configure('Side.TFrame')

		top_frame = ttk.Frame(self.root, style = 'Warna.TFrame')
		top_frame.pack(fill="x", pady=0,)

		ttk.Label(top_frame,
		          text=f'Manajemen Inventory',background= 'black',foreground='White',
		          font=("times new roman", 30, 'bold')).pack(side="left", padx=10)

		ttk.Button(top_frame, text="Logout",style= '1.TButton', command=self.logout).pack(side="right", padx=10)
# ==================================================================================
		sub_frame = ttk.Frame(self.root, style = 'Side.TFrame',width= '200')
		sub_frame.pack(side= 'left', fill= 'y')

		self.logo = PhotoImage(file='logo.png')
		imageLabel = ttk.Label(sub_frame, image= self.logo)
		imageLabel.pack()

		menu = ttk.Label (sub_frame, text= 'MENU', font= ('times new roman', 30 ,'bold'),background='green',anchor='center')
		menu.pack(fill='x')

		ttk.Button(sub_frame, text='Inventory',command=self.barang_gudang).pack(fill= 'x')

	def barang_gudang(self):
		self.clear_window()

		

	# 	self.table = ttk.Treeview(self.root, columns=('id','nama','status',), show="headings")
	# 	self.table.heading("No", text="No")
	# 	self.table.heading("Npm", text="Npm")
	# 	self.table.heading("Nama", text="Nama")
	# 	self.table.heading("Prodi", text="Prodi")
	# 	self.table.heading("Edit", text="Edit")
	# 	self.table.heading("Delete", text="Delete")

	# 	self.table.column("No", width=50)
	# 	self.table.column("Npm", width=100, anchor="center")
	# 	self.table.column("Nama", width=100, anchor="center")
	# 	self.table.column("Prodi", width=100, anchor="center")
	# 	self.table.column("Edit", width=100, anchor="center")
	# 	self.table.column("Delete", width=100, anchor="center")

	# 	self.table.pack(fill="both", expand=True)
	# 	self.table.bind("<ButtonRelease-1>", self.on_table_click)
	# 	self.load_table_data()


	# def load_table_data(self):
	# 	for row in self.table.get_children():
	# 		self.table.delete(row)

	# 	all_mahasiswa = data.get_all_mahasiswa()
	# 	i = 1
	# 	for mahasiswa in all_mahasiswa:
	# 		self.table.insert("", END, values=(i, mahasiswa.npm_mahasiswa, mahasiswa.nama_mahasiswa, mahasiswa.nama_prodi, "Edit", "Delete"))
	# 		i+= 1


	# def add_user_window(self) :
	# 	print("If possible coba dibuat disini")

	# def on_table_click(self, event):
	# 	item = self.table.identify_row(event.y)
	# 	column = self.table.identify_column(event.x)

	# 	if not item:
	# 		return

	# 	_,npm_mahasiswa,_, _, _, _ = self.table.item(item, "values")

	# 	if column == "#5":  
	# 		print(f"Edit {npm_mahasiswa}")
	# 	elif column == "#6":
	# 		print(f"Delete {npm_mahasiswa}")


	def logout(self):
		current_session.logout()
		messagebox.showinfo("Info", "Logged out successfully")
		self.login_page()

	def clear_window(self):
		for widget in self.root.winfo_children():
			widget.destroy()


# ---------- RUN APP ----------
if __name__ == "__main__":
	root = Tk()
	app = Main(root)
	root.mainloop()