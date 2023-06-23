from zipfile import ZipFile
import pandas as pd
import re


class ControlCsv:
    def __init__(self, path: str):
        self.path = path
        self.output_dir = "data"

# 1.1 Descomprimid el fichero twitter.zip y guardad su contenido en la carpeta data del proyecto.
    def unzip(self):
        """
            Descomprime un archivo zip.

            Extrae los archivos contenidos en el archivo zip especificado por `self.path`
            y los guarda en la carpeta de salida especificada por `self.output_dir`.

            Args:
                - self.path (str): Ruta del archivo zip a descomprimir.

            Returns:
                None
        """

        # https://www.geeksforgeeks.org/unzipping-files-in-python/
        with ZipFile(self.path, "r") as zipObject:
            zipObject.extractall(path=self.output_dir)
            print(f"Files unzipped successfully in folder {self.output_dir}")

    def create_listdicts(self):
        """
        Crea una lista de diccionarios a partir de un archivo CSV.

        Lee el archivo CSV especificado (`twitter_reduced.csv`) ubicado en la carpeta de salida,
        carga los datos en un DataFrame de Pandas y luego convierte cada fila del DataFrame en un diccionario.
        El resultado es una lista de diccionarios, donde cada diccionario representa un registro del archivo CSV.

        Prints:
            - Los 5 primeros registros del dataset.

        Returns:
            None
        """
        # 1.2 Leed el fichero twitter.csv y cargad el dataset como una lista de diccionarios.
        # Cada fila del fichero original corresponderá con un diccionario siguiendo la estructura de este ejemplo:
        # Mostrad por pantalla los 5 primeros registros del dataset mediante print.
        self.df = pd.read_csv(f"{self.output_dir}/twitter_reduced.csv")
        self.comments = self.df.to_dict(orient="records")
        print("The list of dictionaries has been created. Use method comments() to interact.")

    def clean_comments(self, text: str) -> str:
        """
        Limpia los comentarios de texto.

        Realiza una serie de transformaciones en el texto de los comentarios para limpiarlos:
        - Elimina las URLs presentes en el texto.
        - Elimina los caracteres no ASCII.
        - Convierte el texto a minúsculas.
        - Elimina los caracteres especiales y puntuación del texto.

        Args:
            - text (str): El texto del comentario a limpiar.

        Returns:
            str: El texto limpio resultante.

        """
        self.text = text
        # Eliminar URLs.
        self.text = re.sub(r'http\S+|www.\S+', '', self.text)
        # Eliminar carácteres no ASCII.
        # https://stackoverflow.com/questions/21472809/python-what-does-encodeascii-ignore-do
        self.text = self.text.encode('ascii', 'ignore').decode('utf-8')
        # Convertir a minúsculas.
        self.text = re.sub(r'[^\w\s]', '', self.text.lower())
        return self.text

# Eliminad las stopwords de los textos de los tuits y mostrad por pantalla las 5 últimas filas.
    def drop_stopwords(self, text, words: list) -> str:
        """
        Elimina las palabras stopwords del texto.

        Remueve las palabras stopwords del texto proporcionado, reemplazándolas por espacios en blanco.

        Args:
            - text (str): El texto al que se le eliminarán las stopwords.
            - words (list): Una lista de palabras stopwords a eliminar.

        Returns:
            str: El texto resultante después de eliminar las stopwords.

        """
        self.text = text
        self.words = words
        for word in self.words:
            self.text = self.text.replace(" " + word + " ", " ")
        return self.text


# Obtened las frecuencias de términos de cada tuit y almacenadlas en una lista de diccionarios en la que cada
# diccionario indique las palabras y su frecuencia de aparición en el tuit. Obtened también un vocabulario
# con todas las palabras únicas del dataset y guardadlas en una lista. Mostrad por pantalla los 5 primeros
# elementos de la lista de diccionarios obtenida. Ordenad alfabéticamente el vocabulario y mostrad por pantalla
# las 10 primeras palabras.
    def split_words(self, text: str) -> list:
        """
        Divide el texto en palabras.

        Divide el texto en palabras utilizando una expresión regular que selecciona palabras
        que consisten únicamente de letras del alfabeto.

        Args:
            - text (str): El texto a dividir en palabras.

        Returns:
            List: Una lista de palabras obtenidas del texto.
        """
        self.text = text
        self.text_words = re.findall(r'\b[a-zA-Z]+\b', self.text)
        return self.text_words

    def words_freq(self, text: str) -> dict:
        """
        Calcula la frecuencia de las palabras en el texto.

        Calcula la frecuencia de las palabras en el texto proporcionado.
        Devuelve un diccionario donde las claves son las palabras y los valores son
        las frecuencias correspondientes.

        Args:
            - text (str): El texto del cual se calculará la frecuencia de las palabras.

        Returns:
            Dict[str, int]: Un diccionario que contiene las palabras y sus frecuencias.
        """
        self.words_freq_dict = {}
        self.text = text
        self.text_words = re.findall(r'\b[a-zA-Z]+\b', self.text)
        self.unique_words = list(set(self.text_words))
        for word in self.unique_words:
            self.words_freq_dict[word] = self.text_words.count(word)
        return self.words_freq_dict

    def words_freq_to_df(self, words_freq_dict: dict) -> pd.DataFrame:
        """
        Agrega la frecuencia de las palabras al DataFrame.

        Agrega la frecuencia de las palabras al DataFrame actual, asignando las frecuencias
        proporcionadas en el diccionario `words_freq_dict` a la columna "Terms_Freq" del DataFrame.

        Args:
            - words_freq_dict (Dict[str, int]): Un diccionario que contiene las palabras y sus frecuencias.

        Returns:
            pd.DataFrame: El DataFrame actualizado con la columna "Terms_Freq" actualizada.
        """
        self.df["Terms_Freq"] = words_freq_dict

        return self.df
