class Persona:
    """Clase base que representa a una persona."""
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Contacto(Persona):
    """Clase que hereda de Persona y agrega teléfono y dirección."""
    def __init__(self, nombre, apellido, telefono, direccion):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{super().__str__()} | Teléfono: {self.telefono} | Dirección: {self.direccion}"


class Agenda:
    """Clase que gestiona una agenda de contactos."""
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        """Agrega un nuevo contacto a la agenda."""
        self.contactos.append(contacto)
        print(f"Contacto agregado: {contacto}")

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por su nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto eliminado: {contacto}")
                return
        print(f"No se encontró un contacto con el nombre: {nombre}")

    def modificar_contacto(self, nombre, nuevo_contacto):
        """Modifica un contacto existente."""
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre.lower() == nombre.lower():
                self.contactos[i] = nuevo_contacto
                print(f"Contacto modificado: {nuevo_contacto}")
                return
        print(f"No se encontró un contacto con el nombre: {nombre}")

    def buscar_contacto(self, nombre):
        """Busca un contacto por su nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        print(f"No se encontró un contacto con el nombre: {nombre}")
        return None

    def listar_contactos(self):
        """Lista todos los contactos en formato estándar."""
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def listar_contactos_html(self, archivo="agenda_contactos.html"):
        """Genera un archivo HTML con el listado de contactos."""
        html = "<html><body><h1>Agenda de Contactos</h1><ul>"
        for contacto in self.contactos:
            html += f"<li>{contacto}</li>"
        html += "</ul></body></html>"

        # Guardar en un archivo
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Listado HTML guardado en: {archivo}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear la agenda
    agenda = Agenda()

    # Crear contactos
    contacto1 = Contacto("Juan", "Pérez", "123456789", "Calle Falsa 123")
    contacto2 = Contacto("María", "López", "987654321", "Avenida Siempre Viva 456")

    # Agregar contactos
    agenda.agregar_contacto(contacto1)
    agenda.agregar_contacto(contacto2)

    # Listar contactos
    print("\nListado estándar:")
    agenda.listar_contactos()

    # Modificar un contacto
    contacto_modificado = Contacto("Juan", "Pérez", "111222333", "Calle Nueva 789")
    agenda.modificar_contacto("Juan", contacto_modificado)

    # Buscar un contacto
    print("\nBuscar contacto:")
    encontrado = agenda.buscar_contacto("María")
    print(encontrado if encontrado else "No se encontró el contacto.")

    # Listar contactos en HTML
    print("\nGenerando listado en HTML:")
    agenda.listar_contactos_html()

    # Eliminar un contacto
    agenda.eliminar_contacto("María")

    # Listar contactos después de eliminación
    print("\nListado después de eliminación:")
    agenda.listar_contactos()
