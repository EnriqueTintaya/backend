from zeep import Client

# Conecta al servidor SOAP local
client = Client('http://localhost:8000')
# Llama al servicio de conversión de número a palabras
#result = client.service.Num(number=5)
#result = client.service.Sum(5, 6)
result=client.service.Invert("radar")
print(result)
