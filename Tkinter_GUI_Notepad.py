from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class Notepad(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("500x400")
        self.title("Untitled - Notepad")
        self.wm_iconbitmap("29_icon.ico")

        self.file = None
        self.textArea = Text(self, font="lucida 13")
        self.textArea.pack(expand=TRUE, fill=BOTH)

        self.scrollbar = Scrollbar(self.textArea)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)

    
    def new(self):
        self.file = None
        self.title("Untitled - Notepad")
        self.textArea.delete(1.0, END)
    
    def open(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.title(os.path.basename(self.file) + " - Notepad")
            self.textArea.delete(1.0, END)
            self.f = open(self.file, "r")
            self.textArea.insert(1.0, self.f.read())
            self.f.close()
            
    def save(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                #save as a new file
                self.f = open(self.file, "w")
                self.f.write(self.textArea.get(1.0, END))
                self.f.close()
                self.title(os.path.basename(self.file) + " - Notepad")
                print("FIle Saved")
        else:
            # save the file
            self.f = open(self.file, "w")
            self.f.write(self.textArea.get(1.0, END))
            self.f.close()
            
    def cut(self):
        self.textArea.event_generate(("<<Cut>>"))
    
    def copy(self):
        self.textArea.event_generate(("<<Copy>>"))

    def paste(self):
        self.textArea.event_generate(("<<Paste>>"))

    def help(self):
        self.msg = tmsg.showinfo("Deep's Notepad", "This Notepad is created by Deep")
        
    def quit(self):
        self.destroy()

    def ribbon(self):
        self.mainMenu = Menu(self)

        self.sm1 = Menu(self.mainMenu, tearoff=0)
        self.sm1.add_command(label="New", command=self.new)
        self.sm1.add_command(label="Open", command=self.open)
        self.sm1.add_command(label="Save", command=self.save)
        self.sm1.add_command(label="Exit", command=self.quit)
        self.mainMenu.add_cascade(label="File", menu=self.sm1)

        self.sm2 = Menu(self.mainMenu, tearoff=0)
        self.sm2.add_command(label="Cut", command=self.cut)
        self.sm2.add_command(label="Copy", command=self.copy)
        self.sm2.add_command(label="Paste", command=self.paste)
        self.mainMenu.add_cascade(label="Edit", menu=self.sm2)

        self.sm3 = Menu(self.mainMenu, tearoff=0)
        self.sm3.add_command(label="About Notepad", command=self.help)
        self.mainMenu.add_cascade(label="Help", menu=self.sm3)
        self.config(menu=self.mainMenu)
    
if __name__ == '__main__':
    window = Notepad()
    window.ribbon()
    window.mainloop()