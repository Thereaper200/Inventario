import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pymongo import MongoClient
from datetime import datetime
from pymongo.server_api import ServerApi


def get_database():
    uri = "mongodb+srv://"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

        # Create the database for our example (we will use the same database throughout the tutorial
    return client['']


dbname = get_database()

coleccion = dbname['']

lista_oficinas = ['Oficina 2', 'Oficina 3', 'Oficina 4', 'Oficina 5', 'QC', 'Incubadora', 'AGTECH']

lista_turnos = ['Turno Diurno', 'Turno Nocturno']

lista_horario = ['Inicio', 'Final']


def send_data():
    fecha = datetime.now()
    ipad_data = int(ipad.get())
    lapiz_data = int(lapiz.get())
    cable_data = int(cable.get())
    adaptador_data = int(adaptador.get())
    base1_data = int(base1.get())
    base2_data = int(base2.get())

    oficina_data = valor_oficnas.get()
    turno_data = valor_turno.get()
    horario_data = valor_horario.get()

    while oficina_data != 'Selecciona Una Oficina' and turno_data != 'Selecciona Un Turno' and \
            horario_data != 'Selecciona Una Opción':

        coleccion.insert_one({'Oficina': oficina_data, 'turno': turno_data, 'horario': horario_data, 'iPads': ipad_data,
                              'Lapices': lapiz_data, 'Cables': cable_data, 'Adaptadores': adaptador_data,
                              'Bases 1ra Generacion': base1_data, 'Base 2da Generacion': base2_data, 'fecha': fecha})

        messagebox.showinfo("showinfo", "Inventario Agregado con Exito")
        break


mywindow = Tk()
mywindow.geometry("650x650")
mywindow.title("Inventario | Alpha Version")
mywindow.resizable(False, False)
mywindow.iconbitmap('ProjectIcon.ico')
mywindow.config(background="#F0F8FF")
main_title = Label(text="Inventario", font=("Cambria", 13), bg="#8B0000", fg="white", width="550", height="2")
main_title.pack()

image = Image.open("ProjectIcon.png")
image = image.resize((200, 200), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
img_label = tkinter.Label(mywindow, image=img, bg="#F0F8FF")
img_label.place(x=500, y=200, anchor=CENTER)

ipad_label = Label(text="iPad", bg="#F0F8FF", foreground="black")
ipad_label.place(x=22, y=70)
lapiz_label = Label(text="Lápiz", bg="#F0F8FF", foreground="black")
lapiz_label.place(x=22, y=130)
cable_label = Label(text="Cable", bg="#F0F8FF", foreground="black")
cable_label.place(x=22, y=190)
adaptador_label = Label(text="Adaptador", bg="#F0F8FF", foreground="black")
adaptador_label.place(x=22, y=250)
base1_label = Label(text="Bases 1ra Generación", bg="#F0F8FF", foreground="black")
base1_label.place(x=22, y=310)
base2_label = Label(text="Bases 2da Generación", bg="#F0F8FF", foreground="black")
base2_label.place(x=22, y=370)

ipad = StringVar()
lapiz = StringVar()
cable = StringVar()
adaptador = StringVar()
base1 = StringVar()
base2 = StringVar()
valor_oficnas = tkinter.StringVar(mywindow)
valor_turno = tkinter.StringVar(mywindow)
valor_horario = tkinter.StringVar(mywindow)

valor_oficnas.set('Selecciona Una Oficina')

menu_oficinas = tkinter.OptionMenu(mywindow, valor_oficnas, *lista_oficinas)
menu_oficinas.config(bg='white', fg='black')
menu_oficinas.place(x=22, y=38)

valor_turno.set('Selecciona Un Turno')

menu_turno = tkinter.OptionMenu(mywindow, valor_turno, *lista_turnos)
menu_turno.config(bg='white', fg='black')
menu_turno.place(x=210, y=38)

valor_horario.set('Selecciona Una Opción')

menu_horario = tkinter.OptionMenu(mywindow, valor_horario, *lista_horario)
menu_horario.config(bg='white', fg='black')
menu_horario.place(x=385, y=38)


ipad_entry = Entry(textvariable=ipad, width=40)
ipad_entry.place(x=22, y=100)
lapiz_entry = Entry(textvariable=lapiz, width=40)
lapiz_entry.place(x=22, y=160)
cable_entry = Entry(textvariable=cable, width=40)
cable_entry.place(x=22, y=220)
adaptador_entry = Entry(textvariable=adaptador, width=40)
adaptador_entry.place(x=22, y=280)
base1_entry = Entry(textvariable=base1, width=40)
base1_entry.place(x=22, y=340)
base2_entry = Entry(textvariable=base2, width=40)
base2_entry.place(x=22, y=400)

submit_btn = Button(mywindow, text="Subir información", command=send_data, width="30", height="2", bg="black")
submit_btn.place(x=22, y=480)

mywindow.mainloop()
