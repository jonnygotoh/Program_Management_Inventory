from db_conn.db import data

db = data
# Membuat CRUD (Create, Read, Update, Delete dan juga fetch/menampilkan barang)

def tambah_barang(id, kode, nama, status):
    sql = "INSERT INTO data_inventory (id_inventory, kode_barang, nama_barang, status_barang) VALUES (%s, %s, %s,%s)"
    val = (id,kode, nama, status)
    return db.execute(sql, val)

def update_barang(id_lama, id_baru, kode, nama, status):
    sql = "UPDATE data_inventory SET id_inventory=%s, kode_barang=%s, nama_barang=%s, status_barang=%s WHERE id_inventory=%s"
    val = (id_baru, kode, nama, status, id_lama)
    return db.execute(sql, val)

def hapus_barang(id_barang):
    sql = "DELETE FROM data_inventory WHERE id_inventory=%s"
    val = (id_barang,)
    return db.execute(sql, val)

def tampilkan_barang():
    sql = "SELECT * FROM data_inventory"
    return db.fetch(sql,())

def tampilkan_kategori_prefix(prefix=None):
    # Query untuk mengambil data barang berdasarkan prefix kode_barang
    if prefix:
        sql = "SELECT kode_barang, nama_barang, status_barang FROM data_inventory WHERE kode_barang LIKE %s"
        val = (prefix + "%",)  # Menambahkan wildcard (%) untuk pencarian
    else:
        sql = "SELECT kode_barang, nama_barang, status_barang FROM data_inventory"
        val = ()

    # Eksekusi query untuk mengambil data barang
    return db.fetch(sql, val)

def tampilkan_ruang_prefix(prefix=None):
    # Query untuk mengambil data barang berdasarkan prefix kode_barang
    
    if prefix:
        sql = 'SELECT id_inventory, nama_barang, status_barang FROM data_inventory WHERE CAST(id_inventory AS CHAR) LIKE %s'
        val = (prefix + '%',)  # Menambahkan wildcard (%) untuk pencarian
    else:
        sql = "SELECT id_inventory, nama_barang, status_barang FROM data_inventory"
        val = ()

    # Eksekusi query untuk mengambil data barang
    return db.fetch(sql, val)

class Login:
    def __init__(self):
        self.db = db
        self.user_name = None   

    def login_user(self, username, password):
        sql = "SELECT username FROM data_user WHERE username=%s AND password=%s"
        val = (username, password)
        result = self.db.fetch(sql, val)

        if result:  
            self.user_name = result[0][0]  
            return True
        
        return False

    def regis_user(self, username, password):
        sql = "INSERT INTO data_user (username, password) VALUES (%s, %s)"
        val = (username, password)
        result = self.db.execute(sql, val)

        if result:
            self.user_name = username
            return True
        
        return False

    def logout(self):
        self.user_name = None