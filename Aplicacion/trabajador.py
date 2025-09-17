
from .persona import Persona
import hashlib

class Trabajador(Persona):
    def __init__(self, rut: str, nombre: str, apellido: str, direccion: str, email: str, password_plano: str):
        super().__init__(rut, nombre, apellido, direccion)
        self._email = email
        self._password_md5 = self._hash_md5(password_plano)

    @staticmethod
    def _hash_md5(password_plano: str) -> str:
        if not isinstance(password_plano, str) or password_plano == "":
            raise ValueError("La contraseña no puede estar vacía")
        return hashlib.md5(password_plano.encode('utf-8')).hexdigest()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if "@" not in value:
            raise ValueError("Email inválido")
        self._email = value

    @property
    def password_md5(self) -> str:
        return self._password_md5

    def mostrar_info(self) -> str:
        return f"Trabajador {self.nombre} {self.apellido} (RUT: {self.rut}) - Email: {self.email}"
