import os
import requests
import csv
import argparse
from datetime import datetime
from bs4 import BeautifulSoup


def getLastMarketDate():
        
    # Obtener fecha del día de cotización que se obtiene
    
    urlTotalCotizaciones = "http://www.bvl.com.pe/jsp/cotizacion.jsp?&fec_fin=20300101"
    response= requests.get(urlTotalCotizaciones)
    soup = BeautifulSoup(response.text,"html.parser")
    table=soup.find('table');  
    currentIndex=0

    for row in table.findAll("tr"):
        cells = row.findAll('td')
        currentIndex=currentIndex+1
        if (currentIndex == 3):
            return (cells[0].find(text=True))
            break


def getCompanyData(nemonic):
        
    # Datos Adocionales de la empresa    
    
    mercadoAlDiaUrl = "http://www.bvl.com.pe/includes/cotizaciones_todas.dat"
    response= requests.get(mercadoAlDiaUrl)
    soup = BeautifulSoup(response.text,"html.parser")
    table=soup.find('table');  

    nemonic = nemonic.strip()

    currentIndex=0
    for row in table.findAll("tr"):
      cells = row.findAll('td')

      currentIndex=currentIndex+1
     
      if (currentIndex > 3):
          
          nemonico=cells[2].find(text=True)          
          
          if nemonic == nemonico.strip(): 
              
              print ("Encontrado")              
              print(nemonico.strip())    
              
              empresa=cells[1].find(text=True)
              print (empresa)              
              
              nemonico=cells[2].find(text=True)
              sector=cells[3].find(text=True)
              segmento=cells[4].find(text=True)
              moneda=cells[5].find(text=True)	  
                    
              return [empresa,sector,segmento,moneda]
              


#Funcion para obtener los datos de las cotizaciones diarias, del último día de cotización
def readDailyStockPrizes():    
    
    cotizaciones=[]

    headerList=["Fecha-Hora Descarga", "Fecha cotización","Imagen","Estado","Empresa","Nemónico","Sector","Segmento","Moneda","Anterior","Fecha Anterior","Apertura","Última","Variación","Compra", "Venta","Número Acciones","Número Operaciones", "Monto Negocio"]

    cotizaciones.append(headerList)

#Obtenemos cuál fue el último día de cotización efectivo.
    diaCotizacion = getLastMarketDate()

    cot = diaCotizacion.replace("/","")

