from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(100,150)
window.configure(padx=30,pady=30)
def convert():
    miles = int(entry.get())
    miles = miles * 1.852
    label_answer.configure(text=miles)


entry = Entry(width=10)
entry.grid(row=0,column=1)

label_text_miles = Label(text="Miles")
label_text_miles.grid(row=0,column=2)


label_text_is_eq = Label(text="is equal to")
label_text_is_eq.grid(row=1,column=0)


label_answer = Label(text='0')
label_answer.grid(row=1,column=1)

label_text_km = Label(text="Km")
label_text_km.grid(row=1,column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2,column=1)


window.mainloop()

