
from typing import List, Optional, Dict, Any
from Aplicacion.producto import Producto
from Conexion.conexion import ConexionMySQL

class ProductoDAO:
    def __init__(self, conexion: ConexionMySQL):
        self.con = conexion

    def crear(self, p: Producto) -> int:
        sql = ("INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)")
        cur = self.con.ejecutar(sql, (p.nombre, p.descripcion, p.precio, p.stock))
        self.con.commit()
        return cur.lastrowid

    def listar(self) -> List[Dict[str, Any]]:
        cur = self.con.ejecutar("SELECT * FROM productos ORDER BY creado_en DESC")
        return cur.fetchall()

    def buscar_por_nombre(self, nombre: str) -> List[Dict[str, Any]]:
        cur = self.con.ejecutar("SELECT * FROM productos WHERE nombre LIKE %s", (f"%{nombre}%",))
        return cur.fetchall()

    def actualizar(self, id_: int, nombre: str, descripcion: str, precio: float, stock: int) -> int:
        cur = self.con.ejecutar(
            "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE id=%s",
            (nombre, descripcion, precio, stock, id_),
        )
        self.con.commit()
        return cur.rowcount

    def eliminar(self, id_: int) -> int:
        cur = self.con.ejecutar("DELETE FROM productos WHERE id=%s", (id_,))
        self.con.commit()
        return cur.rowcount
