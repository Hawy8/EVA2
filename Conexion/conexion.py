
import mysql.connector
from mysql.connector import Error
import configparser
import os

class ConexionMySQL:
    def __init__(self, config_path: str = None):
        self._conn = None
        self._cursor = None
        self._config_path = config_path or os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.ini")

    def conectar(self):
        config = configparser.ConfigParser()
        if not os.path.exists(self._config_path):
            raise FileNotFoundError(f"No se encontró el archivo de configuración: {self._config_path}")
        config.read(self._config_path, encoding="utf-8")
        try:
            self._conn = mysql.connector.connect(
                host=config.get("mysql", "host"),
                port=config.getint("mysql", "port"),
                user=config.get("mysql", "user"),
                password=config.get("mysql", "password"),
                database=config.get("mysql", "database"),
                auth_plugin='mysql_native_password'
            )
            self._cursor = self._conn.cursor(dictionary=True)
        except Error as e:
            raise RuntimeError(f"Error al conectar a MySQL: {e}")

    @property
    def cursor(self):
        if self._cursor is None:
            raise RuntimeError("No existe conexión activa")
        return self._cursor

    def commit(self):
        if self._conn:
            self._conn.commit()

    def cerrar(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
        self._cursor = None
        self._conn = None

    def ejecutar(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        return self.cursor
