import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Word_Cloud:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(path)

    # ¿Cuántos clusters tenemos en nuestro dataset?
    def count_clusters(self) -> int:
        """
        Cuenta el número de clusters (sentimientos) únicos presentes en la columna "sentiment" del DataFrame.

        Returns:
            int: El número de clusters (sentimientos) presentes en el DataFrame.

        """
        return self.df.sentiment.nunique()

    # ¿Tenemos elementos vacíos en las columnas text?
    def empty_text(self) -> int:
        """

        La función cuenta el número de filas en el DataFrame en las cuales el campo "text" está vacío.

        Returns:
            int: El número de filas con el campo "text" vacío en el DataFrame.

        """
        self.empty_text_column = (self.df["text"] == " ").sum()
        return self.empty_text_column

    def empty_terms_freq(self) -> int:
        """
        Calcula el número de filas con el campo "Terms_Freq" vacío en el DataFrame.

        La función cuenta el número de filas en el DataFrame en las cuales el campo "Terms_Freq" está vacío,
        es decir, con el valor "{}".

        Returns:
            int: El número de filas con el campo "Terms_Freq" vacío en el DataFrame.

        """
        self.empty_terms_freq_column = (self.df.Terms_Freq == "{}").sum()
        return self.empty_terms_freq_column

    def pct_empty_terms(self) -> float:
        """
        Calcula el porcentaje de filas con el campo "Terms_Freq" vacío en relación al total de comentarios.

        La función calcula el porcentaje de filas en el DataFrame que tienen el campo "Terms_Freq" vacío,
        es decir, con el valor "{}", en relación al total de comentarios en el DataFrame.

        Returns:
            float: El porcentaje de filas con el campo "Terms_Freq" vacío en relación al total de comentarios.

        """
        self.total_comments = self.df.Terms_Freq.count()
        self.pct_empty_comments = (self.empty_terms_freq_column / self.total_comments) * 100

        return self.pct_empty_comments

    # https://www.programiz.com/python-programming/methods/dictionary/get
    # https://realpython.com/python-eval-function/
    # Usamos eval() porque el diccionario es interpretado inicialmente como string, de este modo se convierte en dict.
    def words_clust_by_sentiment(self, sentiment: int) -> dict:
        """
        Obtiene las palabras y su frecuencia para un sentimiento específico.

        La función recibe un parámetro 'sentiment' que indica el valor del sentimiento para el cual se desean obtener
        las palabras y su frecuencia. La función busca en el DataFrame las filas que corresponden al sentimiento
        especificado y extrae la columna 'Terms_Freq'. Luego, itera sobre cada subdiccionario de 'Terms_Freq',
        convirtiéndolo en un diccionario mediante la función eval(). Posteriormente, agrega las palabras y su frecuencia
        al diccionario 'all_words_sentiment', acumulando la frecuencia para las palabras repetidas.

        Args:
            sentiment (int): El valor del sentimiento para el cual se desean obtener las palabras y su frecuencia.

        Returns:
            dict: Un diccionario que contiene las palabras y su frecuencia para el sentimiento especificado.

        """
        self.all_words_sentiment = {}
        self.sentiment_clust = self.df[self.df["sentiment"] == sentiment].Terms_Freq.tolist()
        for subdict in self.sentiment_clust:
            subdict = eval(subdict)
            for word, freq in subdict.items():
                self.all_words_sentiment[word] = self.all_words_sentiment.get(word, 0) + int(freq)

        return self.all_words_sentiment

    def create_word_cloud(self, words_clust: dict) -> WordCloud:
        """
        Crea una representación gráfica de nube de palabras a partir de un diccionario de palabras y su frecuencia.

        La función recibe un parámetro 'words_clust' que es un diccionario que contiene las palabras y su frecuencia.
        Utiliza la biblioteca WordCloud para generar una representación gráfica de nube de palabras a partir de los
        datos proporcionados. Se configuran parámetros como el color de fondo, el tamaño del lienzo y la
        semilla aleatoria. Finalmente, se devuelve el objeto WordCloud generado.

        Args:
            words_clust (dict): Un diccionario que contiene las palabras y su frecuencia.

        Returns:
            WordCloud: Un objeto WordCloud que representa gráficamente la nube de palabras.

        """

        self.words_clust = words_clust
        self.wordcloud_clust = WordCloud(background_color='white', width=3000, height=2000,
                                random_state=1).generate_from_frequencies(self.words_clust)

        return self.wordcloud_clust

    def top_50_words(self, words_clust: dict) -> list:
        """
        Obtiene las 50 palabras más frecuentes a partir de un diccionario de palabras y su frecuencia.

        La función recibe un parámetro 'words_clust' que es un diccionario que contiene las palabras y su frecuencia.
        Utiliza la función 'sorted' para ordenar el diccionario en función de la frecuencia de las palabras, de forma
        descendente. Luego se seleccionan las 50 primeras palabras ordenadas. El resultado se devuelve como una lista
        de tuplas, donde cada tupla contiene una palabra y su frecuencia.

        Args:
            words_clust (dict): Un diccionario que contiene las palabras y su frecuencia.

        Returns:
            list: Una lista que contiene las 50 palabras más frecuentes y su frecuencia,
            ordenadas de forma descendente.

        """
        self.words_clust = words_clust
        self.top_words = sorted(self.words_clust.items(), key=lambda x: x[1], reverse=True)[:50]

        return self.top_words










