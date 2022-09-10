from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def NewFile():
    global file
    root.title("Untitled - TextEditor")
    file=None
    TextArea.delete(1.0 , END)

def OpenFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - TextEditor")
        TextArea.delete(1.0 , END)
        f=open(file , "r")
        TextArea.insert(1.0 , f.read())
        f.close()

def SaveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0 , END))
            f.close()

            root.title(os.path.basename(file)+" - TextEditor")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def Exit():
    root.destroy()

def CutEdit():
    TextArea.event_generate(("<<Cut>>"))

def CopyEdit():
    TextArea.event_generate(("<<Copy>>"))

def PasteEdit():
    TextArea.event_generate(("<<Paste>>"))

def About():
    showinfo("Text Editor","This is a basic Text Editor Mini Project")

if __name__ == '__main__':
    # basic tkinter setup
    root=Tk()
    root.title("Text Editor")
    root.wm_iconbitmap("txtEditorIcon.ico")
    root.geometry("700x500")
    # text area
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill="both")
    # menubar
    MenuBar=Menu(root)
    # file menu
    M1=Menu(MenuBar,tearoff=0)
    M1.add_command(label="NEW",command=NewFile)
    M1.add_command(label="OPEN",command=OpenFile)
    M1.add_command(label="SAVE", command=SaveFile)
    M1.add_separator()
    M1.add_command(label="EXIT", command=Exit)
    MenuBar.add_cascade(label="FILE",menu=M1)
    # edit menu
    M2 = Menu(MenuBar, tearoff=0)
    M2.add_command(label="CUT", command=CutEdit)
    M2.add_command(label="COPY", command=CopyEdit)
    M2.add_command(label="PASTE", command=PasteEdit)
    MenuBar.add_cascade(label="EDIT", menu=M2)
    #help menu
    M3 = Menu(MenuBar, tearoff=0)
    M3.add_command(label="ABOUT", command=About)
    MenuBar.add_cascade(label="HELP", menu=M3)
    # scrollbar
    ScrollBar=Scrollbar(TextArea)
    ScrollBar.pack(side=RIGHT,fill="y")
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)

    root.config(menu=MenuBar)
    root.mainloop()
