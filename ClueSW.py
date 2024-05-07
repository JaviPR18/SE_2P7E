import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

# Define los personajes, habitaciones y armas de Star Wars
personajes = ["Luke", "Leia", "Han", "Anakin", "Yoda"]
habitaciones = ["Estrella_de_la_muerte", "Tatooine", "Endor", "Mandalore", "Mustafar"]
armas = ["Sable", "Blaster", "Ballesta", "Amban", "La_Fuerza"]

# Genera una solución aleatoria
def Aleatorio(solucion):
    solucion = {
        "personaje": random.choice(personajes),
        "habitacion": random.choice(habitaciones),
        "arma": random.choice(armas)
    }
    return solucion

def casos(opc):
    n_sol = {}
    
    txtHis = ''' '''
    personaje = opc['personaje']
    
    if personaje == 'Luke':
        txtHis = '''
            Durante el encuentro, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de esta. 
            Los presentes corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Chewbacca, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
        
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
            
            -Luke afirmó que estaba en Tatooine buscando a Obi-Wan Kenobi.
            -Leia dijo que estaba en Endor negociando con los ewoks.
            -Han mencionó que estaba en la Estrella de la Muerte con Chewbacca jugando 
            dejar de contrabando.
            -Anakin alegó que estaba en Mustafar buscando a su esposa, Padmé.
            -Yoda declaró que estaba en Mandalore meditando sobre el futuro de la galaxia.
             '''
        n_sol = {
             "personaje":"Luke",
             "habitacion": "Tatooine",
             "arma": "Sable"
                      } 
    if personaje == 'Leia':
        txtHis = '''
            Durante el encuentro, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los presentes corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Chewbacca, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
        
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
            
            -Luke afirmó que estaba en la Estrella de la Muerte buscando a su padre.
            -Leia dijo que estaba en Tatooine reclutando nuevos rebeldes.
            -Han mencionó que estaba en Endor con  organizando una fiesta.
            -Anakin alegó que estaba en Mustafar tratando de controlar su ira.
            -Yoda declaró que estaba en Mandalore meditando sobre la Fuerza.
           '''
        n_sol = {
            "personaje":"Leia",
            "habitacion": "Tatooine",
            "arma": "Blaster"
        }
    if personaje == 'Han':
        txtHis = '''
            Durante el encuentro, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los presentes corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Chewbacca, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
        
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
            
            -Luke afirmó que estaba en Tatooine buscando a Jabba el Hutt.
            -Leia dijo que estaba en Endor organizando una resistencia contra el Imperio.
            -Han mencionó que estaba en la Estrella de la Muerte con Chewbacca reparando 
            el Halcón Milenario.
           -Anakin alegó que estaba en Mustafar intentando rectificar sus errores pasados.
           -Yoda declaró que estaba en Mandalore enseñando a los jóvenes jedi.
          '''
        n_sol = {
            "personaje":"Han",
            "habitacion": "Estrella_de_la_muerte",
            "arma": "Ballesta"
        }
    if personaje == 'Anakin':
        txtHis = '''
            Durante el encuentro, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los presentes corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Chewbacca, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
        
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
            
            -Luke afirmó que estaba en Tatooine entrenando con Obi-Wan Kenobi.
            -Leia dijo que estaba en Endor buscando aliados para la Rebelión.
            -Han mencionó que estaba en la Estrella de la Muerte jugando sabacc.
            -Anakin alegó que estaba en Mustafar tratando de redimirse.
            -Yoda declaró que estaba en Mandalore meditando sobre el Lado Oscuro.
          '''
        n_sol = {
            "personaje":"Anakin",
            "habitacion": "Mustafar",
            "arma": "Amban"
        }
    if personaje == 'Yoda':
        txtHis = '''
            Durante el encuentro, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los presentes corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Chewbacca, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
        
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
            
            -Luke afirmó que estaba en Tatooine meditando sobre el futuro de la galaxia.
            -Leia dijo que estaba en Endor discutiendo estrategias de combate.
            -Han mencionó que estaba en la Estrella de la Muerte realizando negocios con 
            Lando Calrissian.
            -Anakin alegó que estaba en Mustafar buscando paz interior.
            -Yoda declaró que estaba en Mandalore enseñando a los jóvenes padawans.
          '''
        n_sol = {
            "personaje":"Yoda",
            "habitacion": "Mandalore",
            "arma": "La_Fuerza"
        }
    return txtHis, n_sol

