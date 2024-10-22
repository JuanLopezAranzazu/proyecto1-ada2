## Proyecto 1 ADA II

### Integrantes:

- Victor Manuel Álzate Morales - 202313022
- Juan Esteban López Aránzazu - 202313026
- Daniel Meléndez Ramirez - 202313024
- Diego Alejandro Tolosa Sanchez - 202313023

### Descripción:

Resolver los problemas de la terminal inteligente y la subasta pública usando los algoritmos de fuerza bruta, programación dinámica y programación voraz

### Archivos de entrada de datos

La carpeta [data_inputs](./app/data_inputs/) contiene archivos `.txt` que son utilizados como entradas de datos para el programa

### Instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución del programa

Para correr el programa puedes ejecutar el siguiente comando:
```bash
python ./app/main.py
```

### Correr las pruebas

Para correr las pruebas puedes ejecutar los siguientes comandos:

Para las pruebas de la terminal inteligente
```bash
python -m unittest ./app/tests/test_terminal.py
```

Para las pruebas de la subasta pública
```bash
python -m unittest ./app/tests/test_auction.py
```

### Mostrar las gráficas de tiempo de ejecución

Para mostrar las gráficas de la terminal inteligente
```bash
python ./app/graphics/terminal_graphics.py
```

Para mostrar las gráficas de la subasta pública
```bash
python ./app/graphics/auction_graphics.py
```