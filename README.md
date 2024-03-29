# Pygeons
Creadores:
    - Domingo Fuenzalida
    - Martín Hargous
    - Matías Pedemonte

Copyright (c) 2023, Equipo de Pygeons

Todos los derechos reservados. Este código y cualquier material adjunto están protegidos por las leyes de derechos de autor y otros tratados internacionales. La duplicación, reproducción o distribución no autorizada de este código, en su totalidad o en parte, está estrictamente prohibida.
[Open source]

Requisitos mínimos (720p30):
- Tener instalado python
- Tener instaladas las siguientes librerías:
    - pygame
    - numpy
    - random
    - scipy
    - matplotlib
- Tener todos los archivos guardados en una misma carpeta

Funciones:
- show: Genera el la mazmorra.
- exit: Finaliza el programa.
- window_size [NUMBER] [NUMBER]: Cambia el tamaño de la ventana en la cantidad de píxeles especificados.
- room_size [NUMBER] [NUMBER]: Cambia el tamaño de las habitaciones en la cantidad de píxeles especificados.
- backround_color [NUMBER] [NUMBER] [NUMBER]: Cambia el color de fondo en RGB.
- room_color [NUMBER] [NUMBER] [NUMBER]: Cambia el color de las habitaciones en RGB.
- room_units [NUMBER]: Cambia la cantidad de habitaciones de la mazmorra.
- item_chance [NUMBER]: Cambia la probabilidad de que una habitación contenga un item [0~1].
- boss_chance [NUMBER]: Cambia la probabilidad de que una habitación contenga un jefe [0~1].
- passage_width [NUMBER]: Calmbia el grosor de los pasillos en píxeles.

Instrucciones de uso:
- Correr el archivo Main.py.
- Ocupar alguno de los comandos para cambiar los parámetros de la mazmorra (ya vienen unos valores predeterminados).
- cambiar [NUMBER] por el número deseado para ejecutar los comandos.
- Ocupar el comando show para mostrar la mazmorra.
- Usar show repetidamente hasta alcanzar el diseño buscado.
- exit para finalizar el código.