CREATE TABLE `data_user` (
  `id` int NOT NULL,
  `username` varchar(250) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `data_ruangan` (
  `kode_ruangan` varchar(20) DEFAULT NULL,
  `nama_ruangan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `data_kategori` (
  `kode_barang` varchar(20) NOT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `merek_barang` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `data_inventory` (
  `id_inventory` int NOT NULL AUTO_INCREMENT,
  `kode_barang` varchar(20) DEFAULT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `status_barang` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_inventory`),
  KEY `kode_barang` (`kode_barang`),
  CONSTRAINT `data_inventory_ibfk_1` FOREIGN KEY (`kode_barang`) REFERENCES `data_kategori` (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;