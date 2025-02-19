# Snake IA 

Descripción:
Este es el tipico juego de Snake donde tienes que recolectar las manzanas para conseguir puntos.
Si un jugador choca contra un muro o contra el cuerpo de cualquier jugador (incluido el suyo) se acaba el juego.
El juego de momento se ejecuta en una interfaz de terminal, pero es fácilmente migrable a una versión
de interfaz gráfica más avanzada.

Implementaciones:
- 1 jugador humano máximo. Fácil posible implementación de más jugadores.
- Número ilimitado de jugadores IA.

Limitaciones:
- La IA ha sido programada manualmente por lo que es muy simple. No es capaz de visualizar a futuro la situación
  del juego, por lo que al crecer mucho la serpiente controlada por IA, esta tiende a morir al encerrarse sin querer
  sobre si misma.
  Además, cuando no hay frutas en el tablero, la IA da vueltas sobre si misma, por lo que si es suficientemente larga, 
  puede morir por este motivo.

Errores no solucionados:
- Si se mantiene demasiado tiempo una tecla en vez de pulsarse momentaneamente, se acelera el progreso temporal del juego.
  Este error no limita la jugabilidad en la mayoría de partidas. Se pretende arreglar en un futuro pero no es prioridad.
- Cuando muere un jugador y el juego acaba, algunos de los demás jugadores avanzan una casilla más aunque el juego ya haya acabado.
  No afecta a la jugabilidad ya que se sigue contando como perdedor el primer jugador que haya muerto. Se pretende arreglar en caso
  de que afecte al entrenamineto de la IA.

Respecto al codigo:
- Actualmente no se han añadido apenas comentarios explicativos. Se irán añadiendo a medida que avance el proyecto.
- Se ha intentado estructurar al máximo el proyecto en clases siguiendo el modelo de POO. Aun así, hay una serie de 
  variables globales que se han añadido para facilitar ciertas funcionalidades (relacionadas con el uso de librerías: teclado, pantalla, etc.).

Dependencias:
Se han usado las siguientes librerías:
- curses: Captura de las teclas y representación del juego en el interfaz de terminal.
- random: Generación de numeros aleatorios (inicialización de jugadores, decisiones de la IA simple, etc.)

Entorno de desarrollo:
- El programa ha sido desarrollado en la versión 3.12.8 de Python.
- El desarrollo y testeo se ha llevado a cabo en Linux.
  No se ha comprovado si es posible ejecutar el programa en otros sistemas.

