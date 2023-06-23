import unittest
import os
from zipfile import ZipFile
from control import ControlCsv

class TestControlCsv(unittest.TestCase):

    def setUp(self):
        self.zip_file = "twitter.zip"
        self.output_dir = "data"

    def test_create_test_zip(self):
        # Creamos un archivo ZIP de prueba
        with ZipFile(self.zip_file, "w") as zipObject:
            zipObject.writestr("file1.txt", "Contenido del archivo 1")
            zipObject.writestr("file2.txt", "Contenido del archivo 2")
            zipObject.writestr("file3.txt", "Contenido del archivo 3")

    def test_unzip(self):
        control_csv = ControlCsv(self.zip_file)
        control_csv.unzip()

        # Verificamos que los archivos se descomprimieron correctamente
        self.assertTrue(os.path.isdir(self.output_dir))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "file2.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "file3.txt")))

    def test_clean_comments(self):
        control_csv = ControlCsv("ruta/de/prueba")  # Crea una instancia de ControlCsv con una ruta de archivo ficticia
        text1 = "Hello, this is a test comment with a URL: http://example.com"
        expected_result1 = "hello this is a test comment with a url "
        text2 = "Hola ME Llamo Oscar PEDREÑO"
        expected_result2 = "hola me llamo oscar pedreo"

        cleaned_text1 = control_csv.clean_comments(text1)
        cleaned_text2 = control_csv.clean_comments(text2)

        self.assertEqual(cleaned_text1, expected_result1)
        self.assertEqual(cleaned_text2, expected_result2)

    def test_split_words(self):
        control_csv = ControlCsv("ruta/de/prueba")
        text = "This is a test sentence."
        expected_result = ["This", "is", "a", "test", "sentence"]

        split_words = control_csv.split_words(text)

        self.assertEqual(split_words, expected_result)

    def test_words_freq(self):
        control_csv = ControlCsv("ruta/de/prueba")
        text = "This is a test sentence. This sentence is a test hello Oscar."
        expected_result = {"This": 2, "is": 2, "a": 2, "test": 2, "sentence": 2, "hello":1, "Oscar":1}

        words_freq_dict = control_csv.words_freq(text)

        self.assertEqual(words_freq_dict, expected_result)
    def tearDown(self):
        # Una vez comprobado que funciona, eliminamos los archivos y directorios creados durante las pruebas
        if os.path.isdir(self.output_dir):
            for file_name in os.listdir(self.output_dir):
                file_path = os.path.join(self.output_dir, file_name)
                os.remove(file_path)
            os.rmdir(self.output_dir)

            # Eliminamos también el Twitter.zip
            if os.path.exists(self.zip_file):
                os.remove(self.zip_file)

if __name__ == "__main__":
    unittest.main()