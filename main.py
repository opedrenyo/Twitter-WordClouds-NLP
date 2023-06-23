from matplotlib import pyplot as plt
from wordcloud import WordCloud
from control import ControlCsv
from word_cloud import Word_Cloud

# Added "thats" and "shoulda" to the list.
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
             'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
             'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
             'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
             'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
             'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
             'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
             'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
             'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
             'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

reviewer = ControlCsv("../data/twitter_reduced.zip")

# 1.1 Descomprimid el fichero twitter.zip y guardad su contenido en la carpeta data del proyecto.
print("\n----------------------------------------------------------\n")
reviewer.unzip()
print("\n----------------------------------------------------------\n")
# 1.2 Leed el fichero twitter.csv y cargad el dataset como una lista de diccionarios.
# Cada fila del fichero original corresponderá con un diccionario siguiendo la estructura de este ejemplo:
reviewer.create_listdicts()
print("\n----------------------------------------------------------\n")
# Mostrad por pantalla los 5 primeros registros del dataset mediante print.
print(reviewer.comments[:6])
print("\n----------------------------------------------------------\n")
# Realizad un preprocesado haciendo uso de expresiones regulares que elimine las URLs,
# los caracteres especiales no ASCII y los símbolos y que convierta el texto a minúsculas.
# Sustituid los textos originales por los modificados en el dataset del apartado anterior.
for comment in reviewer.comments:
    comment["text"] = reviewer.clean_comments(comment["text"])
print(reviewer.comments[:6])
print("\n----------------------------------------------------------\n")
# Eliminad las stopwords de los textos de los tuits y mostrad por pantalla las 5 últimas filas.
for comment in reviewer.comments:
    comment["text"] = reviewer.drop_stopwords(comment["text"], stopwords)

print(reviewer.comments[:6])
print("\n----------------------------------------------------------\n")
# Obtened las frecuencias de términos de cada tuit y almacenadlas en una lista de diccionarios en la que cada
# diccionario indique las palabras y su frecuencia de aparición en el tuit.  Ordenad alfabéticamente el vocabulario y mostrad por pantalla
# las 10 primeras palabras.

comment_words_list = []
words_freq_list = []

for comment in reviewer.comments:
    words_freq_list.append(reviewer.words_freq(comment["text"]))

# Mostrad por pantalla los 5 primeros elementos de la lista de diccionarios obtenida.
i = 1
for comment_dict in words_freq_list:
    print(f"Comentario {i}")
    print(f"{comment_dict}\n")
    i += 1
    if i > 5:
        break
print("\n----------------------------------------------------------\n")
# Obtened también un vocabulario con todas las palabras únicas del dataset y guardadlas en una lista.
for comment in reviewer.comments:
    comment_words_list.append(reviewer.split_words(comment["text"]))
# comment_words_list es una lista de las palabras de cada comment. Creamos una única lista.
all_words = [word for sublist in comment_words_list for word in sublist]

# Ordenad alfabéticamente el vocabulario y mostrad por pantalla las 10 primeras palabras.
BOW = sorted(set(all_words))
print(BOW[:11])
print("\n----------------------------------------------------------\n")
# Completad el dataset original añadiendo a cada registro del mismo una nueva variable con su diccionario de
# frecuencias de términos asociado. Mostrad el elemento 20 del dataset.
comment_df = reviewer.words_freq_to_df(words_freq_list)

# Mostrad el elemento 20 del dataset.
print(comment_df.iloc[20])
print("\n----------------------------------------------------------\n")
# Guardad el dataset procesado en formato csv. El nombre del fichero será twitter_processed.csv
# y se ubicará en la carpeta data del proyecto.

comment_df.to_csv("data/twitter_processed.csv")

# ¿Cuántos clusters tenemos en nuestro dataset?
wordcloud = Word_Cloud("data/twitter_processed.csv")
print(f"El número de clusters que tenemos en nuestro dataset es de {wordcloud.count_clusters()}")

# ¿Tenemos elementos vacíos en las columnas text?
# No en la columna text, pero tenemos vacíos en la columna Terms_freq

empty_text = wordcloud.empty_text()
print(f"El número de filas vacías de la columna texto es de {empty_text}")
empty_terms_freq = wordcloud.empty_terms_freq()
print(f"El número de filas vacías de la columna Terms_Freq es de {empty_terms_freq}")

