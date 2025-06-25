
from tkinter import *


def button_click():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program with Tkinter")
window.minsize(width=600, height=400)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am Philip", font=("Arial", 24))
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

button = Button(text="Click Me Again", command=button_click)
button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=3, row=2)


window.mainloop()
