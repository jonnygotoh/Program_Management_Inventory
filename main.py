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
		ttk.Button(self.root, text="Register", command=self.regis_page).pack(pady=15)

	def regis_page(self) :
		self.clear_window()

		self.root.title("Register Page")
		self.root.geometry("450x270")

		ttk.Label(self.root, text="Get Your Username Here").pack(pady=5)
		
		ttk.Label(self.root, text="New Username:").pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:").pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Register", command=self.regis_process).pack(pady=15)

	def regis_page(self) :
		self.clear_window()

		self.root.title("Register Page")
		self.root.geometry("450x270")

		ttk.Label(self.root, text="Get Your Username Here").pack(pady=5)
		
		ttk.Label(self.root, text="New Username:").pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:").pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Register", command=self.regis_process).pack(pady=15)

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

	def regis_process(self) :
		username = self.entry_username.get()
		password = self.entry_password.get()

		if username != "" and password != "" :
			stat_login = current_session.regis_user(username,password)

			if stat_login == True :
				messagebox.showinfo("Success", f"Your ID is created !")
				# self.open_main_window()

				self.login_page()

			else :
				messagebox.showerror("Failed", "Invalid input")
		else :
			messagebox.showerror("Failed", "The textbox is empty please login or register first")

		
	def open_main_window(self):
		self.clear_window()

		self.root.title("Dashboard")
		self.root.geometry("650x350")

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('1.TButton',foreground = 'white',background = 'black',padding = 5)
		style.configure('2.TButton',foreground = 'black',background = 'white',font = ('times new roman',25, 'bold'))
		style.configure('Warna.TFrame', background = 'black')
		style.configure('Side.TFrame')

		top_frame = ttk.Frame(self.root, style = 'Warna.TFrame')
		top_frame.pack(fill="x", pady=0,)

		ttk.Label(top_frame,
		          text=f'Manajemen Inventory',background= 'black',foreground='White',
		          font=('times new roman', 30, 'bold')).pack(side="left", padx=10)

		ttk.Button(top_frame, text='Logout',style= '1.TButton', command=self.logout).pack(side="right", padx=10)
