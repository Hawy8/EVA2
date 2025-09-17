
class Producto:
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int = 0):
        self._nombre = nombre
        self._descripcion = descripcion
        self.precio = precio
        self.stock = stock

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if len(value.strip()) < 2:
            raise ValueError("Nombre de producto inválido")
        self._nombre = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str) -> None:
        self._descripcion = value

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = float(value)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        if value < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = int(value)

    def mostrar_info(self) -> str:
        return f"Producto: {self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"
