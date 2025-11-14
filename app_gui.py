"""
Módulo principal de la aplicación GUI del Tamagotchi
"""
import tkinter as tk
from tkinter import messagebox
from tamagochi import Tamagotchi
from src.recursos.gestor_recursos import Recursos
from src.ui.pantallas import Pantallas
from src.logica.gestor_juego import LogicaJuego


class TamagotchiApp:
    """Clase principal que coordina toda la aplicación"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🐣 Tamagotchi")
        self.root.geometry("480x580")
        
        # Inicializar atributos
        self.tama = None
        self.current_img = None
        self.base_sprite = None
        
        # Cargar recursos
        self.recursos = Recursos(self.root)
        
        # Inicializar módulos
        self.pantallas = Pantallas(self, self.root, self.recursos)
        self.logica = LogicaJuego(self, self.root)
        
        # Mostrar pantalla inicial
        self.pantallas.pantalla_inicio()
    
    def crear_tamagotchi(self):
        """Crea un nuevo tamagotchi y inicia el juego"""
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Poné un nombre para la mascota.")
            return
        
        self.tama = Tamagotchi(nombre)
        self.pantallas.pantalla_juego()
        self.logica.actualizar_estado()
        self.logica.temporizador()
    
    def comer(self):
        """Llamada a la acción de comer"""
        self.logica.comer()
    
    def jugar(self):
        """Llamada a la acción de jugar"""
        self.logica.jugar()
    
    def dormir(self):
        """Llamada a la acción de dormir"""
        self.logica.dormir()
    
    def reiniciar_juego(self):
        """Reinicia el juego después de que el tamagotchi muere"""
        opcion = messagebox.askyesno("Reiniciar", "Tu mascota murió 😢\n¿Querés reiniciar?")
        if opcion:
            self.pantallas.pantalla_inicio()
        else:
            self.root.quit()


