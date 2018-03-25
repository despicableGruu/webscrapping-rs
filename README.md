# WebScraping con Python 3.6

## Práctica 1, Web Scraping

## Descripción

El siguiente código en Python 3.6 tiene por objetivo aplicar las técnicas de Web Scraping para extraer datos de la web de la Bolsa de Valores de Lima y generar como resultado un archivo de datos en formato CVS con los datos obtenidos.  

Esta práctica pertenece a la asignatura Tipología y ciclo de vida de los datos, correspondiente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. 

## Miembros del equipo

Patricia Reyes Silva

José Pérez Sánchez


## Características del Dataset

El conjunto de datos a obtener, representa los datos referidos a las cotizaciones diarias de las acciones e índices cotizados en la Bolsa de Valores Lima de forma diaria. 

La práctica se articula con el siguiente esquema:

### 1 Título: "Valores negociados en al Bolsa de Lima"

### 2 Subtítulo: "Cotizaciones diarias"

### 3 Imagen: 

![Imagen Cotizaciones](https://raw.githubusercontent.com/jperezsanchezU/WebScraping/master/stock-marke-image.jpg)


### 4 Contexto y justificación

En la actualidad, las nuevas tecnologías hacen posible acceder a los mercados de valores del mundo simplemente visitando sus respectivas websites, sin movernos de nuestros escritorios.   Pero ¿qué pasaría si se requiere conocer los datos de las cotizaciones diarias de más de una bolsa de valores en las que se desea invertir? De la forma manual, se debería visitar diariamente cada una de las websites de interés y recoger manualmente los datos que necesitamos, pero existe tambien la modalidad automática de extracción de datos, que se vale de la ejecución de scripts para su recopilación.  En nuestro contexto, donde los datos se generan a velocidades cada vez mayores (Big Data), todas las herramientas que nos permitan acelerar la recopilación y posterior tratamiento de los mismos son bienvenidas.

La presente práctica tiene como objeto desarrollar un Script en el lenguaje de programación Python que  permita la extracción diaria de los datos correspondientes a las cotizaciones de la Bolsa de Valores de Lima, a partir de los datos publicados en su página web.

El uso de lenguaje Python nos parece realmente conveniente para esta tarea, no sólo por su utilidad para realizar Scraping (escarbar)  dentro de páginas web, sino también por su enorme potencial para el manejo de grandes conjuntos de datos, para lo cual incluye potentes librerías que facilitan su tratamiento permitiendo la elaboración de distintos modelo de análisis.


### 5 Contenido

Incluye el conjunto de acciones negociadas en la Bolsa de Lima, para cada valor negociado se obtendría, diariamente, la siguiente información:

•	Acción

    a.	Nombre
    
    b.	Nemónico  (C1 acciones comunes,	I1 acciones inversión, Sin sufijo, cotizan también en otras bolsas)
        
    c.	Sector (Diversas, Agrario, Industriales, Bancos – financieras, etc..)        
                
    d.	Segmento (Describe la liquidez de la acción)
    
•	Moneda de cotización de la acción (Sol/Dólar)

•	Cotizaciones


    a.	Precio de cierre día anterior    
    
    b.	Fecha de negociación anterior (no necesariamente día anterior)    
    
    c.	Precio apertura actual.    
    
    d.	Precio último del día.    
    
    e.	Variación del precio en % respecto al día anterior, positivo o negativo   
    

•	Propuestas

    a.	Precio mayor de Compra en el día    
    
    b.	Precio menor de Venta en el día
    

•	Negociación

    a.	Volumen de negociación
    
    b.	Número de operaciones    
    
    c.	Monto/importe negociado en la moneda de cotización
    

## Agradecimientos

A la Bolsa de Lima y su infraestructura informática.

## Inspiración

El áuge de las compañías FinTech y del trading algorítmico, así como la disposición de datos. 

## Licencia

-- A determinar

## Código

-- Aun no desarrollado

## Dataset

-- Dataset en formato CSV aún no obtenido

## Recursos
1.	Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2.	Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
2.  [Bolsa de Valores de Lima (BVL)](http://www.bvl.com.pe/)
