# Proyecto de Análisis de Sentimientos en Twitter

## Autor: 
Oscar Pedreño Fernandez

## Contexto
Nos han encargado analizar el contenido de una base de datos de Twitter para un proyecto de procesamiento del lenguaje natural (NLP) relacionado con el análisis de sentimientos. Contamos con un dataset de 800,000 tweets y seis variables: 
- `sentiment`: indica si el sentimiento del tweet es positivo o negativo.
- `id`: identificador único del tweet.
- `date`: fecha de publicación del tweet.
- `query`: consulta asociada al tweet (en caso de no existir, se mostrará "NO_QUERY").
- `user`: nombre del usuario que publicó el tweet.
- `text`: contenido del mensaje del tweet.

Este proyecto tiene fines educativos y de aprendizaje.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

- Carpeta `data`: Contiene los datasets utilizados en el proyecto.
- Carpeta `test`: Contiene los tests unitarios para la limpieza de datos, control y análisis de los datos.
- `control.py`: Archivo Python que contiene la clase responsable de la limpieza y eliminación de ruido en los datos. El objetivo es generar el dataset limpio "twitter_processed.csv".
- `word_cloud.py`: Archivo Python que contiene la clase encargada de agrupar los datos y generar los wordclouds y histogramas. El objetivo es realizar el análisis y la exploración de los datos.
- `main.py`: Archivo Python donde se ejecutan todas las funciones paso a paso. Debe ser ejecutado para obtener los resultados.
- `license.txt`: Archivo de texto que proporciona información sobre la licencia del programa.
- `requirements.txt`: Archivo de texto que muestra las librerías necesarias para ejecutar el programa, junto con sus versiones. Para instalar las dependencias, ejecutar el comando `pip install -r requirements.txt`.
- `setup.py`: Archivo Python que contiene el script utilizado por setuptools para empaquetar y distribuir el paquete de Python.
- Carpeta `htmlcov`: Contiene información sobre los test coverages realizados en el programa.

## Preprocesamiento del Dataset
La primera parte del proyecto se enfoca en el preprocesamiento del dataset "twitter_cleaned_zip", que incluye la limpieza del ruido en el texto, la eliminación de stopwords que no aportan información relevante al análisis y la eliminación de tweets vacíos o sin valor.

## Análisis del dataset
La segunda parte se basa en la creación de wordclouds e histogramas que nos permitirán llegar a las conclusiones obtenidas.

## Tests y cobertura
Para ejecutar los tests debemos ir a la carpeta `test` y ejecutar los scripts `testControl.py` y `testword_cloud.py`

Para calcular su cobertura hemos utilizado la libreria `coverage.py` que mediante el comando `python -m coverage run <nombre_del_script>` nos genera una ejecución del código y un reporte html (mediante el comando `coverage html`). Estos reportes se pueden encontrar en la carpeta **htmlcov**.

El proyecto utiliza las siguientes librerías:
- `pandas`: Utilizada para el manejo y procesamiento de datos tabulares.
- `Matplotlib`: Empleada para la visualización de gráficos y generación de histogramas.
- `WordCloud`: Usada para la creación de nubes de palabras a partir de frecuencias de términos.
- `os`: Utilizada para interactuar con el sistema operativo y realizar operaciones relacionadas con archivos y directorios.
- `re`: Empleada para realizar operaciones de expresiones regulares y manipulación de texto.

Si no se pueden visualizar los gráficos, se debe instalar tkinter mediante el comando `pip install tk` para poder visualizar los wordclouds.

## Resultados y Conclusiones
Los resultados obtenidos del análisis de sentimientos en la base de datos de Twitter revelan patrones interesantes en el uso de palabras y términos. Se pudo observar que las palabras más utilizadas en las críticas positivas incluyen "I'm", "good", "love", "get", "thanks", entre otras. Por otro lado, en las críticas negativas se destacan palabras como "I'm", "I", "work", "get", "don't", entre otras.

Asimismo, se identificaron palabras generales que aparecen en ambos tipos de críticas, aunque con frecuencias diferentes. Estas palabras, como "I'm", "get" y "go", indican que su uso varía dependiendo del sentimiento expresado.

Un análisis más detallado revela que en las críticas negativas se enfatiza más el autorreferencialismo y se mencionan con mayor frecuencia temas relacionados con el trabajo, la escuela, así como expresiones negativas como "no puedo" y referencias a enfermedades. Por otro lado, en las críticas positivas se observa una menor referencia al "yo" y se habla más de amor, tiempo y días.

En resumen, este análisis de sentimientos en la base de datos de Twitter proporciona información valiosa sobre las palabras y términos utilizados en críticas positivas y negativas. Estos resultados pueden ser útiles para comprender las tendencias y opiniones de los usuarios en las redes sociales.
