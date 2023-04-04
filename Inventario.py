import tkinter
from tkinter import *
from PIL import ImageTk, Image
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)

db = client.inventario

coleccion = db.Inventarios_2023


def send_data():
    fecha = datetime.now()
    ipad_data = ipad.get()
    lapiz_data = lapiz.get()
    cable_data = cable.get()
    adaptador_data = adaptador.get()
    base1_data = base1.get()
    base2_data = base2.get()

    oficina2_data = oficina2.get()
    oficina3_data = oficina3.get()
    oficina4_data = oficina4.get()
    oficina5_data = oficina5.get()
    qc_data = qc.get()
    incubadora_data = incubadora.get()
    oficina_data = [oficina2_data, oficina3_data, oficina4_data, oficina5_data, qc_data, incubadora_data]

    dayshift_data = dayshift.get()
    nightshift_day = nightshift.get()
    turno_data = [dayshift_data, nightshift_day]

    coleccion.insert_one({'Oficina': oficina_data, 'turno': turno_data, 'iPads': ipad_data, 'Lapices': lapiz_data,
                          'Cables': cable_data, 'Adaptadores': adaptador_data,
                          'Bases 1ra Generacion': base1_data, 'Base 2da Generacion': base2_data, 'fecha': fecha})


mywindow = Tk()
mywindow.geometry("650x650")
mywindow.title("Inventario | Alpha Version")
mywindow.resizable(False, False)
mywindow.config(background="#F0F8FF")
main_title = Label(text="Inventario", font=("Cambria", 13), bg="#8B0000", fg="white", width="550", height="2")
main_title.pack()

image = Image.open("ProjectIcon.png")
image = image.resize((200, 200), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
img_label = tkinter.Label(mywindow, image=img)
img_label.place(x=500, y=200, anchor=CENTER)

ipad_label = Label(text="iPad", bg="#F0F8FF", foreground="black")
ipad_label.place(x=22, y=70)
lapiz_label = Label(text="Lapiz", bg="#F0F8FF", foreground="black")
lapiz_label.place(x=22, y=130)
cable_label = Label(text="Cable", bg="#F0F8FF", foreground="black")
cable_label.place(x=22, y=190)
adaptador_label = Label(text="Adaptador", bg="#F0F8FF", foreground="black")
adaptador_label.place(x=22, y=250)
base1_label = Label(text="Bases 1ra Generacion", bg="#F0F8FF", foreground="black")
base1_label.place(x=22, y=310)
base2_label = Label(text="Bases 2da Generacion", bg="#F0F8FF", foreground="black")
base2_label.place(x=22, y=370)

ipad = IntVar()
lapiz = IntVar()
cable = IntVar()
adaptador = IntVar()
base1 = IntVar()
base2 = IntVar()

oficina2 = IntVar()
oficina3 = IntVar()
oficina4 = IntVar()
oficina5 = IntVar()
qc = StringVar()
incubadora = StringVar()

dayshift = StringVar()
nightshift = StringVar()

dayshift_entry = Checkbutton(mywindow, text="Turno Diurno", variable=dayshift,
                             onvalue='Dia', offvalue=False, bg='#F0F8FF', fg='black')
dayshift_entry.place(x=500, y=38)

nightshift_entry = Checkbutton(mywindow, text="Turno Nocturno", variable=nightshift,
                               onvalue='Noche', offvalue=False, bg='#F0F8FF', fg='black')
nightshift_entry.place(x=500, y=60)

oficina2_entry = Checkbutton(mywindow, text="Of2", variable=oficina2,
                             onvalue=2, offvalue=False, bg='#F0F8FF', fg='black')
oficina2_entry.place(x=22, y=38)
oficina3_entry = Checkbutton(mywindow, text="Of3", variable=oficina3,
                             onvalue=3, offvalue=False, bg='#F0F8FF', fg='black')
oficina3_entry.place(x=73, y=38)
oficina4_entry = Checkbutton(mywindow, text="Of4", variable=oficina4,
                             onvalue=4, offvalue=False, bg='#F0F8FF', fg='black')
oficina4_entry.place(x=124, y=38)
oficina5_entry = Checkbutton(mywindow, text="Of5", variable=oficina5,
                             onvalue=5, offvalue=False, bg='#F0F8FF', fg='black')
oficina5_entry.place(x=175, y=38)
qc_entry = Checkbutton(mywindow, text="QC", variable=qc,
                       onvalue='QC', offvalue=False, bg='#F0F8FF', fg='black')
qc_entry.place(x=226, y=38)
incubadora_entry = Checkbutton(mywindow, text="Incubadora", variable=incubadora,
                               onvalue='Incubadora', offvalue=False, bg='#F0F8FF', fg='black')
incubadora_entry.place(x=277, y=38)

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

submit_btn = Button(mywindow, text="Subir informacion", command=send_data, width="30", height="2", bg="black")
submit_btn.place(x=22, y=480)

mywindow.mainloop()
