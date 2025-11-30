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