# ==================================================================================
		sub_frame = ttk.Frame(self.root, style = 'Side.TFrame',width= '200')
		sub_frame.pack(side= 'left', fill= 'y')

		self.logo = PhotoImage(file='logo.png')
		imageLabel = ttk.Label(sub_frame, image= self.logo)
		imageLabel.pack()

		menu = ttk.Label (sub_frame, text= 'MENU', font= ('times new roman', 30 ,'bold'),background='green',anchor='center')
		menu.pack(fill='x')

		ttk.Button(sub_frame, text='Inventory',style = '2.TButton',command = self.barang_gudang).pack(fill= 'x')
		ttk.Button(sub_frame, text='Ruangan', style='2.TButton',command = self.Ruangan).pack(fill = 'x')
		ttk.Button(sub_frame, text='Kategori',style = '2.TButton',command = self.Kategori).pack(fill = 'x')

	def barang_gudang(self):
		self.clear_window()
		self.root.title ('Gudang')

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Warna.TFrame', background = 'black',foreground = 'white')
		style.configure('1.TButton',foreground = 'white',background = 'black',padding = 5)

		top_frame = ttk.Frame(self.root, style = 'Warna.TFrame')
		top_frame.pack(fill='x', pady=0,)

		ttk.Label(top_frame,
		          text=f'Storage',background='black',foreground='white',font=('times new roman', 30, 'bold')).pack(side="left", padx=10)
	
		ttk.Button(top_frame, text="Back",style= '1.TButton', command=self.open_main_window).pack(side="right", padx=10)
		
		self.table = ttk.Treeview(self.root, columns=('id_barang','kode_barang','nama_barang','status_barang',),show="headings")
		self.table.heading("id_barang",text="ID")
		self.table.heading("kode_barang",text="CODE")
		self.table.heading("nama_barang",text="NAMA")
		self.table.heading("status_barang",text="STATUS")

		self.table.column("id_barang",width=60)
		self.table.column("kode_barang",width=60, anchor="center")
		self.table.column("nama_barang",width=120, anchor="center")
		self.table.column("status_barang",width=60, anchor="center")

		self.table.pack(fill='both', expand=True, padx=10, pady=10)

		crud_frame = ttk.Frame(self.root,style = 'Warna.TFrame')
		crud_frame.pack(fill='x',side='bottom',pady=5,padx=10)

		ttk.Button(crud_frame, text='Add', style='1.TButton', command=self.tambah_barang).pack(side='left', padx=5)
		ttk.Button(crud_frame,text='Edit',style='1.TButton',command=self.edit_barang).pack(side = 'left',padx=5)
		ttk.Button(crud_frame, text='Delete', style='1.TButton', command=self.hapus_barang).pack(side='left', padx=5)
        
		self.load_inventory_data()

	def load_inventory_data(self):
		self.table.delete(*self.table.get_children())
		data = sys.tampilkan_barang()
		
		for row in data:
			self.table.insert('', 'end', values=row)

	def tambah_barang(self):
		self.crud = Toplevel(self.root)
		self.crud.title ('Tambah Barang')
		self.crud.geometry('400x250')
		self.crud.resizable(False,False)

		frame = ttk.Frame(self.crud, padding=10)
		frame.pack(fill='both', expand=True)

		ttk.Label(frame, text='Kode').pack(anchor='w')
		entry_kode = ttk.Entry(frame)
		entry_kode.pack(fill='x')

		ttk.Label(frame, text='Nama').pack(anchor='w')
		entry_nama = ttk.Entry(frame)
		entry_nama.pack(fill='x')

		ttk.Label(frame, text='Status').pack(anchor='w')
		entry_status = ttk.Entry(frame)
		entry_status.pack(fill='x')

		def submit():
			kode = entry_kode.get()
			nama = entry_nama.get()
			status = entry_status.get()
			if kode and nama and status:
				sys.tambah_barang(kode,nama,status)
				messagebox.showinfo('Success', 'Barang berhasil ditambahkan!')
				self.crud.destroy()
				self.load_inventory_data()
			else:
				messagebox.showerror('Error', 'Semua kolom harus diisi!')

		ttk.Button(frame, text='Tambah', command=submit).pack(pady=10)

	def edit_barang(self):
		self
	def hapus_barang(self):
		self
	
	def Ruangan(self):
		self.clear_window()
		self.root.title ('Ruangan')

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Warna.TFrame', background = 'black',foreground = 'white')
		style.configure('1.TButton',foreground = 'white',background = 'black',padding = 5)

		top_frame = ttk.Frame(self.root, style = 'Warna.TFrame')
		top_frame.pack(fill='x', pady=0,)

		ttk.Label(top_frame,
		          text=f'Ruangan',background='black',foreground='white',font=('times new roman', 30, 'bold')).pack(side="left", padx=10)
	
		ttk.Button(top_frame, text="Back",style= '1.TButton', command=self.open_main_window).pack(side="right", padx=10)

		self.table = ttk.Treeview(self.root, columns=('kode_ruangan','nama_ruangan',),show="headings")
		self.table.heading("kode_ruangan",text="Kode Ruangan")
		self.table.heading("nama_ruangan",text="Nama Ruangan")

		self.table.column("kode_ruangan",width=60)
		self.table.column("nama_ruangan",width=60, anchor="center")

		self.table.pack(fill='both', expand=True, padx=10, pady=10)

		crud_frame = ttk.Frame(self.root,style = 'Warna.TFrame')
		crud_frame.pack(fill='x',side='bottom',pady=5,padx=10)

		ttk.Button(crud_frame, text='Add', style='1.TButton', command=self.tambah_ruang).pack(side='left', padx=5)
		ttk.Button(crud_frame,text='Edit',style='1.TButton',command=self.edit_ruang).pack(side = 'left',padx=5)
		ttk.Button(crud_frame, text='Delete', style='1.TButton', command=self.hapus_ruang).pack(side='left', padx=5)
        
	def tambah_ruang(self):
		self
	def edit_ruang(self):
		self
	def hapus_ruang(self):
		self

	def Kategori(self):
		self.clear_window()
		self.root.title ('Kategori')

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Warna.TFrame', background = 'black',foreground = 'white')
		style.configure('1.TButton',foreground = 'white',background = 'black',padding = 5)

		top_frame = ttk.Frame(self.root, style = 'Warna.TFrame')
		top_frame.pack(fill='x', pady=0,)

		ttk.Label(top_frame,
		          text=f'Kategori',background='black',foreground='white',font=('times new roman', 30, 'bold')).pack(side="left", padx=10)
	
		ttk.Button(top_frame, text="Back",style= '1.TButton', command=self.open_main_window).pack(side="right", padx=10)

		self.table = ttk.Treeview(self.root, columns=('kode_barang','nama_barang','merek_barang'),show="headings")
		self.table.heading("kode_barang",text="Kode")
		self.table.heading("nama_barang",text="Nama")
		self.table.heading("merek_barang",text="Merek")

		self.table.column("kode_barang",width=60)
		self.table.column("nama_barang",width=60, anchor="center")
		self.table.column("merek_barang",width=60, anchor="center")

		self.table.pack(fill='both', expand=True, padx=10, pady=10)

		crud_frame = ttk.Frame(self.root,style = 'Warna.TFrame')
		crud_frame.pack(fill='x',side='bottom',pady=5,padx=10)

		ttk.Button(crud_frame, text='Add', style='1.TButton', command=self.tambah_kategori).pack(side='left', padx=5)
		ttk.Button(crud_frame,text='Edit',style='1.TButton',command=self.edit_kategori).pack(side = 'left',padx=5)
		ttk.Button(crud_frame, text='Delete', style='1.TButton', command=self.hapus_kategori).pack(side='left', padx=5)
        
	def tambah_kategori(self):
		self
	def edit_kategori(self):
		self
	def hapus_kategori(self):
		self

	def logout(self):
		current_session.logout()
		messagebox.showinfo("Info", "Logged out successfully")
		self.login_page()

	def clear_window(self):
		for widget in self.root.winfo_children():
			widget.destroy()

	# 	def load_table_data(self):
	# 	for item in self.table.get_children():
	# 		self.table.delete(row)

	# 	data_barang = sys.tampilkan_barang()
    # 	for row in data_barang:
    #     	self.tree.insert("", "end", values=row)

	# self.table.pack(fill="both", expand=True)
	# 	self.table.bind("<ButtonRelease-1>", self.on_table_click)
	# 	self.load_table_data()

# ---------- RUN APP ----------
if __name__ == "__main__":
	root = Tk()
	app = Main(root)
	root.mainloop()