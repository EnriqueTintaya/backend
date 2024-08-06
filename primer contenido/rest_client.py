import requests
url="http://localhost:8000/"
#GET
ruta_get =url+"lista_estudiantes"
get_response=requests.request(method="GET",url=ruta_get)
print(get_response.text)
#POST
ruta_post=url+"agrega_estudiante"
nuevo_estudiante={
    "nombre":"Puanito",
    "apellido":"Perez",
    "carrera":"Ingenieria Agronomica",
}
post_response= requests.request(method="POST",
                                url=ruta_post,
                                json=nuevo_estudiante)
print(post_response.text)
#FUNCION PARA BUSCAR EN LA LISTA UN NOMBRE CON P1 6:07 time  leveling

ruta_get=url+"obtener_name_p"
buscando_con_la_letraP=requests.request(method="GET",url=ruta_get)
print("Aqui empieza la f")
print(buscando_con_la_letraP.text)
print("esto termino")

ruta_get=url+"Cantidad_estudiantess_carrera"
contando_estudiantes_carrera=requests.request(method="GET",url=ruta_get)
print(contando_estudiantes_carrera.text)

ruta_get=url+"Cantidad_estudiantes_total"
Estudiantes_total=requests.request(method="GET",url=ruta_get)
print("esto es el numero total de estudiantes :")
print(Estudiantes_total.text)