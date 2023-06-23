from setuptools import setup

# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='Twitter Comments Analysis',
    version='1.0',
    author='Oscar Pedreño Fernandez',
    description='Preprocesamiento y análisis de los comentarios de Twitter categorizados por sentimiento y creación de '
                'Word Cloud.',
    packages=['Twitter_comments_Analysis'],
    install_requires=[
        'matplotlib==3.7.1',
        'pandas==2.0.2',
        'wordcloud==1.9.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
    ],
)