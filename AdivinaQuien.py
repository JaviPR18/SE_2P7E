import json

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import simpledialog, messagebox



class MiVentana:
    def __init__(self, master, VenIm):
        self.VenIm = VenIm
        self.master = master
        self.personajes = self.cargar_personajes()
        self.respuestas = []
        self.personaje_adivinado = None
        self.contador = 0

        # Botones Sí y No
        self.boton_si = tk.Button(self.master, text="Sí", command=lambda: self.registrar_respuesta(True))
        self.boton_si.pack(side=tk.LEFT, padx=10)

        self.boton_no = tk.Button(self.master, text="No", command=lambda: self.registrar_respuesta(False))
        self.boton_no.pack(side=tk.LEFT, padx=10)

        # Etiqueta de pregunta
        self.lbl_preg = tk.Label(self.master, text="Selecciona una característica:")
        self.lbl_preg.pack()

        self.caracteristicas = list(self.personajes["Spiderman"].keys())
        self.caracteristica_actual = self.caracteristicas[0]

        self.actualizar_pregunta()

    def cargar_personajes(self):
        try:
            with open("Marvel.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "Spiderman": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "True",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "False",
                    "Es_un_x-men": "False",
                    "Es_un_vengador": "True",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },
                "Ironman": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "True",
                    "Tiene_factor_curativo": "False",
                    "Es_un_x-men": "False",
                    "Es_un_vengador": "True",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },                
                "Deadpool": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "False",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "True",
                    "Es_un_x-men": "True",
                    "Es_un_vengador": "False",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },
                "Wolverine": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "True",
                    "Es_un_x-men": "True",
                    "Es_un_vengador": "False",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"True",
                    "Tiene_un_escudo":"False"
                },
                "Hulk": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "True",
                    "Es_un_x-men": "False",
                    "Es_un_vengador": "True",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"True",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },
                "Thor": {
                    "Es_hombre":"True", 
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "False",
                    "Es_un_x-men": "False",
                    "Es_un_vengador": "True",
                    "Es_un_hechicero": "False",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },
                "Capitan_America": {
                     "Es_hombre":"True",
                     "Es_un_heroe": "True",
                     "Lanza_Telarañas": "False",
                     "Tiene_armadura": "False",
                     "Tiene_factor_curativo": "False",
                     "Es_un_x-men": "False",
                     "Es_un_vengador": "True",
                     "Es_un_hechicero": "False",
                     "Se_covierte_en_un_monstruo":"False",
                     "Tiene_garras":"False",
                     "Tiene_un_escudo":"True"
                },
                "Dr_Strange": {
                    "Es_hombre":"True",
                    "Es_un_heroe": "True",
                    "Lanza_Telarañas": "False",
                    "Tiene_armadura": "False",
                    "Tiene_factor_curativo": "False",
                    "Es_un_x-men": "False",
                    "Es_un_vengador": "True",
                    "Es_un_hechicero": "True",
                    "Se_covierte_en_un_monstruo":"False",
                    "Tiene_garras":"False",
                    "Tiene_un_escudo":"False"
                },
                 "Black_Panther": {
                     "Es_hombre":"True",
                     "Es_un_heroe": "True",
                     "Lanza_Telarañas": "False",
                     "Tiene_armadura": "False",
                     "Tiene_factor_curativo": "False",
                     "Es_un_x-men": "False",
                     "Es_un_vengador": "True",
                     "Es_un_hechicero": "False",
                     "Se_covierte_en_un_monstruo":"False",
                     "Tiene_garras":"True",
                     "Tiene_un_escudo":"False"
                 }, 
                 "Scarlet_Witch": {
                      "Es_hombre":"False", 
                      "Es_un_heroe": "True",
                      "Lanza_Telarañas": "False",
                      "Tiene_armadura": "False",
                      "Tiene_factor_curativo": "False",
                      "Es_un_x-men": "True",
                      "Es_un_vengador": "True",
                      "Es_un_hechicero": "True",
                      "Se_covierte_en_un_monstruo":"False",
                      "Tiene_garras":"False",
                      "Tiene_un_escudo":"False"
                  },
                  "Loki": {
                       "Es_hombre":"True",
                       "Es_un_heroe": "False",
                       "Lanza_Telarañas": "False",
                       "Tiene_armadura": "False",
                       "Tiene_factor_curativo": "False",
                       "Es_un_x-men": "False",
                       "Es_un_vengador": "False",
                       "Es_un_hechicero": "True",
                       "Se_covierte_en_un_monstruo":"True",
                       "Tiene_garras":"False",
                       "Tiene_un_escudo":"False"
                   },
                  "Venom": {
                        "Es_hombre":"True",
                        "Es_un_heroe": "False",
                        "Lanza_Telarañas": "True",
                        "Tiene_armadura": "False",
                        "Tiene_factor_curativo": "False",
                        "Es_un_x-men": "False",
                        "Es_un_vengador": "False",
                        "Es_un_hechicero": "False",
                        "Se_covierte_en_un_monstruo":"True",
                        "Tiene_garras":"False",
                        "Tiene_un_escudo":"False"
                    },
                     "Storm": {
                          "Es_hombre":"False",
                          "Es_un_heroe": "True",
                          "Lanza_Telarañas": "False",
                          "Tiene_armadura": "False",
                          "Tiene_factor_curativo": "False",
                          "Es_un_x-men": "True",
                          "Es_un_vengador": "False",
                          "Es_un_hechicero": "False",
                          "Se_covierte_en_un_monstruo":"False",
                          "Tiene_garras":"False",
                          "Tiene_un_escudo":"False"
                      },
                       "Abomination": {
                            "Es_hombre":"True", 
                            "Es_un_heroe": "False",
                            "Lanza_Telarañas": "False",
                            "Tiene_armadura": "False",
                            "Tiene_factor_curativo": "True",
                            "Es_un_x-men": "False",
                            "Es_un_vengador": "False",
                            "Es_un_hechicero": "False",
                            "Se_covierte_en_un_monstruo":"True",
                            "Tiene_garras":"False",
                            "Tiene_un_escudo":"False"
                        },
                         "Baron_Mordo": {
                              "Es_hombre":"True",
                              "Es_un_heroe": "False",
                              "Lanza_Telarañas": "False",
                              "Tiene_armadura": "False",
                              "Tiene_factor_curativo": "False",
                              "Es_un_x-men": "False",
                              "Es_un_vengador": "False",
                              "Es_un_hechicero": "True",
                              "Se_covierte_en_un_monstruo":"False",
                              "Tiene_garras":"False",
                              "Tiene_un_escudo":"False"
            }
}
    def guardar_personajes(self):
        with open("Marvel.json", "w") as file:
            json.dump(self.personajes, file, indent=4)

    def registrar_respuesta(self, respuesta):
        caracteristica = self.caracteristica_actual
        self.respuestas.append((caracteristica, respuesta))

        self.contador += 1

        if self.contador == len(self.caracteristicas):
            self.adivinar_personaje()
        else:
            self.caracteristica_actual = self.caracteristicas[self.contador]
            self.actualizar_pregunta()

    def adivinar_personaje(self):
        for personaje, caracteristicas in self.personajes.items():
            coincide = all(caracteristicas[caracteristica] == str(respuesta) for caracteristica, respuesta in self.respuestas)
            if coincide:
                self.personaje_adivinado = personaje
                break

        if self.personaje_adivinado is None:
            print("Ningún personaje coincide con las características.")
            nuevo_personaje = self.agregar_nuevo_personaje()
            if nuevo_personaje:
                self.personajes[nuevo_personaje] = {caracteristica: str(respuesta) for caracteristica, respuesta in self.respuestas}
                self.guardar_personajes()
                print(f"Se ha agregado el personaje {nuevo_personaje} al diccionario.")
        else:
            print(f"El personaje que estás pensando es {self.personaje_adivinado}")

        respuesta = messagebox.askyesno("Jugar de nuevo", f"Tu personaje es: {self.personaje_adivinado}\n¿Deseas jugar de nuevo?")
        if respuesta:
            self.reiniciar_juego()
        else:
            self.VenIm.destroy()
            self.master.destroy()

    def agregar_nuevo_personaje(self):
        nuevo_personaje = simpledialog.askstring("Nuevo Personaje", "Ningún personaje coincide. Ingresa un nuevo nombre:")
        return nuevo_personaje

    def reiniciar_juego(self):
        self.respuestas = []
        self.personaje_adivinado = None
        self.contador = 0
        self.caracteristicas = list(self.personajes["Spiderman"].keys())
        self.caracteristica_actual = self.caracteristicas[0]
        self.actualizar_pregunta()

    def actualizar_pregunta(self):
        caracteristica_formateada = self.caracteristica_actual.replace('_', ' ')
        self.lbl_preg.config(text=f"¿{caracteristica_formateada}?", font=("Arial Bold", 20), fg="Blue")
        

