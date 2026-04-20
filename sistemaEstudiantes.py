
opciones = ""
estudiantes = []
sedes = ("Norte", "Centro")
materias = {"Matemáticas", "Español", "Historia", "Filosofia","Informatica"}

#menu
while opciones != "5":
    print("1) Registro de estudiante")
    print("2) Ver todos los estudaintes")
    print("3) Ver SEDES")
    print("4) Ver materias")
    print("5) Salir del menu")
    opciones = input("Elige una opcion: ")

    if opciones == "1":
        print("Registro de estudiante")
        estudiantes1 = { 
            "Nombre": input("Ingrese el nombre del estudiante"),
            "Edad": input("Ingresa la edad"),
            "ID": input("Ingrese la indetifiación"),
            "fecha_nacimiento": input("Ingrese la fecha de nacimiento del estudiante"),
            "direccion": input("Ingrese la direción del estudiante"),
            "numero_de_contacto": input("Ingrese el numero de contacto"),
            "Faltas": input("Ingrese las faltas del estudiante"),
            "es_estudiante":True
        }
        estudiantes.append(estudiantes1)
    elif opciones == "2":
        print("ver todos los estudiantes")
        
        if len(estudiantes)==0:
            print("No se han registrado estudiantes, por favor ingrese al menos un estudiante")
        else:
            print("el total de de estudiantes es: ", len(estudiantes))
            for listadoEstudiantes in estudiantes:
                print(listadoEstudiantes) 
                
    elif opciones == "3":
        print("Ver SEDES")
        for listadoSedes in sedes:
            print(listadoSedes)
    elif opciones == "4":
        print("Ver materias")
        for listadoMaterias in materias:
            print(listadoMaterias)


    
