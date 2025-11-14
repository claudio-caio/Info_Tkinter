"""
Módulo de pantallas (interfaz de usuario)
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk


class Pantallas:
    """Gestiona la construcción de las diferentes pantallas de la aplicación"""
    
    def __init__(self, app, root, recursos):
        self.app = app
        self.root = root
        self.recursos = recursos
        self.bg_label = None
    
    def pantalla_inicio(self):
        """Muestra la pantalla inicial para crear un nuevo tamagotchi"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Nombre de tu mascota:", font=("Arial", 12)).pack(pady=10)
        self.app.entry_nombre = tk.Entry(self.root, font=("Arial", 12))
        self.app.entry_nombre.pack(pady=10)
        
        tk.Button(self.root, text="Crear Tamagotchi", font=("Arial", 12),
                  command=self.app.crear_tamagotchi).pack(pady=10)
    
    def pantalla_juego(self):
        """Muestra la pantalla principal del juego"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal con imagen de fondo
        main_frame = tk.Frame(self.root, bg=self.root.cget('bg'))
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Agregar imagen de fondo si existe
        if self.recursos.img_fondo_original:
            self.bg_label = tk.Label(main_frame, bg=self.root.cget('bg'))
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_label.lower()
            
            # Actualizar la imagen de fondo cuando se redimensiona la ventana
            def actualizar_fondo(event=None):
                ancho = self.root.winfo_width()
                alto = self.root.winfo_height()
                if ancho > 1 and alto > 1:
                    img_redimensionada = self.recursos.img_fondo_original.resize((ancho, alto))
                    self.recursos.img_fondo = ImageTk.PhotoImage(img_redimensionada)
                    self.bg_label.config(image=self.recursos.img_fondo)
                    self.bg_label.image = self.recursos.img_fondo
            
            self.root.bind("<Configure>", actualizar_fondo)
            actualizar_fondo()
        
        # Frame superior con nombre
        top_frame = tk.Frame(main_frame, bg=self.root.cget('bg'))
        top_frame.pack(fill=tk.X, pady=10)
        
        # Nombre
        self.app.lbl_nombre = tk.Label(top_frame, text="", font=("Arial", 14, "bold"), 
                                        justify="center", bg=self.root.cget('bg'))
        self.app.lbl_nombre.pack()
        
        # Frame principal con imagen a la izquierda y controles a la derecha
        content_frame = tk.Frame(main_frame, bg=self.root.cget('bg'))
        content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        
        # Configurar columnas para que se distribuyan bien
        content_frame.columnconfigure(0, weight=1, minsize=200)  # Columna izquierda
        content_frame.columnconfigure(1, weight=1, minsize=250)  # Columna derecha
        
        # Frame izquierdo con imagen y edad
        left_frame = tk.Frame(content_frame, bg=self.root.cget('bg'))
        left_frame.grid(row=0, column=0, padx=10, sticky="nsew")
        
        # Imagen
        self.app.label_imagen = tk.Label(left_frame, bg=self.root.cget('bg'))
        self.app.label_imagen.pack(pady=20)
        
        # Edad
        self.app.lbl_edad = tk.Label(left_frame, text="", font=("Arial", 12), 
                                      justify="center", bg=self.root.cget('bg'))
        self.app.lbl_edad.pack(pady=10)
        
        # Frame derecho con barras y botones
        right_frame = tk.Frame(content_frame, bg=self.root.cget('bg'))
        right_frame.grid(row=0, column=1, padx=10, sticky="nsew")
        
        # Barras de progreso
        tk.Label(right_frame, text="Hambre", bg=self.root.cget('bg')).pack(pady=(10, 2))
        self.app.bar_hambre = ttk.Progressbar(right_frame, length=200, maximum=100)
        self.app.bar_hambre.pack(pady=4, fill=tk.X, padx=5)
        
        tk.Label(right_frame, text="Energía", bg=self.root.cget('bg')).pack(pady=(10, 2))
        self.app.bar_energia = ttk.Progressbar(right_frame, length=200, maximum=100)
        self.app.bar_energia.pack(pady=4, fill=tk.X, padx=5)
        
        tk.Label(right_frame, text="Felicidad", bg=self.root.cget('bg')).pack(pady=(10, 2))
        self.app.bar_felicidad = ttk.Progressbar(right_frame, length=200, maximum=100)
        self.app.bar_felicidad.pack(pady=4, fill=tk.X, padx=5)
        
        # Botones
        tk.Button(right_frame, text="🍖 Comer", width=18, 
                  command=self.app.comer).pack(pady=8)
        tk.Button(right_frame, text="🎮 Jugar", width=18, 
                  command=self.app.jugar).pack(pady=4)
        tk.Button(right_frame, text="😴 Dormir", width=18, 
                  command=self.app.dormir).pack(pady=4)
        tk.Button(right_frame, text="Salir", width=18, 
                  command=self.root.quit).pack(pady=8)
