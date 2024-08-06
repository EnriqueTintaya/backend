from zeep import Client

# Crear el cliente con la URL del WSDL
client = Client("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")

# Imprimir los servicios y métodos disponibles
print(client.service)

# Llamar al método del servicio web
result = client.service.NumberToWords(5)

# Imprimir el resultado
print(result)
