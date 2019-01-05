# NeuroSnek

## Cómo correr
El programa se ejecuta desde el archivo ```main.py```. En él también se pueden ajustar los parámetros usados. Cambie la veriable ```GENERATIONS``` de este archivo para especificar cuántas generaciones se cruzarán, el recomendado es 60 pero puede tomar mucho tiempo.
Se recomienda utilizar un ambiente virtual. En él se pueden instalar las dependencias con el comando ```pip install -r requirements.txt```.
Una vez que las dependencias están instaladas se puede ejecutar el programa con el comando ```python main.py```, el cual iterará por la cantidad de generaciones especificadas y finalmente graficará el fitness promedio en función de la generación.

Las dependencias utilizadas son matplotlib, pygame y sus dependencias respectivas.

Probado con python 3.6

Las redes juegan MiniSnake http://projects.pixelatedawesome.com/minisnake/