def iniciar_juego(venIm):
    ventana = tk.Tk()
    ventana.title("Adivina el Personaje")
    ventana.geometry("500x100+300+400")
    mi_ventana = MiVentana(ventana,venIm)
    ventana.mainloop()


    
    





class Ventana1_MostrarPers:
    def __init__(self, master):
        self.master = master

        #Etiquetas
        
        self.lbl_title = tk.Label(master, text="¡Bienvenido al juego Adivina Quién!")
        self.lbl_title.config(font=("Arial Bold", 20))
        self.lbl_title.config(fg="green")
        self.lbl_title.place(x=300,y=10)
        
        self.lbl_title2 = tk.Label(master, text="Piensa en un personaje")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=400,y=60)
        
        
        #Imagenes
        
        img_Spiderman = Image.open("Spiderman.png")  
        img_Spiderman_tk = ImageTk.PhotoImage(img_Spiderman)
        self.lbl_img_Spiderman = tk.Label(master, image=img_Spiderman_tk)
        self.lbl_img_Spiderman.image = img_Spiderman_tk
        self.lbl_img_Spiderman.pack()
        self.lbl_img_Spiderman.place(x=100,y=100)
        
        img_Ironman = Image.open("Ironman.png")  
        img_Ironman_tk = ImageTk.PhotoImage(img_Ironman)
        self.lbl_img_Ironman = tk.Label(master, image=img_Ironman_tk)
        self.lbl_img_Ironman.image = img_Ironman_tk
        self.lbl_img_Ironman.pack()
        self.lbl_img_Ironman.place(x=250,y=100)
                    
        img_Deadpool = Image.open("Deadpool.png")  
        img_Deadpool_tk = ImageTk.PhotoImage(img_Deadpool)
        self.lbl_img_Deadpool = tk.Label(master, image=img_Deadpool_tk)
        self.lbl_img_Deadpool.image = img_Deadpool_tk
        self.lbl_img_Deadpool.pack()
        self.lbl_img_Deadpool.place(x=400,y=100)
        
        img_Wolverine = Image.open("Wolverine.png")  
        img_Wolverine_tk = ImageTk.PhotoImage(img_Wolverine)
        self.lbl_img_Wolverine = tk.Label(master, image=img_Wolverine_tk)
        self.lbl_img_Wolverine.image = img_Wolverine_tk
        self.lbl_img_Wolverine.pack()
        self.lbl_img_Wolverine.place(x=550,y=100)
        
        img_Hulk = Image.open("Hulk.png")  
        img_Hulk_tk = ImageTk.PhotoImage(img_Hulk)
        self.lbl_img_Hulk = tk.Label(master, image=img_Hulk_tk)
        self.lbl_img_Hulk.image = img_Hulk_tk
        self.lbl_img_Hulk.pack()
        self.lbl_img_Hulk.place(x=700,y=100)
        
        img_Thor = Image.open("Thor.png")  
        img_Thor_tk = ImageTk.PhotoImage(img_Thor)
        self.lbl_img_Thor = tk.Label(master, image=img_Thor_tk)
        self.lbl_img_Thor.image = img_Thor_tk
        self.lbl_img_Thor.pack()
        self.lbl_img_Thor.place(x=100,y=250)
        
        img_Capitan_America = Image.open("Capitan_America.png")  
        img_Capitan_America_tk = ImageTk.PhotoImage(img_Capitan_America)
        self.lbl_img_Capitan_America = tk.Label(master, image=img_Capitan_America_tk)
        self.lbl_img_Capitan_America.image = img_Capitan_America_tk
        self.lbl_img_Capitan_America.pack()
        self.lbl_img_Capitan_America.place(x=250, y=250)
        
        img_Dr_Strange = Image.open("Dr_Strange.png")  
        img_Dr_Strange_tk = ImageTk.PhotoImage(img_Dr_Strange)
        self.lbl_img_Dr_Strange = tk.Label(master, image=img_Dr_Strange_tk)
        self.lbl_img_Dr_Strange.image = img_Dr_Strange_tk
        self.lbl_img_Dr_Strange.pack()
        self.lbl_img_Dr_Strange.place(x=400, y=250) 
        
        img_Black_Panther = Image.open("Black_Panther.png")  
        img_Black_Panther_tk = ImageTk.PhotoImage(img_Black_Panther)
        self.lbl_img_Black_Panther = tk.Label(master, image=img_Black_Panther_tk)
        self.lbl_img_Black_Panther.image = img_Black_Panther_tk
        self.lbl_img_Black_Panther.pack() 
        self.lbl_img_Black_Panther.place(x=550, y=250)
        
        img_Scarlet_Witch = Image.open("Scarlet_Witch.png")  
        img_Scarlet_Witch_tk = ImageTk.PhotoImage(img_Scarlet_Witch)
        self.lbl_img_Scarlet_Witch = tk.Label(master, image=img_Scarlet_Witch_tk)
        self.lbl_img_Scarlet_Witch.image = img_Scarlet_Witch_tk
        self.lbl_img_Scarlet_Witch.pack()
        self.lbl_img_Scarlet_Witch.place(x=700, y=250)
        
        img_Loki = Image.open("Loki.png")  
        img_Loki_tk = ImageTk.PhotoImage(img_Loki)
        self.lbl_img_Loki = tk.Label(master, image=img_Loki_tk)
        self.lbl_img_Loki.image = img_Loki_tk
        self.lbl_img_Loki.pack()
        self.lbl_img_Loki.place(x=100, y=400)
        
        img_Venom = Image.open("Venom.png")  
        img_Venom_tk = ImageTk.PhotoImage(img_Venom)
        self.lbl_img_Venom = tk.Label(master, image=img_Venom_tk)
        self.lbl_img_Venom.image = img_Venom_tk
        self.lbl_img_Venom.pack()
        self.lbl_img_Venom.place(x=250, y=400)
        
        img_Storm = Image.open("Storm.png")  
        img_Storm_tk = ImageTk.PhotoImage(img_Storm)
        self.lbl_img_Storm = tk.Label(master, image=img_Storm_tk)
        self.lbl_img_Storm.image = img_Storm_tk
        self.lbl_img_Storm.pack()
        self.lbl_img_Storm.place(x=400, y=400)
        
        img_Abomination = Image.open("Abomination.png")  
        img_Abomination_tk = ImageTk.PhotoImage(img_Abomination)
        self.lbl_img_Abomination = tk.Label(master, image=img_Abomination_tk)
        self.lbl_img_Abomination.image = img_Abomination_tk
        self.lbl_img_Abomination.pack()
        self.lbl_img_Abomination.place(x=550, y=400)
        
        img_Baron_Mordo = Image.open("Baron_Mordo.png")  
        img_Baron_Mordo_tk = ImageTk.PhotoImage(img_Baron_Mordo)
        self.lbl_img_Baron_Mordo = tk.Label(master, image=img_Baron_Mordo_tk)
        self.lbl_img_Baron_Mordo.image = img_Baron_Mordo_tk
        self.lbl_img_Baron_Mordo.pack()
        self.lbl_img_Baron_Mordo.place(x=700, y=400)

        #Botones
        
        self.boton_cerrar = tk.Button(master, text="Siguiente", command=self.cerrar_ventana)
        self.boton_cerrar.config(font=("Arial", 20))
        self.boton_cerrar.config(bg="red", fg="black")
        self.boton_cerrar.place(x= 800, y = 500)

    def cerrar_ventana(self):
        self.master.destroy()
        nueva_ventana = Ventana2_RondaPreg()

