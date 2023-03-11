"""
Script made by Malva
Year: 2023/03/07
"""

# crush = "Ella"
# num = 5
# NUM2 = 8
crush, num, NUM2 = "Ella", 5, 8
x = y = z = "Ella no te ama"

# Cast
numString = str(num)
num_integer = int(num)
_num_float = float(num)
_numFloat2 = float(num)
_num_Float2 = float(NUM2)

print(type(numString) )
print(type(num_integer))
print(type(_num_float))

# ellaTeAma = False

# if num > 2:
#     print(crush+" no te ama")

# Unpack a Collection
frutas = ['fresa','mango','kiwi']
x, y , z = frutas
print(x, y, z)
print(x + y + z)
print(num + NUM2)
# print('5'+num) TypeError: can only concatenate str (not "int") to str


palabra = "ella no te ama 💔"

def miPrimerFuncion():
    global palabra
    palabra = "Ella ama a tu mejor amigo"
    print(palabra)

miPrimerFuncion()
print(palabra)
#  Tipos de datos

x = str("Hola Crayola")
print(x)
x = int(10)
print(x)
x = float(12.5)
print(x)
x = complex(1j)
print(type(x))
x = list(('fresa','banana', 'sandia'))
frutas = ['fresa','mango','kiwi']
print(type(frutas))
x = tuple(('Cholate','Milk', 'Cereal'))
print(type(x))
x = dict(nombre='Malva', edad=26)
print(type(x))