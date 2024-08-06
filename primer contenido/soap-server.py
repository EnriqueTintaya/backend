from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from zeep import Client

# Inicializa el cliente SOAP para el servicio externo
def SumaDosNumeros(x,y):
    return "esta es la suma de los numeros ingresados: {}".format(x+y)
def cadena(a,b):
    return "esta es la cadena conbinada : {}".format(a+" "+b)

def num(number):
    cliente=Client("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")
    return "Este es el número retornado por NumberToWords: {}".format(cliente.service.NumberToWords(number))
def invert(str1):
    origin=str1
    new_string=""
    for x in str1:
        new_string=x+new_string
    print(origin," ",new_string)
    if origin==new_string:
        return("es una palabra palindroma")
    else:
        return("no es una palabra palindroma")
# Configura el despachador SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Num",
    num,
    returns={"resultado": str},
    args={"number": int},
)
dispatcher.register_function(
    "Sum",
    SumaDosNumeros,
    returns={"resultado":str},
    args={"x":int,"y":int},
)
dispatcher.register_function(
    "Cadenas",
    cadena,
    returns={"resultado":str},
    args={"a":str,"b":str},
)
dispatcher.register_function(
    "Invert",
    invert,
    returns={"resltado":str},
    args={"str1":str},
)
# Configura el servidor
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("SERVIDOR SOAP INICIADO EN http://localhost:8000/")
server.serve_forever()
