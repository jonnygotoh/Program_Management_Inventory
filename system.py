from db_conn.db import data

db = data
# Membuat CRUD (Create, Read, Update, Delete dan juga fetch/menampilkan barang)

def tambah_barang(kode, nama, status):
    sql = "INSERT INTO data_inventory (kode_barang, nama_barang, status_barang) VALUES (%s, %s, %s)"
    val = (kode, nama, status)
    return db.execute(sql, val)

def update_barang(id, nama, stok):
    sql = "UPDATE data_inventory SET nama_barang=%s, status_barang=%s WHERE id_inventory=%s"
    val = (nama, stok, id)
    return db.execute(sql, val)

def hapus_barang(id):
    sql = "DELETE FROM data_inventory WHERE id_inventory=%s"
    val = (id,)
    return db.execute(sql, val)

def tampilkan_barang():
    sql = "SELECT * FROM data_inventory"
    return db.fetch(sql)

class Login:
    def __init__(self):
        self.db = db()
        self.user_name = None   

    def login_user(self, username, password):
        sql = "SELECT username FROM data_user WHERE username=%s AND pw=%s"
        val = (username, password)
        result = self.db.fetch(sql, val)

        if result:  
            self.user_name = result[0][0]  
            return True
        
        return False

    def logout(self):
        self.user_name = None

#  # Main Frame
#         self.main_frame = ttk.Frame(self.root)
#         self.main_frame.pack(fill="both", expand=True, pady=10)

#         # Tombol masuk Gudang
#         ttk.Label(self.main_frame, text=f"Selamat datang, {current_session.user_name}!", font=("times new roman", 14)).pack(pady=10)
#         ttk.Button(self.main_frame, text="Gudang", style='Dark.TButton', command=self.show_gudang_page).pack(pady=10)

#  def show_gudang_page(self):
#         self.clear_window()
#         self.root.title("Gudang")
#         self.root.geometry("700x400")

#         style = ttk.Style()
#         style.configure('Dark.TButton', foreground='white', background='black', padding=5)

#         top_frame = ttk.Frame(self.root)
#         top_frame.pack(fill="x")
#         ttk.Label(top_frame, text="Gudang", font=("times new roman", 20, "bold")).pack(side="left", padx=10)
#         ttk.Button(top_frame, text="Kembali", style='Dark.TButton', command=self.open_main_window).pack(side="right", padx=10)

#         # Treeview untuk menampilkan data
#         self.tree = ttk.Treeview(self.root, columns=("ID", "Kode", "Nama", "Status"), show="headings")
#         self.tree.heading("ID", text="ID")
#         self.tree.heading("Kode", text="Kode")
#         self.tree.heading("Nama", text="Nama Barang")
#         self.tree.heading("Status", text="Status")
#         self.tree.pack(fill="both", expand=True, padx=20, pady=20)

#         # Tombol CRUD
#         crud_frame = ttk.Frame(self.root)
#         crud_frame.pack(pady=5)
#         ttk.Button(crud_frame, text="Tambah Barang", style='Dark.TButton', command=self.tambah_barang).pack(side="left", padx=5)
#         ttk.Button(crud_frame, text="Edit Barang", style='Dark.TButton', command=self.edit_barang).pack(side="left", padx=5)
#         ttk.Button(crud_frame, text="Hapus Barang", style='Dark.TButton', command=self.hapus_barang).pack(side="left", padx=5)

#         self.load_data_barang()

#     # ---------- Fungsi CRUD ----------
#     def load_data_barang(self):
#         # Clear tree
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         # Ambil data dari system.py
#         data_barang = sys.tampilkan_barang()
#         for row in data_barang:
#             self.tree.insert("", "end", values=row)

#     def tambah_barang(self):
#         kode = simpledialog.askstring("Input", "Kode Barang:")
#         nama = simpledialog.askstring("Input", "Nama Barang:")
#         status = simpledialog.askstring("Input", "Status Barang:")
#         if kode and nama and status:
#             sys.tambah_barang(kode, nama, status)
#             self.load_data_barang()

#     def edit_barang(self):
#         selected = self.tree.focus()
#         if not selected:
#             messagebox.showwarning("Pilih Barang", "Pilih barang untuk diedit")
#             return
#         values = self.tree.item(selected, "values")
#         id_barang = values[0]
#         nama_baru = simpledialog.askstring("Edit Nama", "Nama Barang:", initialvalue=values[2])
#         status_baru = simpledialog.askstring("Edit Status", "Status Barang:", initialvalue=values[3])
#         if nama_baru and status_baru:
#             sys.update_barang(id_barang, nama_baru, status_baru)
#             self.load_data_barang()

#     def hapus_barang(self):
#         selected = self.tree.focus()
#         if not selected:
#             messagebox.showwarning("Pilih Barang", "Pilih barang untuk dihapus")
#             return
#         values = self.tree.item(selected, "values")
#         id_barang = values[0]
#         if messagebox.askyesno("Konfirmasi", f"Hapus barang {values[2]}?"):
#             sys.hapus_barang(id_barang)
#             self.load_data_barang()
# def popup_form(self, title, values=None):
#         popup = tk.Toplevel(self.root)
#         popup.title(title)
#         popup.geometry("300x200")
#         popup.resizable(False, False)

#         ttk.Label(popup, text="Kode Barang:").pack(pady=5)
#         kode_entry = ttk.Entry(popup)
#         kode_entry.pack(pady=5)
#         ttk.Label(popup, text="Nama Barang:").pack(pady=5)
#         nama_entry = ttk.Entry(popup)
#         nama_entry.pack(pady=5)
#         ttk.Label(popup, text="Status Barang:").pack(pady=5)
#         status_entry = ttk.Entry(popup)
#         status_entry.pack(pady=5)

#         # Jika edit, isi default value
#         if values:
#             kode_entry.insert(0, values[1])
#             kode_entry.config(state="disabled")
#             nama_entry.insert(0, values[2])
#             status_entry.insert(0, values[3])

#         def submit():
#             kode = kode_entry.get()
#             nama = nama_entry.get()
#             status = status_entry.get()
#             if not (kode and nama and status):
#                 messagebox.showwarning("Input Kosong", "Semua field harus diisi!")
#                 return
#             if values:  # edit
#                 sys.update_barang(values[0], nama, status)
#             else:       # tambah
#                 sys.tambah_barang(kode, nama, status)
#             self.load_data_barang()
#             popup.destroy()

#         ttk.Button(popup, text="Submit", style='Dark.TButton', command=submit).pack(pady=10)

#     def logout(self):
#         current_session.logout()
#         self.login_page()










#  def show_gudang_page(self):
#         # Bersihkan main frame
#         for widget in self.main_frame.winfo_children():
#             widget.destroy()

#         ttk.Label(self.main_frame, text="Halaman Gudang", font=("times new roman", 16, 'bold')).pack(pady=10)

#         # Ambil data barang dari system.py
#         data_barang = sys.tampilkan_barang()

#         # Tampilkan data dengan loop
#         for item in data_barang:
#             ttk.Label(self.main_frame, text=f"{item[1]} - {item[2]} - {item[3]}").pack(anchor="w", padx=20)

#         # Tombol kembali ke dashboard
#         ttk.Button(self.main_frame, text="Kembali ke Dashboard", style='Dark.TButton', command=self.open_main_window).pack(pady=10)

#     def logout(self):
#         current_session.logout()
#         self.login_page()
