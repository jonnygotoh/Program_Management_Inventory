Database: inventory_kampus

CREATE TABLE data_user (
    username VARCHAR(50) PRIMARY KEY,
    nama VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE data_ruangan (
    kode_ruangan VARCHAR(20) PRIMARY KEY,
    nama_ruangan VARCHAR(100)
);

CREATE TABLE data_kategori (
    kode_barang VARCHAR(20) PRIMARY KEY,
    nama_barang VARCHAR(100),
    merek_barang VARCHAR(100)
);

CREATE TABLE data_inventori (
    id_inventori INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(20),
    nama_barang VARCHAR(100),
    nama_ruangan VARCHAR(100),
    status_barang VARCHAR(100),
    FOREIGN KEY (kode_barang) REFERENCES data_kategori(kode_barang)
);