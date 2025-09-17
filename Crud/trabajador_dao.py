
from typing import List, Optional, Dict, Any
from Aplicacion.trabajador import Trabajador
from Conexion.conexion import ConexionMySQL

class TrabajadorDAO:
    def __init__(self, conexion: ConexionMySQL):
        self.con = conexion

    def crear(self, t: Trabajador) -> int:
        sql = ("INSERT INTO trabajadores (rut, nombre, apellido, direccion, email, password_md5) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
        cur = self.con.ejecutar(sql, (t.rut, t.nombre, t.apellido, t.direccion, t.email, t.password_md5))
        self.con.commit()
        return cur.lastrowid

    def listar(self) -> List[Dict[str, Any]]:
        cur = self.con.ejecutar("SELECT * FROM trabajadores ORDER BY creado_en DESC")
        return cur.fetchall()

    def buscar_por_rut(self, rut: str) -> Optional[Dict[str, Any]]:
        cur = self.con.ejecutar("SELECT * FROM trabajadores WHERE rut=%s", (rut,))
        return cur.fetchone()

    def actualizar(self, rut: str, nombre: str, apellido: str, direccion: str, email: str) -> int:
        cur = self.con.ejecutar(
            "UPDATE trabajadores SET nombre=%s, apellido=%s, direccion=%s, email=%s WHERE rut=%s",
            (nombre, apellido, direccion, email, rut),
        )
        self.con.commit()
        return cur.rowcount

    def eliminar(self, rut: str) -> int:
        cur = self.con.ejecutar("DELETE FROM trabajadores WHERE rut=%s", (rut,))
        self.con.commit()
        return cur.rowcount
