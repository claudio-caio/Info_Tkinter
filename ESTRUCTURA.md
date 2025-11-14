📁 ESTRUCTURA DEL PROYECTO TAMAGOTCHI
====================================

Tamagochi/
├── main.py                          # Punto de entrada principal
├── app_gui.py                       # Clase principal que coordina todo
├── tamagochi.py                     # Lógica del tamagotchi
├── test_tamagochi.py                # Tests unitarios
│
├── img/                             # Carpeta de imágenes
│   ├── feliz.png
│   ├── neutral.png
│   ├── triste.png
│   ├── comer.png
│   ├── jugar.png
│   ├── dormir.png
│   └── fondo.png
│
├── src/                             # Carpeta principal del código fuente
│   ├── __init__.py
│   │
│   ├── recursos/                    # Gestión de recursos
│   │   ├── __init__.py
│   │   └── gestor_recursos.py       # Carga de imágenes y estilos
│   │
│   ├── ui/                          # Interfaz de usuario
│   │   ├── __init__.py
│   │   └── pantallas.py             # Construcción de pantallas
│   │
│   └── logica/                      # Lógica del juego
│       ├── __init__.py
│       └── gestor_juego.py          # Animaciones, estado y acciones
│
└── README.md                        # Documentación


DESCRIPCIÓN DE CARPETAS
=======================

📂 src/
   Carpeta principal que contiene todo el código organizado

📂 src/recursos/
   - gestor_recursos.py: Carga todas las imágenes (estados, acciones, fondo) y configura estilos

📂 src/ui/
   - pantallas.py: Construye las interfaces (pantalla inicio y pantalla juego)

📂 src/logica/
   - gestor_juego.py: Maneja animaciones, actualizaciones de estado y acciones


VENTAJAS DE ESTA ESTRUCTURA
============================

✅ Separación de responsabilidades
   - Cada módulo tiene un propósito específico
   - Más fácil de entender y mantener

✅ Escalabilidad
   - Fácil agregar nuevas pantallas o funcionalidades
   - Puedes crear nuevos módulos sin afectar otros

✅ Reutilización
   - Los módulos pueden importarse en otros proyectos

✅ Mantenibilidad
   - Código organizado y estructurado
   - Cambios localizados en carpetas específicas


CÓMO IMPORTAR
=============

# Desde main.py o app_gui.py:
from src.recursos.gestor_recursos import Recursos
from src.ui.pantallas import Pantallas
from src.logica.gestor_juego import LogicaJuego

# Los archivos __init__.py hacen que las carpetas sean paquetes Python
