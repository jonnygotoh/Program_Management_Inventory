class data_user:
    def __init__(self, nama, password,):
        self.nama = nama
        self.password = password

    def info(self):
        return f'{self.nama},{self.password}'