#Obtenemos los datos del último día cotizado para todas las compañías en Bolsa de Lima    
    
    mercadoAlDiaUrl = "http://www.bvl.com.pe/includes/cotizaciones_todas.dat"
    response= requests.get(mercadoAlDiaUrl)
    soup = BeautifulSoup(response.text,"html.parser")
    table=soup.find('table');  
    
    #Momento actual de la lectura
    diahora= datetime.now().strftime("%d-%m-%Y %H:%M")
    
    currentIndex=0
    for row in table.findAll("tr"):
      cells = row.findAll('td')

      currentIndex=currentIndex+1
     
      if (currentIndex > 3):
      
          fecha = diahora
          imagen = cells[0].find('img')['src']
          empresa=cells[1].find(text=True)
          nemonico=cells[2].find(text=True)
          sector=cells[3].find(text=True)
          segmento=cells[4].find(text=True)
          moneda=cells[5].find(text=True)	  
          anterior=cells[6].find(text=True)
          fechaAnterior=cells[7].find(text=True)
          apertura=cells[8].find(text=True)
          ultima=cells[9].find(text=True)
          variacion=cells[10].find(text=True)
          compra=cells[11].find(text=True)
          venta=cells[12].find(text=True)
          numeroAcciones=cells[13].find(text=True)
          numeroOperaciones=cells[14].find(text=True)
          montoNegocio=cells[15].find(text=True)		
          
          if imagen == '/images/azul1.jpg':
              estado = 'Igual'
          elif imagen == '/images/flecha_roja-b.gif':
              estado = 'A la baja'
          else :
              estado = 'Al alza'
            
          cotizacion=[fecha,diaCotizacion,imagen,estado,empresa,nemonico,sector,segmento,moneda,anterior,fechaAnterior,apertura,ultima, variacion,compra,venta,numeroAcciones,numeroOperaciones, montoNegocio]
          cotizaciones.append(cotizacion)

    # Generación del fichero csv de datos. 
    # El nombre del fichero es CotizacionesDiarias_YYYYMMDD.csv
    # Indicando el día de cotización que incluye.
    currentDir = os.path.dirname(__file__)
    filename = "CotizacionesDiarias_" + cot[4:8]+ cot[2:4]+cot[:2]+ ".csv"
    filePath = os.path.join(currentDir, filename)
      
    print (filePath) 

    with open(filePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for cotizacion in cotizaciones:
            writer.writerow(cotizacion)
  



# Funcion para obtener los datos de las cotizaciones de la compañía indicada por nemonic
# entre las fechas indicadas. Sino se indican se cargarán todos los datos disponibles            
def readCompanyStockPrizes(nemonic, startDate, endDate):    
    
    cotizaciones=[]

    headerList=["Fecha-Hora Descarga", "Fecha cotización","Imagen","Estado","Empresa","Nemónico","Sector","Segmento","Moneda","Anterior","Fecha Anterior","Apertura","Última","Variación","Compra", "Venta","Número Acciones","Número Operaciones", "Monto Negocio"]
    
    nemonic = nemonic.upper()
  
    # Obtener datos adiconales de la compañía aparte de cotizaciones:
    # nombre de la empresa, sector, segmento y moneda
    
    datosCompania = getCompanyData(nemonic)
    
    if (datosCompania == None):
        # Si no se encuentra la compañía se retorna con mensaje de error.
        print ("Error, compañía " + nemonic + " no encontrada!!!")
        return
    
    empresa = datosCompania[0]
    sector = datosCompania[1]
    segmento = datosCompania[2]
    moneda = datosCompania[3]

    cotizaciones.append(headerList)

    
    # Preparación de parámetros de consulta
    
    payload =  {'nemonico': nemonic}

    if endDate == None:
        print("No se ha indicado fecha final. Se generará todos los datos disponibles.")
        payload['fec_fin'] = '20300101'
        
    else:
        payload['fec_fin'] = endDate        
        if startDate == None:
            print("No se ha indicado fecha inicial. Se generará todo hasta la fecha final.")
            payload['fec_inicio'] = '20000101'
        else:
            payload['fec_inicio'] = startDate
            
    diahora= datetime.now().strftime("%d-%m-%Y %H:%M")
    
    currentIndex=0
    estado = ""
    imagen = ""
    compra=""
    venta=""
    numeroOperaciones=""            
    

    # Consulta datos de cotizaciones.
    urlCompania = "http://www.bvl.com.pe/jsp/cotizacion.jsp"
    response= requests.get(urlCompania, params=payload)            
    soup = BeautifulSoup(response.text,"html.parser")
    table=soup.find('table');  
    
    for row in table.findAll("tr"):
        
      cells = row.findAll('td')
      currentIndex=currentIndex+1
      
      if (currentIndex > 2):
     #This is because exists rowspan, if not use the previous category     
      
          diaCotizacion = cells[0].find(text=True)          
          anterior=cells[8].find(text=True)
          fechaAnterior=cells[9].find(text=True)
          apertura=cells[1].find(text=True)
          ultima=cells[2].find(text=True)
          variacion = "0.00"
          
          if ultima.strip() and ultima.strip():
              variacion = round((float(ultima) - float(apertura))/100,3)
                            
          numeroAcciones=cells[6].find(text=True)          
          montoNegocio=cells[7].find(text=True)		         

          cotizacion=[diahora,diaCotizacion,imagen,estado,empresa,nemonic,sector,segmento,moneda,anterior,fechaAnterior,apertura,ultima, variacion,compra,venta,numeroAcciones,numeroOperaciones, montoNegocio]
          cotizaciones.append(cotizacion)


    # Generación de fichero csv de cotizaciones. El nombre será
    # Cotizaciones_nemonico de la compañía.csv, por ejemplo Cotizaciones_BVN.csv
    currentDir = os.path.dirname(__file__)
    filename = "Cotizaciones_" + nemonic + ".csv"
    filePath = os.path.join(currentDir, filename)

    with open(filePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for cotizacion in cotizaciones:
            writer.writerow(cotizacion)
  
    

    
# Comienzo del script principal: 
            
parser = argparse.ArgumentParser()
parser.add_argument("--nemonic", help="Indique el nemónico de la compañía")
parser.add_argument("--startDate", help="Fecha de inicio, opcional, formato YYYYMMDD")
parser.add_argument("--endDate", help="Fecha fin, formato YYYYMMDD")
args = parser.parse_args()

if args.nemonic == None:
    print("No se indicó un nemónico, se generarán las últimas cotizaciones diarias")
    readDailyStockPrizes()
    
else:
    print("Buscando cotizaciones para " + args.nemonic)
    readCompanyStockPrizes(args.nemonic, args.startDate, args.endDate)

print ("Script Terminado")
