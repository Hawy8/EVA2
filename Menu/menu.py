import os
from getpass import getpass
from Aplicacion.trabajador import Trabajador
from Aplicacion.producto import Producto
from Conexion.conexion import ConexionMySQL
from Crud.trabajador_dao import TrabajadorDAO
from Crud.producto_dao import ProductoDAO

# === utilitarios ===
def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def _pausa():
    input("\nPresiona Enter para continuar...")

CATEGORIAS = [
    "Alimentación", "Bebidas", "Limpieza", "Higiene", "Mascotas", "Panadería"
]

def _elige_categoria():
    print("\nCategorías:")
    for i, c in enumerate(CATEGORIAS, 1):
        print(f"{i}) {c}")
    op = input("Elige categoría (número) o escribe una nueva: ").strip()
    if op.isdigit() and 1 <= int(op) <= len(CATEGORIAS):
        return CATEGORIAS[int(op)-1]
    return op if op else "Alimentación"

def menu():
    con = ConexionMySQL()
    con.conectar()
    tdao = TrabajadorDAO(con)
    pdao = ProductoDAO(con)

    while True:
        _clear()
        print("""
                    ╔═════════════════════════════════════╗
                    ║           MENÚ Mercadona            ║
                    ╠═════════════════════════════════════╣
                    ║  1) Ingresar trabajador             ║
                    ║  2) Listar trabajadores             ║
                    ║  3) Buscar trabajador por RUT       ║
                    ║  4) Actualizar trabajador           ║
                    ║  5) Eliminar trabajador             ║
                    ╟─────────────────────────────────────╢
                    ║  6) Ingresar producto               ║
                    ║  7) Listar productos                ║
                    ║  8) Listar productos por categoría  ║
                    ║  9) Buscar producto por nombre      ║
                    ║ 10) Actualizar producto             ║
                    ║ 11) Eliminar producto               ║
                    ╟─────────────────────────────────────╢
                    ║  0) Salir                           ║
                    ╚═════════════════════════════════════╝
                    """)
        op_str = input("Opción: ").strip()
        if not op_str.isdigit():
            print("Ingrese un número válido (0-11)"); _pausa(); continue
        op = int(op_str)

        try:
            # ===== TRABAJADORES =====
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
                _pausa()

            elif op == 2:
                datos = tdao.listar()
                if not datos:
                    print("No hay trabajadores.")
                else:
                    print("\nRUT          NOMBRE       APELLIDO       EMAIL")
                    print("-"*65)
                    for t in datos:
                        print(f"{t['rut']:<12} {t['nombre']:<12} {t['apellido']:<14} {t.get('email','')}")
                _pausa()

            elif op == 3:
                rut = input("RUT a buscar: ").strip()
                res = tdao.buscar_por_rut(rut)
                print(res if res else "RUT no encontrado")
                _pausa()

            elif op == 4:
                rut = input("RUT a actualizar: ").strip()
                nombre = input("Nuevo nombre: ").strip()
                apellido = input("Nuevo apellido: ").strip()
                direccion = input("Nueva dirección: ").strip()
                email = input("Nuevo email: ").strip()
                filas = tdao.actualizar(rut, nombre, apellido, direccion, email)
                print(f"Filas afectadas: {filas}")
                _pausa()

            elif op == 5:
                rut = input("RUT a eliminar: ").strip()
                filas = tdao.eliminar(rut)
                print(f"Filas de trabajador afectadas: {filas}")
                _pausa()

            # ===== PRODUCTOS =====
            elif op == 6:
                nombre = input("Nombre: ").strip()
                descripcion = input("Descripción: ").strip()
                precio = float(input("Precio: ").strip())
                p = Producto(nombre, descripcion, precio)
                pdao.crear(p)
                print("Producto creado correctamente.")
                _pausa()


            elif op == 7:
                datos = pdao.listar()
                if not datos:
                    print("No hay productos.")
                else:
                    print("\nID  NOMBRE                 PRECIO    CREADO_EN           DESCRIPCIÓN")
                    print("-"*95)
                    for pr in datos:
                        # pr es dict porque usamos dictionary=True
                        desc = (pr['descripcion'] or "")[:30]  # recorta para que quepa
                        print(f"{pr['id']:>3} {pr['nombre']:<22} {pr['precio']:>8.2f}  {str(pr['creado_en'])[:19]:<19}  {desc}")
                _pausa()


            elif op == 8:
                cat = _elige_categoria()
                # usa método del DAO si existe; si no, filtra en memoria
                if hasattr(pdao, "listar_por_categoria"):
                    res = pdao.listar_por_categoria(cat)
                else:
                    res = [pr for pr in pdao.listar() if pr.get('categoria') == cat]
                if not res:
                    print("No hay productos en esa categoría.")
                else:
                    print(f"\n== {cat} ==")
                    for pr in res:
                        print(f"{pr['id']:>3} {pr['nombre']:<22} {pr.get('marca','-'):<12}  ${pr['precio']:>8.2f}")
                _pausa()

            elif op == 9:
                id_ = int(input("ID producto a actualizar: ").strip())
                nombre = input("Nuevo nombre: ").strip()
                descripcion = input("Nueva descripción: ").strip()
                precio = float(input("Nuevo precio: ").strip())
                filas = pdao.actualizar(id_, nombre, descripcion, precio)
                print(f"Filas afectadas: {filas}")
                _pausa()



            elif op == 10:
                id_ = int(input("ID producto a actualizar: ").strip())
                nombre = input("Nuevo nombre: ").strip()
                descripcion = input("Nueva descripción: ").strip()
                categoria = _elige_categoria()
                marca = input("Nueva marca: ").strip() or "Hacendado"
                precio = float(input("Nuevo precio: ").strip())
                stock = int(input("Nuevo stock: ").strip())
                activo = input("¿Activo? (s/n) [s]: ").strip().lower() != "n"
                # espera que el DAO soporte estos campos:
                filas = pdao.actualizar(id_, nombre, descripcion, categoria, marca, precio, stock, activo)
                print(f"Filas afectadas: {filas}")
                _pausa()

            elif op == 11:
                id_ = int(input("ID producto a eliminar: ").strip())
                filas = pdao.eliminar(id_)
                print(f"Filas afectadas: {filas}")
                _pausa()

            elif op == 0:
                print("¡Hasta luego!")
                con.cerrar()
                break

            else:
                print("Opción no válida.")
                _pausa()

        except Exception as e:
            print(f"Error: {e}")
            _pausa()

if __name__ == "__main__":
    menu()
