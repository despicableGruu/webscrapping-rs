import os
import requests
import csv
import argparse
from datetime import datetime
from datetime import timedelta

from bs4 import BeautifulSoup

#Current directory where is located the script
#currentDir = os.path.dirname("C:/temp")
#filename = "food_prices_dataset.csv"
#filePath = os.path.join(currentDir, filename)


#Function to get prices of webpage
def readDailyStockPrizes(listaCotizaciones):
    
  mercadoAlDiaUrl = "http://www.bvl.com.pe/includes/cotizaciones_todas.dat"
  response= requests.get(mercadoAlDiaUrl)
  soup = BeautifulSoup(response.text,"html.parser")
  table=soup.find('table');
  
  
  print(table)
  
  currentIndex=0
  for row in table.findAll("tr"):
      cells = row.findAll('td')
      
      print("current Index")
      print(currentIndex)
      currentIndex=currentIndex+1
      if (currentIndex > 3):
     #This is because exists rowspan, if not use the previous category
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
          cotizacion=[empresa,nemonico,sector,segmento,moneda,anterior,fechaAnterior,apertura,ultima, variacion,compra,venta,numeroAcciones,numeroOperaciones, montoNegocio]
          listaCotizaciones.append(cotizacion)
      
  return


cotizaciones=[]
headerList=["Empresa","Nemónico","Sector","Segmento","Moneda","Anterior","Fecha Anterior","Apertura","Última","Variación","Compra", "Venta","Número Acciones","Número Operaciones", "Monto Negocio"]
cotizaciones.append(headerList)

print(cotizaciones)
    

readDailyStockPrizes(cotizaciones)

print(cotizaciones)

currentDir = os.path.dirname(__file__)
filename = "cotizacionesDiarias.csv"
filePath = os.path.join(currentDir, filename)

with open(filePath, 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for cotizacion in cotizaciones:
    writer.writerow(cotizacion)
