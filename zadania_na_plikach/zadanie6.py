import tkinter

def jakas_funkcja():
    wartosc = entry.get()
    label.configure(text=wartosc)


root=tkinter.Tk()
root.columnconfigure(1)
entry=tkinter.Entry(master=root)
entry.grid(row=0, column=0)
label = tkinter.Label(master=root, text="napis")
label.grid(row=0, column=1)
button=tkinter.Button(master=root, text="Kliknij tu", command=jakas_funkcja)
button.grid(row=1, column=0)
root.mainloop()