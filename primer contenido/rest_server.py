from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estudiantes=[
    {
        "id":1,
        "nombre":"Pedrito",
        "apellido":"Garcia",
        "carrera":"Ingenieria de Sistemas",
        },
]
Respuesta=[]
Ncarreras={}
#POST
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path=='/obtener_name_p':
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.end_headers()
            ###logica
            for itm  in estudiantes:
                if itm.get("nombre")[0]=='P':
                    Respuesta.append(itm.get("nombre"))
            self.wfile.write(json.dumps(Respuesta).encode('utf-8'))       
            Respuesta.remove         
        elif self.path=='/Cantidad_estudiantess_carrera':
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.end_headers()
            #logica
            cont=0
            
            for itm in estudiantes:
                Ncarreras[itm.get("carrera")]=0
            listaC=Ncarreras.keys()
            for Carrera in listaC:
                for est in estudiantes:
                    if est.get("carrera")==Carrera:
                        cont=cont+1
                    Ncarreras[Carrera]=cont
                cont=0
            self.wfile.write(json.dumps(Ncarreras).encode('utf-8'))       
            Ncarreras.remove                   
            #Respuesta.remove
        elif self.path=='/Cantidad_estudiantes_total':
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.end_headers()
            #logica
            total=[]
            total.append(len(estudiantes))
            self.wfile.write(json.dumps(total).encode('utf-8'))            
        else:
            self.send_response(404)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))
    def do_POST(self):
        if self.path=='/agrega_estudiante':
            content_length =int(self.headers['content-length'])
            post_data=self.rfile.read(content_length)
            post_data=json.loads(post_data.decode('utf-8'))
            post_data['id']=len(estudiantes)+1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))
def run_server(port=8000):
    try:
        server_addres=('',port)
        httpd = HTTPServer(server_addres, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()
if __name__=="__main__":
    run_server()