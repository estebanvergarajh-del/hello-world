#ETAPAS:
#Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
import os
os.system("cls")
try:
    edad = int(input(f"Ingrese la edad: "))
    if edad < 18: 
        print(f"Es menor de edad({edad})")
    else:
        print(f"Es mayor de edad({edad})")
except ValueError:
    print(f"Debe ingresar un valor numerico entero")

#Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
#User1: pedro   	Contraseña1: 1234
#User2: angel		Contraseña2: a4s1

usuario = str(input(f"Ingrese el nombre de usuario: "))
contraseña = str(input(f"Ingrese la contraseña: "))
if usuario == "pedro" and contraseña == "1234":
    print(f"Ingresó a User1 ({usuario})")
elif usuario == "angel" and contraseña == "a4s1":
    print(f"Ingresó a User2 ({usuario})")
else:
    print("Usuario o contraseña erroneas")

#Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

try:
    nota1 = float(input(f"Ingrese nota 1: "))
    nota2 = float(input(f"Ingrese nota 2: "))
    nota3 = float(input(f"Ingrese nota 3: "))
    promedio = (nota1 + nota2 + nota3)/3
    if promedio >= 4:
        print(f"Está aprobado ({promedio})")
    else:
        print(f"Está reprobado ({promedio})")
except ValueError:
    print("Debe ingresar un valor numerico")