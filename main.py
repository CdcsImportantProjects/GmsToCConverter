from tkinter import *
from tkinter import filedialog as fd
window = Tk()
def OpenCS():
    filetypes = (
        ('CSharp Files', '*.cs'),
        ('GameMakerLanguage Files', '*.gml'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        filetypes=filetypes,

    )
    print(filename)
    return filename
window.title("GML To CSharp Converter")
label = Label(window, text="Select a GML file")
label.grid(column=0, row=0)
btn = Button(window, text="Select file", command=lambda: print("File selected"))
btn.grid(column=0,row=1)
label2 = Label(window, text="Select a CS file")
label2.grid(column=0, row=2)
btn2 = Button(window, text="Select file", command=OpenCS)
btn2.grid(column=0,row=3)
window.mainloop()
