from lxml import etree
from suds.client import Client
import os


cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)
peticion = raw_input("Introduce una linea de Tussam: ")
respuesta = cliente.service.GetStatusLinea(peticion)

raiz = etree.fromstring(respuesta)
raiz2 = raiz[0][0]

prefijo = "{http://tempuri.org/}"

activos = raiz2.find(prefijo+"GetStatusLineaResult/"+prefijo+"activos")
frecuencia = raiz2.find(prefijo+"GetStatusLineaResult/"+prefijo+"frec_bien")
graves = raiz2.find(prefijo+"GetStatusLineaResult/"+prefijo+"graves")

os.system("clear")

print "En este momento hay %s activos , %s bien de frecuencia y %s incidencias" % (activos.text,frecuencia.text,graves.text)
