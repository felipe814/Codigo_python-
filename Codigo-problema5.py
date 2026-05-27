# Matriz: [Nombre,Lunes, Martes, Miercoles,Jueves,Viernes]
equipo = [
    ["Ana",8,8,8,8,8],
    ["Carlos",9,8,9,8,9],
    ["Laura",7,8,7,8,7],
    ["Pedro",10,9,8,9,8]
]
 #Función para calcular y clasificar las horas 
def calcular_jornada(recurso):
    total_horas=sum(recurso[1:]) #Suma las horas de lunes a viernes
    if total_horas>40:
        clasificacion="Sobretiempo; El total de horas es mayor al umbral de 40 horas"
    else:
        clasificacion="Horario estandar; El total de horas no excede el umbral"
    return total_horas, clasificacion

#Mostrar resultados 
for recurso in equipo:
    nombre= recurso[0]
    total, clasificacion = calcular_jornada(recurso)
    print("Nombre persona: ",nombre)
    print("Total de horas trabajadas: ",total)
    print("Clasificación: ",clasificacion)
    print("_________________________________")
