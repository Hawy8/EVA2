
from getpass import getpass
from Aplicacion.trabajador import Trabajador
from Aplicacion.producto import Producto
from Conexion.conexion import ConexionMySQL
from Crud.trabajador_dao import TrabajadorDAO
from Crud.producto_dao import ProductoDAO

def menu():
        con = ConexionMySQL()
        con.conectar()
        tdao = TrabajadorDAO(con)
        pdao = ProductoDAO(con)

        while True:
            print("""\n=== MENÚ AV ===
1) Ingresar trabajador
2) Listar trabajadores
3) Buscar trabajador por RUT
4) Actualizar trabajador
5) Eliminar trabajador
---
6) Ingresar producto
7) Listar productos
8) Buscar producto por nombre
9) Actualizar producto
10) Eliminar producto
0) Salir
""")
            try:
                op = int(input("Opción: ").strip())
            except ValueError:
                print("Ingrese un número válido")
                continue

            try:
                if op == 1:
                    rut = input("RUT: ").strip()
                    nombre = input("Nombre: ").strip()
                    apellido = input("Apellido: ").strip()
                    direccion = input("Dirección: ").strip()
                    email = input("Email: ").strip()
                    password = getpass("Password (oculta): ")
                    t = Trabajador(rut, nombre, apellido, direccion, email, password)
                    tdao.crear(t)
                    print("Trabajador creado correctamente.")
                elif op == 2:
                    for t in tdao.listar():
                        print(t)
                elif op == 3:
                    rut = input("RUT a buscar: ").strip()
                    res = tdao.buscar_por_rut(rut)
                    print(res if res else "No encontrado")
                elif op == 4:
                    rut = input("RUT a actualizar: ").strip()
                    nombre = input("Nuevo nombre: ").strip()
                    apellido = input("Nuevo apellido: ").strip()
                    direccion = input("Nueva dirección: ").strip()
                    email = input("Nuevo email: ").strip()
                    filas = tdao.actualizar(rut, nombre, apellido, direccion, email)
                    print(f"Filas afectadas: {filas}")
                elif op == 5:
                    rut = input("RUT a eliminar: ").strip()
                    filas = tdao.eliminar(rut)
                    print(f"Filas afectadas: {filas}")
                elif op == 6:
                    nombre = input("Nombre: ").strip()
                    descripcion = input("Descripción: ").strip()
                    precio = float(input("Precio: ").strip())
                    stock = int(input("Stock: ").strip())
                    p = Producto(nombre, descripcion, precio, stock)
                    pdao.crear(p)
                    print("Producto creado correctamente.")
                elif op == 7:
                    for p in pdao.listar():
                        print(p)
                elif op == 8:
                    nombre = input("Nombre a buscar: ").strip()
                    res = pdao.buscar_por_nombre(nombre)
                    print(res if res else "No hay coincidencias")
                elif op == 9:
                    id_ = int(input("ID producto a actualizar: ").strip())
                    nombre = input("Nuevo nombre: ").strip()
                    descripcion = input("Nueva descripción: ").strip()
                    precio = float(input("Nuevo precio: ").strip())
                    stock = int(input("Nuevo stock: ").strip())
                    filas = pdao.actualizar(id_, nombre, descripcion, precio, stock)
                    print(f"Filas afectadas: {filas}")
                elif op == 10:
                    id_ = int(input("ID producto a eliminar: ").strip())
                    filas = pdao.eliminar(id_)
                    print(f"Filas afectadas: {filas}")
                elif op == 0:
                    print("¡Hasta luego!")
                    con.cerrar()
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")
                if __name__ == "__main__":
                    menu()