# ¿Si es así, cuál es el porcentaje?
pct_empty_comments = wordcloud.pct_empty_terms()
print(f"El porcentaje de filas con filas vacías en la columna Terms_Freq es de {pct_empty_comments}")

# En caso de tener elementos nulos en la columna text, se deben eliminar antes de generar el word cloud.
wordcloud.df.drop(wordcloud.df[wordcloud.df["Terms_Freq"] == "{}"].index, inplace=True)
empty_terms_freq = wordcloud.empty_terms_freq()
print(f"El número de filas vacías de la columna Terms_Freq es de {empty_terms_freq}")

# Separamos palabras por clúster
all_words_0 = wordcloud.words_clust_by_sentiment(0)
all_words_4 = wordcloud.words_clust_by_sentiment(4)


# Generar un word cloud para cada cluster.
# Una vez generado el world cloud en el ejercicio anterior os pedimos que hagáis una validación de los
# resultados obtenidos en el apartado anterior. Para ello tenéis que generar un histograma con los valores
# que habéis obtenido en el ejercicio 3.
# https://stackoverflow.com/questions/43043437/wordcloud-python-with-generate-from-frequencies
wordcloud_0 = wordcloud.create_word_cloud(all_words_0)
wordcloud_4 = wordcloud.create_word_cloud(all_words_4)

# En vez de mostrar todas las palabras en los histogramas, vamos a mostrar las 50 más utilizadas por cluster.
top_words_0 = wordcloud.top_50_words(all_words_0)
top_words_4 = wordcloud.top_50_words(all_words_4)

# Separamos entre palabras y frecuencias para mostrarlo en el histograma.
words_0 = [word for word, freq in top_words_0]
freq_0 = [freq for word, freq in top_words_0]
words_4 = [word for word, freq in top_words_4]
freq_4 = [freq for word, freq in top_words_4]

# https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
# sudo apt-get install python3-tk
# Crear una figura con 2 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Word cloud para el sentimiento 0
axs[0, 0].imshow(wordcloud_0, interpolation='bilinear')
axs[0, 0].set_title('Word Cloud - Sentimiento: 0')
axs[0, 0].axis('off')
# Word cloud para el sentimiento 4
axs[0, 1].imshow(wordcloud_4, interpolation='bilinear')
axs[0, 1].set_title('Word Cloud - Sentimiento: 4')
axs[0, 1].axis('off')

# Histograma para el sentimiento 0
axs[1, 0].bar(words_0, freq_0)
axs[1, 0].set_title('Histograma - Sentimiento: 0')
axs[1, 0].set_xlabel('Palabras')
axs[1, 0].set_ylabel('Frecuencia')
axs[1, 0].tick_params(axis='x', rotation=90)

# Histograma para el sentimiento 4
axs[1, 1].bar(words_4, freq_4)
axs[1, 1].set_title('Histograma - Sentimiento: 4')
axs[1, 1].set_xlabel('Palabras')
axs[1, 1].set_ylabel('Frecuencia')
axs[1, 1].tick_params(axis='x', rotation=90)

# Ajustar el espaciado entre los subplots
plt.tight_layout()

# Mostrar la figura con los subplots
plt.show()
print("\n----------------------------------------------------------\n")
# a. ¿Cuáles son las palabras más utilizadas en las críticas positivas?
print("Como podemos observar las palabras más utilizadas en las críticas positivas son I'm, good, love, get, thanks...")
# b. ¿Cuáles son las palabras más utilizadas en las críticas negativas?
print("Como podemos observar las palabras más utilizadas en las críticas negativas son I'm, I, work, get, don't...")
# c. ¿Hay palabras que aparezcan tanto en las críticas positivas como en las negativas?
print("Si, palabras generalistas como I'm, get, go aparecen en ambas, aunque en proporciones diferentes.")
# d. A partir de la word cloud, ¿qué se puede deducir sobre el sentimiento general de cada grupo?
print("Podemos deducir que cuando la crítica es negativa nos centramos mucho más en el 'yo', además hay muchas más "
      "referencias a la escuela o el trabajo, a palabras como 'no puedo' y referencias a enfermedades.\nEn cuanto a "
      "los mensajes positivos vemos una menor referencia al 'yo', hablamos de amor, tiempo , día. \nEn general podemos "
      "ver una diferencia de las palabras utilizadas que resulta muy interesante.")