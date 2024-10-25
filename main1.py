from tkinter import *
window=Tk()
window.title("Denotes Calculator")
window.geometry("600x600")

label= Label(window, text="Enter you total amount", bg="light grey")
entry = Entry()
lbl = Label(window, text="Here the notes for each detnotation")

l1= Label(window, text= "1000")
l2 = Label(window, text= "500")
l3= Label(window, text= "100")

t1= Entry(window)
t2= Entry(window)
t3= Entry(window)

def calculator():
    try:
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    except ValueError:
        print("enter proper value")



btn=Button(window, text="Calcute", command= calculator)

label.place(x=230, y=50 )

entry.place(x=200, y=80 )

btn.place(x=240, y=120 )

lbl.place(x=140, y=170 )

l1.place(x=180, y=200 )

l2.place(x=180, y=230 )

l3.place(x=180, y=260 )

t1.place(x=270, y=200 )

t2.place(x=270, y=230 )

t3.place(x=270, y=260)

window.mainloop()