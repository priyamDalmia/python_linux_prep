import tkinter as tk 


def on_click() -> None:
    myapp.destroy()

myapp = tk.Tk()
myapp.title("Testp!")
button = tk.Button(myapp, text='Button', command=on_click)
# button.pack()
button.place(x=15, y=10)
myapp.mainloop()