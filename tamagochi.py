from tkinter import messagebox

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 100
        self.vivo = True
        self.edad = 0

    def comer(self):
        if not self.vivo: return
        self.hambre -= 20
        self.energia -= 5
        self.felicidad += 5
        self.validar_stats()

    def dormir(self):
        if not self.vivo: return
        self.energia += 40
        self.hambre += 10
        self.validar_stats()

    def jugar(self):
        if not self.vivo: return
        self.felicidad += 20
        self.energia -= 15
        self.hambre += 10
        self.validar_stats()

    def pasar_tiempo(self):
        if not self.vivo: return
        self.hambre += 5
        self.felicidad -= 3
        self.energia -= 4
        self.edad += 1
        self.validar_stats()

    def validar_stats(self):
        self.hambre = max(0, min(100, self.hambre))
        self.energia = max(0, min(100, self.energia))
        self.felicidad = max(0, min(100, self.felicidad))

        if self.hambre >= 100:
            self.vivo = False
            messagebox.showerror("😢 Tu mascota murió", f"{self.nombre} murió de hambre.")
        elif self.energia <= 0:
            self.vivo = False
            messagebox.showerror("😢 Tu mascota murió", f"{self.nombre} murió de cansancio.")
        elif self.felicidad <= 0:
            self.vivo = False
            messagebox.showerror("😢 Tu mascota murió", f"{self.nombre} murió de tristeza.")
