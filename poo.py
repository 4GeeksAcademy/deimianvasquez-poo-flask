class Human: 

    def __init__(self, nombre, apellido, edad, color_piel):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.color_piel = color_piel
        self.caminando = False
        
    
    def __repr__(self):
        return "<class Human>"
    

    def saludar(self):
        print(f"Hola ¿qué tal {self.nombre} {self.apellido} ?") 


    def despedirse(self):
        print(f"Bye señor {self.nombre} {self.apellido}")


    def informacion(self):
        print(
            f"nombre: {self.nombre}"
            f"\napellido: {self.apellido}"
            f"\nedad: {self.edad}"
            f"\ncolor piel: {self.color_piel}"
        )

    def caminar(self, data):
        self.caminando = data

    def serialize(selt):
        return {
            "nombre": selt.nombre,
            "apellido": selt.apellido
        }


class Trabajador(Human):

    def __init__(self, salario, profesion, humano_nombre, humano_apellido, humano_edad, humano_color_piel):
        super().__init__(humano_nombre, humano_apellido, humano_edad, humano_color_piel)

        self.salario = salario
        self.profesion = profesion



    # def informacion(self):
    #     print(
    #         f"nombre: {self.nombre}"
    #         f"\napellido: {self.apellido}"
    #         f"\nedad: {self.edad}"
    #         f"\ncolor piel: {self.color_piel}"
    #         f"\nsalario: {self.salario}"
    #         f"\nprofesion: {self.profesion}"
    #     )


    def informacion(self):
        super().informacion()
        print(
            f"salario: {self.salario}"
            f"\nprofesion: {self.profesion}"
        )
       
            

arr = []

huttman = Human("Huttman", "Ochoa", 21, "claro")
arr.append(huttman)
huttman.saludar()
huttman.informacion()
huttman.despedirse()
huttman.caminar(True)
huttman.informacion()



print("*"*80)
trabajador_deimian = Trabajador(1500, "presidente", "José", "Trump", 112, "transparente")
trabajador_deimian.informacion()
arr.append(trabajador_deimian)

for person in arr:
    print(person.serialize())

# print(arr)
 


