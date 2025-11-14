"""
Módulo de lógica de juego (animaciones, estado, acciones)
"""
from PIL import ImageTk


class LogicaJuego:
    """Gestiona la lógica y estado del juego"""
    
    def __init__(self, app, root):
        self.app = app
        self.root = root
    
    def animar(self, base_image):
        """Anima la imagen del tamagotchi con un efecto de pulso"""
        frames = 6
        delay = 70
        size = 150
        
        def frame(i):
            if i >= frames:
                if self.app.current_img:
                    self.app.label_imagen.config(image=self.app.current_img)
                    self.app.label_imagen.image = self.app.current_img
                return
            
            scale = 1.15 if i % 2 == 0 else 0.85
            w = int(size * scale)
            h = int(size * scale)
            
            img = base_image.resize((w, h))
            tk_img = ImageTk.PhotoImage(img)
            
            self.app.label_imagen.config(image=tk_img)
            self.app.label_imagen.image = tk_img
            
            self.root.after(delay, lambda: frame(i + 1))
        
        frame(0)
    
    def temporizador(self):
        """Ejecuta el temporizador que hace envejecer al tamagotchi"""
        if self.app.tama and self.app.tama.vivo:
            self.app.tama.pasar_tiempo()
            self.actualizar_estado()
            self.root.after(30000, self.temporizador)
    
    def actualizar_estado(self):
        """Actualiza la pantalla con el estado actual del tamagotchi"""
        if not self.app.tama.vivo:
            self.app.reiniciar_juego()
            return
        
        # Seleccionar imagen según el estado
        if self.app.tama.felicidad > 60 and self.app.tama.hambre < 60:
            base = self.app.recursos.img_feliz_base
            self.app.current_img = self.app.recursos.img_feliz
        elif self.app.tama.felicidad < 30 or self.app.tama.hambre > 70:
            base = self.app.recursos.img_triste_base
            self.app.current_img = self.app.recursos.img_triste
        else:
            base = self.app.recursos.img_neutral_base
            self.app.current_img = self.app.recursos.img_neutral
        
        self.app.label_imagen.config(image=self.app.current_img)
        self.app.label_imagen.image = self.app.current_img
        self.app.base_sprite = base
        
        # Actualizar textos
        self.app.lbl_nombre.config(text=f"🐾 {self.app.tama.nombre}")
        self.app.lbl_edad.config(text=f"📅 Edad: {self.app.tama.edad}")
        
        # Actualizar barras
        saciedad = 100 - self.app.tama.hambre
        self.app.bar_hambre["value"] = saciedad
        self.app.bar_energia["value"] = self.app.tama.energia
        self.app.bar_felicidad["value"] = self.app.tama.felicidad
        
        self._aplicar_color_bar(self.app.bar_hambre, saciedad)
        self._aplicar_color_bar(self.app.bar_energia, self.app.tama.energia)
        self._aplicar_color_bar(self.app.bar_felicidad, self.app.tama.felicidad)
    
    def _aplicar_color_bar(self, barra, valor):
        """Aplica color a una barra según su valor"""
        if valor > 60:
            barra.config(style="green.Horizontal.TProgressbar")
        elif valor > 30:
            barra.config(style="yellow.Horizontal.TProgressbar")
        else:
            barra.config(style="red.Horizontal.TProgressbar")
    
    def comer(self):
        """Realiza la acción de comer"""
        self.app.tama.comer()
        self.actualizar_estado()
        self.app.label_imagen.config(image=self.app.recursos.img_comer)
        self.app.label_imagen.image = self.app.recursos.img_comer
        self.animar(self.app.recursos.img_comer_base)
    
    def jugar(self):
        """Realiza la acción de jugar"""
        self.app.tama.jugar()
        self.actualizar_estado()
        self.app.label_imagen.config(image=self.app.recursos.img_jugar)
        self.app.label_imagen.image = self.app.recursos.img_jugar
        self.animar(self.app.recursos.img_jugar_base)
    
    def dormir(self):
        """Realiza la acción de dormir"""
        self.app.tama.dormir()
        self.actualizar_estado()
        self.app.label_imagen.config(image=self.app.recursos.img_dormir)
        self.app.label_imagen.image = self.app.recursos.img_dormir
        self.animar(self.app.recursos.img_dormir_base)