class Ventana2_DTrama:
    def __init__(self, master, venIm):
        self.master = master
        self.venIm = venIm
        
        self.solucion = {}
        
        # Variables para almacenar la selección
        self.opc_Pers = tk.StringVar()
        self.opc_Place = tk.StringVar()
        self.opc_Arma = tk.StringVar()
        
        # Añadimos un contador de intentos
        self.intentos = 0
        self.max_intentos = 3
        
        #Etiquetas
        #Historia
        self.lbl_hist = tk.Label(self.master, text="", justify="left", font=("Arial", 11))
        self.lbl_hist.pack()
        
        
        #Preguntas
        self.lbl_pers = tk.Label(self.master, text="¿Quién es el asesino?", justify="center", font=("Arial", 11), fg="blue")
        self.lbl_pers.pack()
        self.lbl_pers.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_pers.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=40)
        
        self.lbl_place = tk.Label(self.master, text="¿Dónde se cometió el crimen?", justify="center", font=("Arial", 11), fg="green")
        self.lbl_place.pack()
        self.lbl_place.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_place.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=100)
     
        
        self.lbl_arma = tk.Label(self.master, text="¿Qué arma se usó?", justify="center", font=("Arial", 11), fg="red")
        self.lbl_arma.pack()
        self.lbl_arma.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_arma.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=160)
        
        # Crear radio buttons
        #Personaje
        self.radio_boton1 = tk.Radiobutton(self.master, text="Luke", variable=self.opc_Pers, value="Luke")
        self.radio_boton2 = tk.Radiobutton(self.master, text="Leia", variable=self.opc_Pers, value="Leia")
        self.radio_boton3 = tk.Radiobutton(self.master, text="Han", variable=self.opc_Pers, value="Han")
        self.radio_boton4 = tk.Radiobutton(self.master, text="Anakin", variable=self.opc_Pers, value="Anakin")
        self.radio_boton5 = tk.Radiobutton(self.master, text="Yoda", variable=self.opc_Pers, value="Yoda")
        
        #Lugar
        self.radio_boton6 = tk.Radiobutton(self.master, text="Estrella de la Muerte", variable=self.opc_Place, value="Estrella_de_la_muerte")
        self.radio_boton7 = tk.Radiobutton(self.master, text="Tatooine", variable=self.opc_Place, value="Tatooine")
        self.radio_boton8 = tk.Radiobutton(self.master, text="Endor", variable=self.opc_Place, value="Endor")
        self.radio_boton9 = tk.Radiobutton(self.master, text="Mandalore", variable=self.opc_Place, value="Mandalore")
        self.radio_boton10 = tk.Radiobutton(self.master, text="Mustafar", variable=self.opc_Place, value="Mustafar")
        
        
        #Arma
        self.radio_boton11 = tk.Radiobutton(self.master, text="Sable", variable=self.opc_Arma, value="Sable")
        self.radio_boton12 = tk.Radiobutton(self.master, text="Blaster", variable=self.opc_Arma, value="Blaster")
        self.radio_boton13 = tk.Radiobutton(self.master, text="Ballesta", variable=self.opc_Arma, value="Ballesta")
        self.radio_boton14 = tk.Radiobutton(self.master, text="Amban", variable=self.opc_Arma, value="Amban")
        self.radio_boton15 = tk.Radiobutton(self.master, text="La Fuerza", variable=self.opc_Arma, value="La_Fuerza")
        
        # Posicionar radio buttons
        
        self.radio_boton1.pack()
        self.radio_boton2.pack()
        self.radio_boton3.pack()
        self.radio_boton4.pack()
        self.radio_boton5.pack()
        self.radio_boton6.pack()
        self.radio_boton7.pack()
        self.radio_boton8.pack()
        self.radio_boton9.pack()
        self.radio_boton10.pack()
        self.radio_boton11.pack()
        self.radio_boton12.pack()
        self.radio_boton13.pack()
        self.radio_boton14.pack()
        self.radio_boton15.pack()
        
        
        self.radio_boton1.place(x=10,y=400)
        self.radio_boton2.place(x=110,y=400)
        self.radio_boton3.place(x=220,y=400)
        self.radio_boton4.place(x=330,y=400)
        self.radio_boton5.place(x=440,y=400)
        
        self.radio_boton6.place(x=5,y=460)
        self.radio_boton7.place(x=130,y=460)
        self.radio_boton8.place(x=220,y=460)
        self.radio_boton9.place(x=370,y=460)
        self.radio_boton10.place(x=450,y=460)
        
        self.radio_boton11.place(x=5,y=520)
        self.radio_boton12.place(x=235,y=520)
        self.radio_boton13.place(x=425,y=520)
        self.radio_boton14.place(x=150,y=540)
        self.radio_boton15.place(x=350,y=540)


        # Botón para mostrar selección
        self.boton_mostrar = tk.Button(self.master, text="Comprobar suposiciones", command=self.comp_sup)
        self.boton_mostrar.pack()
        self.boton_mostrar.config(font=("Arial", 14))
        self.boton_mostrar.config(bg="purple", fg="white")
        self.boton_mostrar.place(x=180,y=600)
        
        
        self.selec_random()
        self.mostrar_hist()
        
    def cerrar_ventana(self):
      self.master.destroy()
     
    def cerrar_ventanas(self):
        self.master.destroy()  # Cierra la ventana principal
        if hasattr(self, "ventana_secundaria"):
            self.ventana_secundaria.destroy()  # Cierra la ventana secundaria
        self.venIm.destroy()
    def selec_random(self):
        self.solucion = Aleatorio(self.solucion)
 
    def mostrar_hist(self):
     self.historia,self.n_sol = casos(self.solucion)
     self.txt = self.historia
     self.solucion = self.n_sol

     
     self.lbl_hist.config(text= self.txt)
 
    def comp_sup(self):
     self.sel_pers = self.opc_Pers.get()
     self.sel_place = self.opc_Place.get()
     self.sel_arma = self.opc_Arma.get()
     
     
     #print("Personaje",self.solucion["personaje"])
     #print("Lugar",self.solucion["habitacion"])
     #print("Arma",self.solucion["arma"])


     
     self.intentos += 1
     
     if self.sel_pers in self.solucion["personaje"] and self.sel_place in self.solucion["habitacion"] and self.sel_arma in self.solucion["arma"]:
         messagebox.showinfo("¡Ganaste!", "¡Has adivinado correctamente!")
               
         # Preguntar si desea jugar de nuevo
         if messagebox.askyesno("Jugar de nuevo", "¿Deseas volver a jugar?"):
             self.intentos = 0
             self.selec_random()
             self.mostrar_hist()
         else:
             self.cerrar_ventanas()
                     
   
     else:
         if self.intentos < self.max_intentos:
             messagebox.showinfo("¡Fallaste!", "Intenta de nuevo.")
         
         if self.intentos >= self.max_intentos:
             messagebox.showinfo("¡Fallaste!", "Has agotado tus intentos.")

             # Preguntar si desea jugar de nuevo
             if messagebox.askyesno("Jugar de nuevo", "¿Deseas volver a jugar?"):
                 self.intentos = 0
                 self.selec_random()
                 self.mostrar_hist()
             else:
                 self.cerrar_ventanas()
                 
