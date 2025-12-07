import mysql.connector as mysql_conn
import os

class database:
    def __init__(self):
        self.dbgw = mysql_conn.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'db_go'
        )
        self.cur = self.dbgw.cursor()

    def execute (self,sql,val):
        self.cur.execute(sql,val)
        self.dbgw.commit()
        return self.cur.rowcount
    
    def fetch (self,sql,val):
        self.cur.execute(sql,val)
        hasil = self.cur.fetchall()
        return hasil
    
    def menhubungkan_sql(self, filename='schema.sql'):
        # agar python tw dimana file scheme.sql berada
        # juga untuk buat path yang sama untuk file db sama schema
        filepath = os.path.join(os.path.dirname(__file__), filename)

        # baca seluruh isi file SQL
        with open(filepath, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # pisahkan setiap statement berdasarkan titik koma
        statements = sql_script.split(';')
        for stmt in statements:
            stmt = stmt.strip()
            # if stmt itu untuk menghindari baris kosong
            if stmt:  
                self.cur.execute(stmt)
        self.dbgw.commit()

data = database()