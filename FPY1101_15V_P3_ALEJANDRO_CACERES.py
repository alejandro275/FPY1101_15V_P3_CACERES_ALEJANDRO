import os 
os.system ("cls")


def menu1() :
    try :
        nif_v = int(input("ingrese su nif "))
        if nif_v != 00000000 or nif_v <= 99999999 :
            print("nif valido")
        else :
            ("nif invalido , reintente  ")

        nif_v2 = input("ingrese ultimos 3 digitos de su nif")
        if nif_v2 != 0  or nif_v2<4 :
            print("codigo valido ")
        else :
            print("nif codigo invalido ")
            
        edad_v = int(input("ingrese edad "))
        if edad_v > 15 :
            print("edad guardada correctamente ")
        else :
            print("edad incorrecta , reintente ")
                    
        nombrev = input("ingrese nombre ")
        if nombrev != " " :
            print("nombre valido")
        else :
            print("nombre invalido , intente nuevamente  ")
    except :
        print("fin de grabado") 
        
    nif = {
    "nif":nif_v,
    "codigo nif":nif_v2,
    "edad":edad_v,
    "nombre":nombrev
     
    } 
    print("los datos an sido guardados correctamente , los datos son = ", nif )
#fin menu grabado 
        
def menu2():
#menu de buscar 
    buscar_v =int(input("ingrese nif que desee buscar "))
    if buscar_v in nif : 
            print("los datos de la persona son =", )
    else :
            print("nif no esta guardado ")

    if nif == "SP" :
            print("persona pertenece a españa ")
    else :
        print("pertenece a otro pais ")
    #fin de menu buscar 
          
def menu3():
    certificados=print("1.nacimiento")
    certificados=print("2.estado conyugal")
    certificados=print("3.Perteneciente a la union europea") 
    certificados=print("4.salir")
    try:
        certificados=input("que certificado desea sacar ?")
        if certificados == 1 :
            validacion1 =input("el certificado de nacimiento tiene un valor de 1.500 , desea continuar ? Y/N")
            if validacion1 == "Y " :
                print("el certificado de nacimiento es ---------------------------")
            else :
                print("volviendo al menu ")
        else :
            print("error ")
            
        if certificados == 2 :
            validacion2 =input("el certificado de nestado conyugal tiene un valor de 2.500 , desea continuar ? Y/N")
            if validacion2 == "Y " :
                print("el certificado de estado conyugal es ---------------------------")
            else :
                print("volviendo al menu ")
        else :
            print("error ")
        if certificados == 3 :
            validacion3 =input("el certificado Perteneciente a la union europea tiene un valor de 5.000 , desea continuar ? Y/N")
            if validacion3 == "Y " :
                print("su certificado es  ---------------------------")
            else :
                print("volviendo al menu ")
        else :
            print("error ")
    except certificados == 4 :
        print("volviendo al menu principal")
    
#ingreso a la pag 
print("BIENVENIDO AL SISTEMA DE NIF DE LA UNION EUROPEA")
 
#menu de opciones 
menu =print("1.grabar nif ")
menu =print ("2.buscar ")
menu=print("3.imprimir certificado")
menu=print("4.salir ")
menu=int(input("ingrese opcion que desea "))
try :
    if menu ==1 :
        menu1()

    if menu == 2 :
        menu2()

    if menu == 3:
        menu3()
except menu == 4 :
    print("hasta luego ")
#fin menu de opciones 