class Ventana2_RondaPreg:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("1000x350+150+10")
        self.master.title("Ronda de preguntas")
        
        #Imagenes
        
        img_Spiderman = Image.open("Spiderman.png")  
        img_Spiderman_tk = ImageTk.PhotoImage(img_Spiderman)
        self.lbl_img_Spiderman = tk.Label(self.master, image=img_Spiderman_tk)
        self.lbl_img_Spiderman.image = img_Spiderman_tk
        self.lbl_img_Spiderman.pack()
        self.lbl_img_Spiderman.place(x=50,y=38)
        
        img_Ironman = Image.open("Ironman.png")  
        img_Ironman_tk = ImageTk.PhotoImage(img_Ironman)
        self.lbl_img_Ironman = tk.Label(self.master, image=img_Ironman_tk)
        self.lbl_img_Ironman.image = img_Ironman_tk
        self.lbl_img_Ironman.pack()
        self.lbl_img_Ironman.place(x=200,y=38)
                    
        img_Deadpool = Image.open("Deadpool.png")  
        img_Deadpool_tk = ImageTk.PhotoImage(img_Deadpool)
        self.lbl_img_Deadpool = tk.Label(self.master, image=img_Deadpool_tk)
        self.lbl_img_Deadpool.image = img_Deadpool_tk
        self.lbl_img_Deadpool.pack()
        self.lbl_img_Deadpool.place(x=350,y=38)
        
        img_Wolverine = Image.open("Wolverine.png")  
        img_Wolverine_tk = ImageTk.PhotoImage(img_Wolverine)
        self.lbl_img_Wolverine = tk.Label(self.master, image=img_Wolverine_tk)
        self.lbl_img_Wolverine.image = img_Wolverine_tk
        self.lbl_img_Wolverine.pack()
        self.lbl_img_Wolverine.place(x=500,y=38)
        
        img_Hulk = Image.open("Hulk.png")  
        img_Hulk_tk = ImageTk.PhotoImage(img_Hulk)
        self.lbl_img_Hulk = tk.Label(self.master, image=img_Hulk_tk)
        self.lbl_img_Hulk.image = img_Hulk_tk
        self.lbl_img_Hulk.pack()
        self.lbl_img_Hulk.place(x=650,y=38)
        
        img_Thor = Image.open("Thor.png")  
        img_Thor_tk = ImageTk.PhotoImage(img_Thor)
        self.lbl_img_Thor = tk.Label(self.master, image=img_Thor_tk)
        self.lbl_img_Thor.image = img_Thor_tk
        self.lbl_img_Thor.pack()
        self.lbl_img_Thor.place(x=50,y=148)
        
        img_Capitan_America = Image.open("Capitan_America.png")  
        img_Capitan_America_tk = ImageTk.PhotoImage(img_Capitan_America)
        self.lbl_img_Capitan_America = tk.Label(self.master, image=img_Capitan_America_tk)
        self.lbl_img_Capitan_America.image = img_Capitan_America_tk
        self.lbl_img_Capitan_America.pack()
        self.lbl_img_Capitan_America.place(x=200,y=150)
        
        img_Dr_Strange = Image.open("Dr_Strange.png")  
        img_Dr_Strange_tk = ImageTk.PhotoImage(img_Dr_Strange)
        self.lbl_img_Dr_Strange = tk.Label(self.master, image=img_Dr_Strange_tk)
        self.lbl_img_Dr_Strange.image = img_Dr_Strange_tk
        self.lbl_img_Dr_Strange.pack()
        self.lbl_img_Dr_Strange.place(x=350,y=148)
        
        img_Black_Panther = Image.open("Black_Panther.png")  
        img_Black_Panther_tk = ImageTk.PhotoImage(img_Black_Panther)
        self.lbl_img_Black_Panther = tk.Label(self.master, image=img_Black_Panther_tk)
        self.lbl_img_Black_Panther.image = img_Black_Panther_tk
        self.lbl_img_Black_Panther.pack()
        self.lbl_img_Black_Panther.place(x=500,y=148)
        
        img_Scarlet_Witch = Image.open("Scarlet_Witch.png")  
        img_Scarlet_Witch_tk = ImageTk.PhotoImage(img_Scarlet_Witch)
        self.lbl_img_Scarlet_Witch = tk.Label(self.master, image=img_Scarlet_Witch_tk)
        self.lbl_img_Scarlet_Witch.image = img_Scarlet_Witch_tk
        self.lbl_img_Scarlet_Witch.pack()
        self.lbl_img_Scarlet_Witch.place(x=650,y=148)
        
        img_Loki = Image.open("Loki.png")  
        img_Loki_tk = ImageTk.PhotoImage(img_Loki)
        self.lbl_img_Loki = tk.Label(self.master, image=img_Loki_tk)
        self.lbl_img_Loki.image = img_Loki_tk
        self.lbl_img_Loki.pack()
        self.lbl_img_Loki.place(x=50,y=258)
        
        img_Venom = Image.open("Venom.png")  
        img_Venom_tk = ImageTk.PhotoImage(img_Venom)
        self.lbl_img_Venom = tk.Label(self.master, image=img_Venom_tk)
        self.lbl_img_Venom.image = img_Venom_tk
        self.lbl_img_Venom.pack()
        self.lbl_img_Venom.place(x=200,y=258)
        
        img_Storm = Image.open("Storm.png")  
        img_Storm_tk = ImageTk.PhotoImage(img_Storm)
        self.lbl_img_Storm = tk.Label(self.master, image=img_Storm_tk)
        self.lbl_img_Storm.image = img_Storm_tk
        self.lbl_img_Storm.pack()
        self.lbl_img_Storm.place(x=350,y=258)
        
        img_Abomination = Image.open("Abomination.png")  
        img_Abomination_tk = ImageTk.PhotoImage(img_Abomination)
        self.lbl_img_Abomination = tk.Label(self.master, image=img_Abomination_tk)
        self.lbl_img_Abomination.image = img_Abomination_tk
        self.lbl_img_Abomination.pack()
        self.lbl_img_Abomination.place(x=500,y=258)
        
        img_Baron_Mordo = Image.open("Baron_Mordo.png")  
        img_Baron_Mordo_tk = ImageTk.PhotoImage(img_Baron_Mordo)
        self.lbl_img_Baron_Mordo = tk.Label(self.master, image=img_Baron_Mordo_tk)
        self.lbl_img_Baron_Mordo.image = img_Baron_Mordo_tk
        self.lbl_img_Baron_Mordo.pack()
        self.lbl_img_Baron_Mordo.place(x=650,y=258)

        #Etiquetas
        
        self.lbl_tPers = tk.Label(self.master, text="Personajes")
        self.lbl_tPers.config(font=("Arial Bold", 20))
        self.lbl_tPers.config(fg="green")
        self.lbl_tPers.pack()
        
        
        
        iniciar_juego(self.master)   
        
        self.master.mainloop()
    
    def cerrar_ventana(self):
        self.master.destroy()
        

    

if __name__ == "__main__":
    
    # Crear la ventana inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.geometry("1000x650+150+10")
    ventana_inicio.title("Personajes")
 

    # Crear una instancia de VentanaAnterior
    ventana = Ventana1_MostrarPers(ventana_inicio)

    ventana_inicio.mainloop()
