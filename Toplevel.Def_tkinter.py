from tools import *
from tkinter import *
frm=form()

def test():
    frm =Toplevel()
    frm.grab_set()
button(frm,"ok",test).pack(pady=10)

frm.mainloop()



