import tkinter
from tkinter import *
from PIL import ImageTk, Image
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.inventario

coleccion = db.test

image = Image.open("ProjectIcon.png")
image = image.resize((200,200), Image.LANCZOS)

def send_data():
    iPad_data = iPad.get()
    lapiz_data = lapiz.get()
    cable_data = cable.get()
    adaptador_data = adaptador.get()
    print(iPad_data, lapiz_data, cable_data, adaptador_data)
    coleccion.insert_one({'Oficina': 1, 'iPads': iPad_data, 'Lapices': lapiz_data, 'Cables': cable_data, 'Adaptadores': adaptador_data})


mywindow = Tk()
mywindow.geometry("650x650")
mywindow.title("Inventario | Alpha Version")
mywindow.resizable(False, False)
mywindow.config(background="#F0F8FF")
main_title = Label(text="Inventario", font=("Cambria", 13), bg="#8B0000", fg="white", width="550", height="2")
img = ImageTk.PhotoImage(image)
img_label = tkinter.Label(mywindow, image=img)
img_label.pack()
main_title.pack()

img_label.place(x=500 ,y=200, anchor=CENTER)

iPad_label = Label(text="iPad", bg="#F0F8FF", foreground="black")
iPad_label.place(x=22, y=70)
lapiz_label = Label(text="Lapiz", bg="#F0F8FF", foreground="black")
lapiz_label.place(x=22, y=130)
cable_label = Label(text="Cable", bg="#F0F8FF", foreground="black")
cable_label.place(x=22, y=190)
adaptador_label = Label(text="Adaptador", bg="#F0F8FF", foreground="black")
adaptador_label.place(x=22, y=250)

iPad = IntVar()
lapiz = IntVar()
cable = IntVar()
adaptador = IntVar()


iPad_entry = Entry(textvariable=iPad, width=40)
iPad_entry.place(x=22, y=100)
lapiz_entry = Entry(textvariable=lapiz, width=40)
lapiz_entry.place(x=22, y=160)
cable_entry = Entry(textvariable=cable, width=40)
cable_entry.place(x=22, y=220)
adaptador_entry = Entry(textvariable=adaptador, width=40)
adaptador_entry.place(x=22, y=280)

submit_btn = Button(mywindow, text="Subir informacion", command=send_data, width="30", height="2", bg="black")
submit_btn.place(x=22, y=320)

mywindow.mainloop()