class Ventana1_MostrarPers:
    def __init__(self, master):
        self.master = master

        #Etiquetas
        
        self.lbl_title = tk.Label(master, text="¡Bienvenido a Stars Clue")
        self.lbl_title.config(font=("Arial Bold", 20))
        self.lbl_title.config(fg="green")
        self.lbl_title.place(x=75,y=5)
        
        self.lbl_title2 = tk.Label(master, text="Murdered")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="red")
        self.lbl_title2.place(x=650,y=2)
        
        self.lbl_title2 = tk.Label(master, text="Personajes")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=90,y=40)
        
        self.lbl_title2 = tk.Label(master, text="Escenas de Crimen")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=345,y=80)
        
        self.lbl_title2 = tk.Label(master, text="Armas")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=655,y=135)
        
        
        #Imagenes
        
        #Personajes
        
        img_chew = Image.open("chew.png")
        img_chew_tk = ImageTk.PhotoImage(img_chew)
        self.lbl_img_chew = tk.Label(master, image=img_chew_tk)
        self.lbl_img_chew.image = img_chew_tk
        self.lbl_img_chew.place(x=675, y=27)

        img_luke = Image.open("luke.png")
        img_luke_tk = ImageTk.PhotoImage(img_luke)
        self.lbl_img_luke = tk.Label(master, image=img_luke_tk)
        self.lbl_img_luke.image = img_luke_tk
        self.lbl_img_luke.pack()
        self.lbl_img_luke.place(x=100, y=75)  # Comment goes here

        img_leia = Image.open("leia.png")
        img_leia_tk = ImageTk.PhotoImage(img_leia)
        self.lbl_img_leia = tk.Label(master, image=img_leia_tk)
        self.lbl_img_leia.image = img_leia_tk
        self.lbl_img_leia.pack()
        self.lbl_img_leia.place(x=100, y=195)

        img_anakin = Image.open("anakin.png")
        img_anakin_tk = ImageTk.PhotoImage(img_anakin)
        self.lbl_img_anakin = tk.Label(master, image=img_anakin_tk)
        self.lbl_img_anakin.image = img_anakin_tk
        self.lbl_img_anakin.pack()
        self.lbl_img_anakin.place(x=100, y=315)

        img_han = Image.open("han.png")
        img_han_tk = ImageTk.PhotoImage(img_han)
        self.lbl_img_han = tk.Label(master, image=img_han_tk)
        self.lbl_img_han.image = img_han_tk
        self.lbl_img_han.pack()
        self.lbl_img_han.place(x=100, y=435)

        img_yoda = Image.open("yoda.png")
        img_yoda_tk = ImageTk.PhotoImage(img_yoda)
        self.lbl_img_yoda = tk.Label(master, image=img_yoda_tk)
        self.lbl_img_yoda.image = img_yoda_tk
        self.lbl_img_yoda.pack()
        self.lbl_img_yoda.place(x=100, y=555)

