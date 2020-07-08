import json
from difflib import get_close_matches
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

data = json.load(open("resources/data.json"))

window = Tk()
window.title("My Dictionary")
window.geometry('1000x600')
#window.iconbitmap(r"resources/logo.png")


def translate(word):
    word = word.lower()
    if word in data:
        out = data[word]
        t1.delete(1.0, END)
        t1.config(fg="#fff")
        if type(out) == list:
            for item in out:
                t1.insert(END, f"- {item} \n\n")
        else:
            t1.insert(END, out)
    elif word.title() in data:
        out = data[word.title()]
        t1.delete(1.0, END)
        t1.config(fg="#fff")
        if type(out) == list:
            for item in out:
                t1.insert(END, f"- {item} \n\n")
        else:
            t1.insert(END, out)
    elif word.upper() in data:
        out = data[word.upper()]
        t1.delete(1.0, END)
        t1.config(fg="#fff")
        if type(out) == list:
            for item in out:
                t1.insert(END, f"- {item}\n\n")
        else:
            t1.insert(END, out)
    elif len(get_close_matches(word, data.keys())) > 0:
        t1.config(fg="orange")
        t1.delete(1.0, END)
        out = data[get_close_matches(word, data.keys())[0]]
        t1.insert(END, f"Did you mean {get_close_matches(word, data.keys())[0]}:\n")
        if type(out) == list:
            for item in out:
                t1.insert(END, f"- {item} \n\n")
        else:
            t1.insert(END, f"- {out} \n\n")
    else:
        t1.config(fg="red")
        t1.delete(1.0, END)
        t1.insert(END, "The word doesn't exist. Please check it again.")


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo


image = Image.open('resources/back1.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

#input(Entry)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, bg="#4f5257", fg="black", justify=CENTER, font=('courier', 30, 'bold'))
e1.place(relx=.185, rely=0.30, relwidth=.63, relheight=.082)

#search botton
b1 = Button(window, text="Search", bg="black", fg="white", font=('Arial Rounded MT', 20, 'bold'), command=lambda: translate(e1_value.get()))
b1.place(relx=.40, rely=.45, relwidth=.2, relheight=.052)

#output box
t1 = Text(window, fg="#fff", relief=FLAT, bg="#444444", font=('Arial Rounded MT', 12, 'bold'))
t1.place(relx=.185, rely=.60, relwidth=.63, relheight=.30)
window.mainloop()