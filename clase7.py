import random
import time

dic_usu = {}
print("Bienvenido a nuestra app de registro de usuarios")
def app ():
        usuario = str(input("Ingrese su nombre de usuario: ")) 
        contraseña = str(input("Ingrese su contraseña: "))
        edad = random.randint(10, 80)
        dic_usu.update({usuario: [contraseña, edad]})
        print("La lista de usuarios agregados es:")
        for i, j in dic_usu.items():
            print(i,":",j)
            time.sleep(5)
        pregunta = str(input("¿Desea continuar ingresando usuarios? (s/n) "))
        if pregunta == 's':
            app()
        else: 
            print("Gracias por visitarnos")
app()