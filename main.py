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

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('aw.TButton',font = ('times new roman',15,))
		style.configure('log.TFrame',background = 'skyblue')

		frame = ttk.Frame(self.root, padding=10,style='log.TFrame')
		frame.pack(fill='both')

		ttk.Label(frame, text="Login",background='skyblue',font=('times new roman',20, 'bold')).pack(pady=5)
		
		self.logoLogin = PhotoImage(file= 'Login.png')
		imageLabel = ttk.Label(image= self.logoLogin)
		imageLabel.pack(pady=45,anchor='center') 

		ttk.Label(self.root, text="Username:",font=('times new roman',20, 'bold')).pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:",font=('times new roman',20, 'bold')).pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Login",style='aw.TButton', command=self.login_process).pack(pady=10)
		ttk.Button(self.root, text="Register",style='aw.TButton', command=self.regis_page).pack(pady=5)

	def regis_page(self) :
		self.clear_window()

		self.root.title("Register Page")
		self.root.geometry("450x270")

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('aw.TButton',font = ('times new roman',15,))
		style.configure('log.TFrame',background = 'skyblue')

		frame = ttk.Frame(self.root, padding=10,style='log.TFrame')
		frame.pack(fill='both')

		ttk.Label(frame, text="Get Your Username Here",background='skyblue',font=('times new roman',20, 'bold')).pack(pady=5)

		self.logoLogin = PhotoImage(file= 'Login.png')
		imageLabel = ttk.Label(image= self.logoLogin)
		imageLabel.pack(pady=45,anchor='center') 
		
		ttk.Label(self.root, text="New Username:",font=('times new roman',20, 'bold')).pack(pady=5)
		self.entry_username = ttk.Entry(self.root)
		self.entry_username.pack()

		ttk.Label(self.root, text="Password:",font=('times new roman',20, 'bold')).pack(pady=5)
		self.entry_password = ttk.Entry(self.root, show="*")
		self.entry_password.pack()

		ttk.Button(self.root, text="Register",style='aw.TButton', command=self.regis_process).pack(pady=10)
		ttk.Button(self.root, text="Back",style='aw.TButton', command=self.login_page).pack(pady=5)

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

		self.table.column("id_barang",width=60, anchor='center')
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

		ttk.Label(frame, text='Id').pack(anchor='w')
		entry_id = ttk.Entry(frame)
		entry_id.pack(fill='x')

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
			id = entry_id.get()
			if id and kode and nama and status:
				sys.tambah_barang(id, kode, nama, status)
				messagebox.showinfo('Success', 'Barang berhasil ditambahkan!')
				self.crud.destroy()
				self.load_inventory_data()
			else:
				messagebox.showerror('Error', 'Semua kolom harus diisi!')

		ttk.Button(frame, text='Tambah', command=submit).pack(pady=10)

	def edit_barang(self):
		selected = self.table.focus()
		if not selected:
			messagebox.showwarning("Warning", "Pilih data yang mau diedit!")
			return

		data = self.table.item(selected)['values']
		id_awal = data[0]
		kode_awal = data[1]
		nama_awal = data[2]
		status_awal = data[3]

		self.crud = Toplevel(self.root)
		self.crud.title("Edit Barang")
		self.crud.geometry("500x350")
		self.crud.resizable(False, False)

		frame = ttk.Frame(self.crud, padding=10)
		frame.pack(fill='both', expand=True)
		
		ttk.Label(frame, text='ID Lama').pack(anchor='w')
		entry_id_lama = ttk.Entry(frame)
		entry_id_lama.insert(0, id_awal)
		entry_id_lama.configure(state='disabled')
		entry_id_lama.pack(fill='x')

		ttk.Label(frame, text='Id').pack(anchor='w')
		entry_id = ttk.Entry(frame)
		entry_id.insert(0, id_awal)
		entry_id.pack(fill='x')

		ttk.Label(frame, text='Kode').pack(anchor='w')
		entry_kode = ttk.Entry(frame)
		entry_kode.insert(0, kode_awal)
		entry_kode.pack(fill='x')

		ttk.Label(frame, text='Nama').pack(anchor='w')
		entry_nama = ttk.Entry(frame)
		entry_nama.insert(0, nama_awal)
		entry_nama.pack(fill='x')

		ttk.Label(frame, text='Status').pack(anchor='w')
		entry_status = ttk.Entry(frame)
		entry_status.insert(0, status_awal)
		entry_status.pack(fill='x')

		def submit():
			id_baru = entry_id.get()
			id_lama = entry_id_lama.get()
			kode = entry_kode.get()
			nama = entry_nama.get()
			status = entry_status.get()

			if not (id_baru and kode and nama and status):
				messagebox.showerror("Error", "Semua kolom harus diisi!")
				return

			sys.update_barang(id_lama, id_baru,  kode, nama, status)
			messagebox.showinfo("Success", "Barang berhasil diedit!")
			self.load_inventory_data()
			self.crud.destroy()

		ttk.Button(frame, text='Save', command=submit).pack(pady=10,anchor= 'w')


	def hapus_barang(self):
		selected = self.table.focus()
		if not selected:
			messagebox.showwarning("Warning", "Pilih data yang mau dihapus!")
			return

		data = self.table.item(selected)['values']
		id_barang = data[0]
	
		if messagebox.askyesno("Confirm", f"Hapus barang ID {id_barang}?"):
			sys.hapus_barang(id_barang)
			self.load_inventory_data()
			messagebox.showinfo("Success", "Barang berhasil dihapus!")

	
	def Ruangan(self):
		self.clear_window()
		self.root.title('Ruangan')

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Warna.TFrame', background='black', foreground='white')
		style.configure('1.TButton', foreground='white', background='black', padding=5)

		top_frame = ttk.Frame(self.root, style='Warna.TFrame')
		top_frame.pack(fill='x', pady=0)

		ttk.Label(top_frame,text='Ruangan',background='black',foreground='white',font=('times new roman', 30, 'bold')).pack(side="left", padx=10)

		ttk.Button(top_frame, text="Ruang 20", style='1.TButton',command=lambda: self.load_ruangan_data("20")).pack(side="right", padx=5)

		ttk.Button(top_frame, text="Ruang 10", style='1.TButton',command=lambda: self.load_ruangan_data("10")).pack(side="right", padx=5)

		ttk.Button(top_frame, text="Back", style='1.TButton',command=self.open_main_window).pack(side="right", padx=10)

		self.table = ttk.Treeview(self.root, columns=('Id_inventory','nama_barang','status_barang'), show="headings")
		self.table.heading("Id_inventory", text="Kode Barang")
		self.table.heading("nama_barang", text="Nama Barang")
		self.table.heading('status_barang',text='Status Barang')

		self.table.column("Id_inventory", width=60, anchor='center')
		self.table.column("nama_barang", width=60, anchor="center")
		self.table.column('status_barang',width=60, anchor='center')

		self.table.pack(fill='both', expand=True, padx=10, pady=10)
		
		self.load_ruangan_data(prefix=None)

	def load_ruangan_data(self, prefix=None):
		rows = sys.tampilkan_ruang_prefix(prefix)

    # Clear table
		for item in self.table.get_children():
			self.table.delete(item)

    # Insert table
		for row in rows:
			self.table.insert("", "end", values=row)

	def kode_ruang(self):
		self

	def Kategori(self):
		self.clear_window()
		self.root.title('Kategori')

		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Warna.TFrame', background='black', foreground='white')
		style.configure('1.TButton', foreground='white', background='black', padding=5)

		top_frame = ttk.Frame(self.root, style='Warna.TFrame')
		top_frame.pack(fill='x', pady=0)

		ttk.Label(top_frame,text='Kategori',background='black',foreground='white',font=('times new roman', 30, 'bold')).pack(side="left", padx=10)

		ttk.Button(top_frame, text="Elektronik", style='1.TButton',command=lambda: self.load_kategori_data("EL")).pack(side="right", padx=5)

		ttk.Button(top_frame, text="Furniture", style='1.TButton',command=lambda: self.load_kategori_data("FU")).pack(side="right", padx=5)

		ttk.Button(top_frame, text="Back", style='1.TButton',command=self.open_main_window).pack(side="right", padx=10)

		self.table = ttk.Treeview(self.root, columns=('kode_barang','nama_barang','status_barang'), show="headings")
		self.table.heading("kode_barang", text="Kode Barang")
		self.table.heading("nama_barang", text="Nama Barang")
		self.table.heading('status_barang',text='Status Barang')

		self.table.column("kode_barang", width=60, anchor='center')
		self.table.column("nama_barang", width=60, anchor="center")
		self.table.column('status_barang',width=60, anchor='center')

		self.table.pack(fill='both', expand=True, padx=10, pady=10)
		
		self.load_kategori_data(prefix=None)


	def load_kategori_data(self, prefix=None):
		rows = sys.tampilkan_kategori_prefix(prefix)

    # Clear table
		for item in self.table.get_children():
			self.table.delete(item)

    # Insert table
		for row in rows:
			self.table.insert("", "end", values=row)

	
	def logout(self):
		current_session.logout()
		messagebox.showinfo("Info", "Logged out successfully")
		self.login_page()

	def clear_window(self):
		for widget in self.root.winfo_children():
			widget.destroy()

	# def load_table_data(self):
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