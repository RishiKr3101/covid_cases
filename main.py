from tkinter import *
from covid import Covid
covid= Covid()

r = Tk()
r.title("Covid Cases check by Rishi")


def submit():
    cases= covid.get_status_by_country_name(country_code.get())
    c=0
    for x in cases:

        st= str(x) + ":" + str(cases[x])
        Label(r, text=st).grid(row=8+c, column=0, columnspan=2)
        c+=1
    country_code.delete(0, END)



country_code = Entry(r, width=30)
country_code.grid(row=0, column=1)
n_l = Label(r, text="Country").grid(row=0, column=0)

submit_b = Button(r, text="show", command=submit)
submit_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
r.mainloop()