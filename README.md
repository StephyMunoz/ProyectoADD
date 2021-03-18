# ARQUITECTURA DATALAKE DE TEMAS POLITICOS, SALUD Y ENTRETENIMIENTO 

## Integrantes:
Cristian Mañay
Stephanie Muñoz
Luis Ortiz

## Casos de estudio

Se plantearon 5 temas que tienen un gran impacto en la actualidad, ejemplos que afectan a la sociedad directamente. 

Pulso político en 20 ciudades principales de Ecuador. 

Pulso político por provincias en Ecuador. 

Juegos en línea por países. 

Evolución del Covid19. 

Eventos y noticias mundiales. 

## Pulso político en 20 ciudades principales de Ecuador

Para el tema de pulso político en 20 ciudades de Ecuados, se obtiene información la red social Twitter por medio de filtro de geolocalización y también mediante filtro de palabras utilizando así palabras clave con temas relevantes de la política actual como son las elecciones presidenciales, esto se lo realizó por medio de scripts de python que guardan directamente la información en la herramienta elasticsearch para su posterior análisis.  También se recolectaron datos de la red social Facebook, los cuales fueron almacenados en la base de datos NoSQL MongoDBs Atlas, y se pasó a otra base de datos no relacional llamada CouchDB para su posterior análisis. 
Una vez concluida la recopilación de datos se procede a usar la herramienta Kibana para realizar un análisis gráfico de los datos, ya que esta herramienta permite tener todos los campos recopilados y usarlos de diferentes maneras dependiendo de la visualización que queramos lograr. 

![image](https://user-images.githubusercontent.com/58042439/111574375-6084ae00-877a-11eb-84fd-f251dd673e14.png)

## Pulso político por provincias en Ecuador

Se realizó el levantamiento de la información por medio de la red social Twitter con filtros por tema, en este caso de la actual coyuntura política debido a las elecciones, estos datos fueron almacenados en la base de datos no relacional CouchDB y por medio de un script de python se subieron los datos a la herramienta elasticsearch para su posetior análisis. Adicional a esto, se realizó un scrapping de la red social Tiktok con el objetivo de ver la percepción y el alcance de cada candidato a la presidencia en esta red social. Se generó mediante la herramienta tik-tok scraper un archivo csv con las estadísticas generadas de cada video publicado por los candidatos a la presidencia Guillermo Lasso y Andrés Arauz. 
Para el análisis se utilizó tanto la herramienta Kibana para los datos obtenidos en tiempo real desde Twitter y para los datos recopilados desde Tiktok se utilizó la herramienta Tableau Public para generar las visualizaciones. 

![image](https://user-images.githubusercontent.com/58042439/111574571-bb1e0a00-877a-11eb-8af8-2490cb46df84.png)

## Juegos en línea por países

Para este tema, se obtiene información de la página web de newzoo.com en la cual se encuentra estadísticas de varios temas, en este caso se extrajo datos referentes al mayor número de ventas de videojuegos en cada país, por medio de WebScraping, se utilizó un script de Python para la extracción de información. Para complementar la información también se obtiene un dataset desde la página de Kagle sobre videojuegos en el cual se clasificaban por las ventas en cada región. 
Una vez recolectados los datos, se realizó un análisis de la información obtenida, en la cual se extrajo información sobre ventas de videojuegos en 100 países. En el dataset de Kaggle se encontró registros de 16710 juegos con información de género, rating, calificación, número de usuarios y ventas por cada región.  

![image](https://user-images.githubusercontent.com/58042439/111577288-fbcc5200-877f-11eb-8c6a-7ca6b83b4950.png)

## Evolución del Covid19. 

Se obtiene datos de la red social Twitter, el tema Covid19 influye directamente en la actualidad, generando datos constantemente. Con la ejecución de scripts realizados en Python se obtiene un scraping de la red social que se almacena directamente en una base de datos NoSQL. Los datos son importados en archivos CSV para generar su correspondiente visualización en la herramienta Tableau. 
Para obtener una proyección diferente de datos se utiliza una base de datos SQL para crear tablas y así subir esta información en Elasticsearch y generar las visualizaciones en Kibana. Una vez recolectada la información de diferentes fuentes, se procede a convertir en archivos csv o Excel, los cuales facilitan su importación en otra herramienta de visualización en este caso Tableau. 

![image](https://user-images.githubusercontent.com/58042439/111577476-5665ae00-8780-11eb-8fdf-ca550ad69e20.png)


## Eventos y noticias mundiales. 

Se obtienen datos de Twitter tanto de los usuarios como DW español Y la BBC, se guardan en bases de datos NoSQL. Adicional se realiza un Web Scraping de las páginas web oficiales de estas cadenas de noticias para obtener una versión diferente de los datos. Una vez recolectada la información de diferentes fuentes, se procede a convertir en archivos csv o Excel, los cuales facilitan su importación en otra herramienta de visualización en este caso Tableau. 

![image](https://user-images.githubusercontent.com/58042439/111577577-8ad96a00-8780-11eb-9b82-c791c7c61e52.png)

## Link a datasets utilizados:

https://epnecuador-my.sharepoint.com/personal/luis_ortiz02_epn_edu_ec/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9lcG5lY3VhZG9yLW15LnNoYXJlcG9pbnQuY29tLzpmOi9nL3BlcnNvbmFsL2x1aXNfb3J0aXowMl9lcG5fZWR1X2VjL0VpOTM0RE9fN2ZwRXVaYmp0ajY5SzhBQjlScTFMbkVTdjZ4SV9kRm9Xa0tYeFE%5FcnRpbWU9bFZpQ0pvemgyRWc&id=%2Fpersonal%2Fluis%5Fortiz02%5Fepn%5Fedu%5Fec%2FDocuments%2FPTDC%5F%20documentos%20compartidos%2FDataset%5Ftemas%2Erar&parent=%2Fpersonal%2Fluis%5Fortiz02%5Fepn%5Fedu%5Fec%2FDocuments%2FPTDC%5F%20documentos%20compartidos