#Lugares 
        
        img_Estrella_de_la_muerte = Image.open("Estrella_de_la_muerte.png")  
        img_Estrella_de_la_muerte_tk = ImageTk.PhotoImage(img_Estrella_de_la_muerte)
        self.lbl_img_Estrella_de_la_muerte = tk.Label(master, image=img_Estrella_de_la_muerte_tk)
        self.lbl_img_Estrella_de_la_muerte.image = img_Estrella_de_la_muerte_tk
        self.lbl_img_Estrella_de_la_muerte.pack()
        self.lbl_img_Estrella_de_la_muerte.place(x=345,y=115)
        
        img_Tatooine = Image.open("Tatooine.png")  
        img_Tatooine_tk = ImageTk.PhotoImage(img_Tatooine)
        self.lbl_img_Tatooine = tk.Label(master, image=img_Tatooine_tk)
        self.lbl_img_Tatooine.image = img_Tatooine_tk
        self.lbl_img_Tatooine.pack()
        self.lbl_img_Tatooine.place(x=345,y=230)
                    
        img_endor = Image.open("Endor.png")
        img_endor_tk = ImageTk.PhotoImage(img_endor)
        self.lbl_img_endor = tk.Label(master, image=img_endor_tk)
        self.lbl_img_endor.image = img_endor_tk
        self.lbl_img_endor.pack()
        self.lbl_img_endor.place(x=345, y=345)
        
        img_mustafar = Image.open("Mustafar.png")
        img_mustafar_tk = ImageTk.PhotoImage(img_mustafar)
        self.lbl_img_mustafar = tk.Label(master, image=img_mustafar_tk)
        self.lbl_img_mustafar.image = img_mustafar_tk
        self.lbl_img_mustafar.pack()
        self.lbl_img_mustafar.place(x=345, y=460)
        
        img_mandalore = Image.open("Mandalore.png")
        img_mandalore_tk = ImageTk.PhotoImage(img_mandalore)
        self.lbl_img_mandalore = tk.Label(master, image=img_mandalore_tk)
        self.lbl_img_mandalore.image = img_mandalore_tk
        self.lbl_img_mandalore.pack()
        self.lbl_img_mandalore.place(x=345, y=575)
        
        #armas
        
        img_Estrella_de_la_muerte = Image.open("Sable.png")  
        img_Estrella_de_la_muerte_tk = ImageTk.PhotoImage(img_Estrella_de_la_muerte)
        self.lbl_img_Estrella_de_la_muerte = tk.Label(master, image=img_Estrella_de_la_muerte_tk)
        self.lbl_img_Estrella_de_la_muerte.image = img_Estrella_de_la_muerte_tk
        self.lbl_img_Estrella_de_la_muerte.pack()
        self.lbl_img_Estrella_de_la_muerte.place(x=640,y=170)
        
        img_Tatooine = Image.open("Blaster.png")  
        img_Tatooine_tk = ImageTk.PhotoImage(img_Tatooine)
        self.lbl_img_Tatooine = tk.Label(master, image=img_Tatooine_tk)
        self.lbl_img_Tatooine.image = img_Tatooine_tk
        self.lbl_img_Tatooine.pack()
        self.lbl_img_Tatooine.place(x=640,y=266)
                    
        img_endor = Image.open("Ballesta.png")
        img_endor_tk = ImageTk.PhotoImage(img_endor)
        self.lbl_img_endor = tk. Label(master, image=img_endor_tk)
        self.lbl_img_endor.image = img_endor_tk
        self.lbl_img_endor.pack()
        self.lbl_img_endor.place(x=640,y=362)
        
        img_mustafar = Image.open("The_force.png")
        img_mustafar_tk = ImageTk.PhotoImage(img_mustafar)
        self.lbl_img_mustafar = tk.Label(master, image=img_mustafar_tk)
        self.lbl_img_mustafar.image = img_mustafar_tk
        self.lbl_img_mustafar.pack()
        self.lbl_img_mustafar.place(x=640,y=458)
        
        img_mandalore = Image.open("Amban.png")
        img_mandalore_tk = ImageTk.PhotoImage(img_mandalore)
        self.lbl_img_mandalore = tk.Label(master, image=img_mandalore_tk)
        self.lbl_img_mandalore.image = img_mandalore_tk
        self.lbl_img_mandalore.pack()
        self.lbl_img_mandalore.place(x=640,y=594)
       

    def cerrar_ventana(self):
        self.master.destroy()
        
if __name__ == "__main__":
    
    # Crear la ventana inicio <principal>
    ventana_inicio = tk.Tk()
    ventana_inicio.geometry("800x695+0+0")
    ventana_inicio.title("Personajes")
 

    # Crear una instancia de ventana_inicio
    ventana1 = Ventana1_MostrarPers(ventana_inicio)
    
    # Crear una ventana secundaria a partir de la de inicio
    ventana_preg =  tk.Toplevel(ventana_inicio)
    ventana_preg.geometry("560x695+801+0")
    ventana_preg.title("Trama Pregustas")
 

    # Crear una instancia de ventana_preg
    ventana2 = Ventana2_DTrama(ventana_preg, ventana_inicio)
    
    
    ventana_inicio.mainloop()

    