listaEstudiantes = [] #lista vacia

class Estudiantes(object):
    def __init__(self, _cedula, _nombre, _apellido, _edad, _nota1, _nota2, _nota3): ##constructor
        self.cedula = _cedula
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.nota1 = _nota1
        self.nota2 = _nota2
        self.nota3 = _nota3
        self.notaFinal = (_nota1 + _nota2 + _nota3) / 3
        self.historial = [] # guarda eventos 
    def entregarDatos(self): ## entrega datos del usuario
        print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.cedula, self.nombre, self.apellido, self.notaFinal))#datos del usuario
    def editarNotas(self, _nota1, _nota2, _nota3):## parametros de notas 
        self.nota1 = _nota1
        self.nota2 = _nota2
        self.nota3 = _nota3
        self.notaFinal = (_nota1 + _nota2 + _nota3) / 3
        print("Registro Exitoso!")
    def incluirEvento(self, _nota1, _nota2, _nota3):##modificar nota
        return ("modificacion: Nota_1: {} Nota_2: {} Nota_3: {}".format(_nota1, _nota2, _nota3))
    def entregaHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))



def registrarEstudiante():
    print("Registro de Estudiantes\n")
    cedula = int(input("Ingrese el numero de cedula: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese su edad: "))
    nota1 = float(input("Ingrese nota 1: "))
    nota2 = float(input("Ingrese nota 2: "))
    nota3 = float(input("Ingrese nota 3: "))
    objAlumno = Estudiantes(cedula, nombre, apellido, edad, nota1, nota2, nota3)
    listaEstudiantes.append(objAlumno)

def listadoEstudiantes():
    print("Listado de Estudiantes\n")
    for objAlumno in listaEstudiantes:
        objAlumno.entregarDatos()

def buscarEstudiante():
    print("Buscar Estudiante\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            objAlumno.entregarDatos()

def modificarNotas():
    print("Modificar Notas\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            nota1 = float(input("Ingrese nota 1: "))
            nota2 = float(input("Ingrese nota 2: "))
            nota3 = float(input("Ingrese nota 3: ")) 
            objAlumno.editarNotas(nota1, nota2, nota3)
            objAlumno.entregarDatos()
            recepcionMensaje = objAlumno.incluirEvento(nota1, nota2, nota3)
            objAlumno.historial.append(recepcionMensaje)

def consultarHistorial():
    print("Consulta de Historial\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaEstudiantes:
        if cedula == objAlumno.cedula:
            for recepcionMensaje in objAlumno.historial:
                print("Evento: {}".format(recepcionMensaje))
            
def salir():
    print("Salida inminente...!")
    exit()

def main():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar Estudiante")
        print("2.- Mostrar Estudiantes")
        print("3.- Buscar Estudiante")
        print("4.- Modificar notas")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
        elif opcion == 3:
            buscarEstudiante()
        elif opcion == 4:
            modificarNotas()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            salir()

if __name__ == '__main__':
    main();