# ===============================
# Funciones de validación
# ===============================

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Debe ingresar un número entero válido")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Debe ingresar un número decimal válido")

def pedir_opcion(mensaje, opciones):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones:
                return opcion
            else:
                print("Opción no válida")
        except ValueError:
            print(" Debe ingresar un número")


class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, id, nombre, edad, curso, promedio):
        super().__init__(id, nombre, edad)
        self.curso = curso
        self.promedio = promedio

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Curso: {self.curso}")
        print(f"Promedio: {self.promedio}")


class Trabajador(Persona):
    def __init__(self, id, nombre, edad, cargo, salario):
        super().__init__(id, nombre, edad)
        self.cargo = cargo
        self.salario = salario

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")


# ===============================
# Sistema
# ===============================

class SistemaColegio:
    def __init__(self):
        self.estudiantes = []
        self.trabajadores = []

    # ---------- ESTUDIANTES ----------
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
        else:
            for estudiante in self.estudiantes:
                estudiante.mostrar_datos()
                print("-" * 30)

    def actualizar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                estudiante.nombre = input("Nuevo nombre: ")
                estudiante.edad = pedir_int("Nueva edad: ")
                estudiante.curso = input("Nuevo curso: ")
                estudiante.promedio = pedir_float("Nuevo promedio: ")
                print("Estudiante actualizado")
                return
        print("ID no encontrada")

    def eliminar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                self.estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        print("ID no encontrada")

    # ---------- TRABAJADORES ----------
    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def mostrar_trabajadores(self):
        if not self.trabajadores:
            print("No hay trabajadores registrados")
        else:
            for trabajador in self.trabajadores:
                trabajador.mostrar_datos()
                print("-" * 30)

    def actualizar_trabajador(self, id):
        for trabajador in self.trabajadores:
            if trabajador.id == id:
                trabajador.nombre = input("Nuevo nombre: ")
                trabajador.edad = pedir_int("Nueva edad: ")
                trabajador.cargo = input("Nuevo cargo: ")
                trabajador.salario = pedir_float("Nuevo salario: ")
                print("Trabajador actualizado")
                return
        print("ID no encontrada")

    def eliminar_trabajador(self, id):
        for trabajador in self.trabajadores:
            if trabajador.id == id:
                self.trabajadores.remove(trabajador)
                print("Trabajador eliminado")
                return
        print("ID no encontrada")


# ===============================
# Menús
# ===============================

sistema = SistemaColegio()

def menu_principal():
    while True:
        print("""
Por favor digite el tipo de usuario
1. Estudiante
2. Trabajador
3. Salir
""")
        opcion = pedir_opcion("Opción: ", [1, 2, 3])

        if opcion == 1:
            menu_estudiante()
        elif opcion == 2:
            menu_trabajador()
        elif opcion == 3:
            print("Saliendo del sistema...")
            break


def menu_estudiante():
    while True:
        print("""
Bienvenido al registro estudiantil
1. Agregar estudiante
2. Mostrar estudiantes
3. Actualizar estudiante
4. Eliminar estudiante
5. Volver al menú principal
""")
        opcion = pedir_opcion("Opción: ", [1, 2, 3, 4, 5])

        if opcion == 1:
            id = pedir_int("Id: ")
            nombre = input("Nombre: ")
            edad = pedir_int("Edad: ")
            curso = input("Curso: ")
            promedio = pedir_float("Promedio: ")
            sistema.agregar_estudiante(
                Estudiante(id, nombre, edad, curso, promedio)
            )

        elif opcion == 2:
            sistema.mostrar_estudiantes()

        elif opcion == 3:
            sistema.actualizar_estudiante(pedir_int("Id a actualizar: "))

        elif opcion == 4:
            sistema.eliminar_estudiante(pedir_int("Id a eliminar: "))

        elif opcion == 5:
            break


def menu_trabajador():
    while True:
        print("""
Bienvenido al registro de empleados
1. Agregar trabajador
2. Mostrar trabajadores
3. Actualizar trabajador
4. Eliminar trabajador
5. Volver al menú principal
""")
        opcion = pedir_opcion("Opción: ", [1, 2, 3, 4, 5])

        if opcion == 1:
            id = pedir_int("Id: ")
            nombre = input("Nombre: ")
            edad = pedir_int("Edad: ")
            cargo = input("Cargo: ")
            salario = pedir_float("Salario: ")
            sistema.agregar_trabajador(
                Trabajador(id, nombre, edad, cargo, salario)
            )

        elif opcion == 2:
            sistema.mostrar_trabajadores()

        elif opcion == 3:
            sistema.actualizar_trabajador(pedir_int("Id a actualizar: "))

        elif opcion == 4:
            sistema.eliminar_trabajador(pedir_int("Id a eliminar: "))

        elif opcion == 5:
            break


menu_principal()




    
    
    
