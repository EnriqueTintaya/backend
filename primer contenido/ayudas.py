estudiantes=[{
    "a":"1",
    "b":"2" 
    },
    {
    "a":"13",
    "d":"4"
    },{
    "a":"25",
    "f":"6"
    }]
respuesta=[]
for itm in estudiantes:
    if itm.get("a")[0]=='1':
        respuesta.append(itm.get("a"))
estudiantes[0]["aa"]=1
for vector in respuesta:
    print(vector)


for itm in estudiantes:
    print("-------")
    for valor in itm:
        print(valor)
        
print("tamaño del dic0")
print(len(estudiantes[0]))
print(".....")
lista=(estudiantes[0].keys())
for element in lista:
    print(element)
