"""
Módulo de carga de recursos (imágenes y estilos)
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Recursos:
    """Gestiona la carga y almacenamiento de todas las imágenes y estilos"""
    
    def __init__(self, root):
        self.root = root
        self._cargar_imagenes()
        self._configurar_estilos()
    
    def _cargar_imagenes(self):
        """Carga todas las imágenes necesarias para la app"""
        # Imágenes de estado
        self.img_feliz_base = Image.open("img/feliz.png").resize((150, 150))
        self.img_neutral_base = Image.open("img/neutral.png").resize((150, 150))
        self.img_triste_base = Image.open("img/triste.png").resize((150, 150))
        
        self.img_feliz = ImageTk.PhotoImage(self.img_feliz_base)
        self.img_neutral = ImageTk.PhotoImage(self.img_neutral_base)
        self.img_triste = ImageTk.PhotoImage(self.img_triste_base)
        
        # Imágenes de acciones
        self.img_comer_base = Image.open("img/comer.png").resize((150, 150))
        self.img_jugar_base = Image.open("img/jugar.png").resize((150, 150))
        self.img_dormir_base = Image.open("img/dormir.png").resize((150, 150))
        
        self.img_comer = ImageTk.PhotoImage(self.img_comer_base)
        self.img_jugar = ImageTk.PhotoImage(self.img_jugar_base)
        self.img_dormir = ImageTk.PhotoImage(self.img_dormir_base)
        
        # Imagen de fondo
        try:
            self.img_fondo_original = Image.open("img/fondo.png")
            self.img_fondo = None
        except:
            self.img_fondo_original = None
            self.img_fondo = None
    
    def _configurar_estilos(self):
        """Configura los estilos de ttk para las barras de progreso"""
        style = ttk.Style(self.root)
        try:
            style.theme_use("default")
        except:
            pass
        
        style.configure("green.Horizontal.TProgressbar", 
                       troughcolor="#ddd", background="#2ecc71")
        style.configure("yellow.Horizontal.TProgressbar", 
                       troughcolor="#ddd", background="#f1c40f")
        style.configure("red.Horizontal.TProgressbar", 
                       troughcolor="#ddd", background="#e74c3c")
