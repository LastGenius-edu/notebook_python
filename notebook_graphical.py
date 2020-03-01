from tkinter import *
import tkinter.filedialog as fd
import time
from notebook import Notebook
from menu import Menu


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.main()

    def Quit(self, ev):
        """
        Ends the application after a button click
        """
        print("########Debug: Quit Application Button Pressed")
        self.master.destroy()

    def LoadFile(self, ev):
        """
        Loads the file using native file selector

        If the file name is empty, returns None
        """
        fn = fd.Open(self.master, filetypes=[('*.txt files', '.txt')]).show()

        if fn == '':
            print("########Debug: load file name is empty")
            return

        textbox.delete('1.0', 'end')
        textbox.insert('1.0', open(fn, 'rt').read())

    def SaveFile(self, ev):
        """
        Saves the file using native file save selector window.
        If file's name's empty, return None
        If file's name doesn't have .txt in it, just add it.
        """
        fn = fd.SaveAs(self.master, filetypes=[('*.txt files', '.txt')]).show()
        print(fn)

        if fn == '':
            print("########Debug: Name is empty")
            return

        if not fn.endswith(".txt"):
            fn += ".txt"
            print("########Debug file name:", fn)

        open(fn, 'wt').write(textbox.get('1.0', 'end'))

    def main(self):
        """
        The main function of the app
        Sets up a top frame, three buttons in it.
        Sets up a bottom frame with a textbox (scrollable).
        """
        panelFrame = Frame(self.master, height=60, bg='dark slate grey')
        textFrame = Frame(self.master, height=340, width=600)

        panelFrame.pack(side='top', fill='x')
        textFrame.pack(side='bottom', fill='both', expand=1)

        global textbox
        textbox = Text(textFrame, font='Arial 12', wrap='word')
        scrollbar = Scrollbar(textFrame)
        scrollbar['command'] = textbox.yview
        textbox['yscrollcommand'] = scrollbar.set

        textbox.pack(side='left', fill='both', expand=1)
        scrollbar.pack(side='right', fill='y')

        loadButton = Button(panelFrame, text='Load', font="Arial")
        saveButton = Button(panelFrame, text='Save', font="Arial")
        quitButton = Button(panelFrame, text='Quit', font="Arial")

        loadButton.bind("<Button-1>", self.LoadFile)
        saveButton.bind("<Button-1>", self.SaveFile)
        quitButton.bind("<Button-1>", self.Quit)

        loadButton.place(x=10, y=10, width=60, height=40)
        saveButton.place(x=80, y=10, width=60, height=40)
        quitButton.place(x=150, y=10, width=60, height=40)

        self.master.title("Sultanov Andriy's Notebook")
        self.master.mainloop()


root = Tk()
app = Application(master=root)
