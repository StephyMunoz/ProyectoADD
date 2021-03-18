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
