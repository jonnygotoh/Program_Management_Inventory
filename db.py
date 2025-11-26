import mysql.connector as mysql_conn

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
    
    def delete (self,sql,val):
        self.cur.execute(sql,val)
        self.dbgw.commit()
        return self.cur.rowcount
    
    def fetch (self,sql,val):
        self.cur.execute(sql,val)
        hasil = self.cur.fetchall()
        return hasil