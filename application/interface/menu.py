from tkinter import Button, Frame, Label, Tk

class Menu:

    def __init__(self):
        self.master = Tk()
        self.master.title('Finanças Pessoais')
        self.master.geometry('640x480')
        self.master.resizable(width=False,height=False)

        self.menu_iniciar(self.master)

        self.master.mainloop()

    def menu_iniciar(self, tk):
        self.fr1 = Frame(tk)
        self.fr1.pack()

        self.title = Label(self.fr1, text='Finanças Pessoais')
        self.title.config(font=('sans-serif', 30))
        self.title.pack()




instance = Menu
instance()