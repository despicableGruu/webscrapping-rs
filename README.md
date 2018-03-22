# WebScraping
Práctica 1, Web Scraping

Descripción

El siguiente código en Python 3.6 tiene por objetivo aplicar las técnicas de Web Scraping para extraer datos de la web XXXX y generar como resultado un archivo de datos en formato CVS con los datos obtenidos.  

Esta práctica pertenece a la asignatura Tipología y ciclo de vida de los datos, correspondiente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. 

Miembros del equipo

Patricia Reyes Silva
José Pérez Sánchez


Contexto y justificación

Las nuevas tecnologías que permiten acceder de forma simultánea a los mercados de valores permiten la recopilación automática de datos con los que crear distintas estrategias de inversión. El poder automatizar la actualización automática de datos permite recalcular dichas estrategias, por empresas, por sectores, etc.., y, el poder actualizar automáticamente datos de distintos mercados permite realizar arbitrajes entre empresas que cotizan en distintos países, distintas monedas o incluso entre sectores de distintos países.

Un comienzo será la extracción de datos diaria de las cotizaciones de la Bolsa de Valores de Lima, a partir de los datos publicados en su página web, obteniendo los datos de mercado a fin de día cuando sean publicados.

El uso de lenguaje Python nos parece realmente conveniente para esta tarea, no sólo por su utilidad para realizar Scraping de páginas web, sino también por su potencial para el manejo de dataframes, incluyendo potentes librerías para el manejo de matrices con módulos como numpy, para el cálculo de ratios como el Sharpe, relación de una acción respecto a su índice, etc….



Características del Dataset

Representa las cotizaciones diarias de las acciones e índices cotizados en la bolsa de Lima. La estructura datos obtenido es:

•	Acción
    a.	Nombre
    b.	Nemónico
        i.	C1 acciones comunes?
        ii.	I1 acciones inversión
        iii.	Sin sufijo valores que cotizan también en extranjero (para arbitraje?)
    c.	Sector
        i.	Diversas
        ii.	Agrario
        iii.	Industriales
        iv.	Bancos – financieras..
        ....
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




Ficheros del código fuente
Aun no especificados

Recursos
1.	Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2.	Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
2.  Web de la Bolsa de Valores de Lima (BVL)
