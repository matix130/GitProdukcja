import tkinter

def jakas_funkcja():
    c=int(dystans.get())
    d=int(paliwo.get())
    e=int(spalanie.get())
    koszt = (c / 100) * d * e
    koszt = round(koszt, 2)
    print(koszt)
    wynik.configure(text=koszt)

root=tkinter.Tk()
root.columnconfigure(1)
paliwo=tkinter.Entry(master=root)
paliwo.grid(row=0, column=0)

label_paliwo = tkinter.Label(master=root, text="Podaj cenę paliwa")
label_paliwo.grid(row=0, column=1)

dystans=tkinter.Entry(master=root)
dystans.grid(row=1, column=0)

label_dystans = tkinter.Label(master=root, text="Podaj dystans między miastami")
label_dystans.grid(row=1, column=1)


spalanie=tkinter.Entry(master=root)
spalanie.grid(row=2, column=0)

label_spalanie = tkinter.Label(master=root, text="Podaj spalanie na 100 km")
label_spalanie.grid(row=2, column=1)

wynik=tkinter.Label(master=root, text="")
wynik.grid(row=4, column=2)


button=tkinter.Button(master=root, text="Kliknij tu", command=jakas_funkcja)
button.grid(row=4, column=4)
root.mainloop()