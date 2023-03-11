"""
Writing by: @malva
Last Edition: 2023-03-08
"""

# malva = ["Argentina",26, "Ingenieria en Sistemas",6]
# jack = ["Colombia", "Diseño", 8]

class PersonaClass:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Programador(PersonaClass):
    text_1 ='hola el dev 1 se llama '
    text_2 =' y su especialidad es '
    text_3 =' y su stack tecnologico es '
    stack = []

    def __init__(self, nombre, edad, especialidad, stack = stack):
        super().__init__(nombre, edad)
        self.stack = stack
        self.especialidad = especialidad
    
    def stack_description(self):
        return f"{self.text_1} {self.nombre} {self.text_3} {self.stack}"
    
    def __str__(self):
        return f"{self.nombre} {self.edad} {self.especialidad} {self.stack}"

class ProjectManager(PersonaClass):
    
    def __init__(self, nombre, edad, especialidad, stack):
        super().__init__(nombre, edad)
        self.stack = stack
        self.especialidad = especialidad
    
    def __str__(self):
        return f"{self.nombre} {self.edad} {self.especialidad} {self.stack}"

stack = ['js','py','golang']

dev_1 = Programador('Malva', 26, 'front end', stack)
dev_2 = Programador('Rosa', 23, 'Back end', stack)
dev_3 = Programador('Manu', 34, 'front end', stack)
dev_4 = Programador('Elvira', 78, 'front end', stack)
pm_1 = Programador('Julieta', 35, 'MP')

# print(dev_1.stack_description())

print(dev_1)
print(dev_2)
print(dev_3)
print(dev_4)
print(pm_1)

# print(type(dev_1))

# print(isinstance(dev_1, Programador))


