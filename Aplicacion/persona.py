
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, rut: str, nombre: str, apellido: str, direccion: str = ""):
        self._rut = rut
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion

    # Encapsulamiento con properties
    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, value: str) -> None:
        if not value:
            raise ValueError("El RUT no puede estar vacío")
        self._rut = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if len(value.strip()) < 2:
            raise ValueError("El nombre es muy corto")
        self._nombre = value

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str) -> None:
        if len(value.strip()) < 2:
            raise ValueError("El apellido es muy corto")
        self._apellido = value

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, value: str) -> None:
        self._direccion = value

    @abstractmethod
    def mostrar_info(self) -> str:
        ...
