import unittest
import pandas as pd
import os
from word_cloud import Word_Cloud

class TestWordCloud(unittest.TestCase):

    def setUp(self):
        # Generar archivo CSV de prueba
        self.test_file_path = "test_data.csv"
        data = {
            "sentiment": [0, 4, 4, 0],
            "Terms_Freq": ["{}", "{'a': 2}", "{}", "{'b': 1}"],
            "text": ["Hello", " ", "World", " "]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_file_path, index=False)

    def test_empty_terms_freq(self):
        # Utilizamos el archivo CSV de prueba
        word_cloud = Word_Cloud(self.test_file_path)
        # Cargamos el archivo CSV en el DataFrame
        word_cloud.df = pd.read_csv(self.test_file_path)

        expected_result = 2

        empty_terms_freq_column = word_cloud.empty_terms_freq()

        self.assertEqual(empty_terms_freq_column, expected_result)


    def test_empty_text(self):
        word_cloud = Word_Cloud(self.test_file_path)
        word_cloud.df = pd.read_csv(self.test_file_path)

        expected_result = 2

        empty_text_column = word_cloud.empty_text()

        self.assertEqual(empty_text_column, expected_result)

    def test_words_clust_by_sentiment(self):
        word_cloud = Word_Cloud(self.test_file_path)
        word_cloud.df = pd.read_csv(self.test_file_path)

        expected_result4 = {"a": 2}
        expected_result0 = {"b": 1}

        all_words_sentiment_0 = word_cloud.words_clust_by_sentiment(0)
        all_words_sentiment_4 = word_cloud.words_clust_by_sentiment(4)

        self.assertDictEqual(all_words_sentiment_0, expected_result0)
        self.assertDictEqual(all_words_sentiment_4, expected_result4)


    def tearDown(self):
        # Eliminar archivo CSV de prueba
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

if __name__ == "__main__":
    unittest.main()