from tkinter import *
import pyperclip
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate():
    nr_letters=random.randint(8,10)
    nr_numbers=random.randint(2,4)
    nr_symbols=random.randint(2,4)

    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    password_number=[random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]

    password_list=password_letter+password_number+password_symbols
    random.shuffle(password_list)
    

    Password= ""
    for char in password_list:
     Password+=char
    Password_entry.insert(index=0,string=f"{Password}")
    pyperclip.copy(Password) # directly copy the text/password
     

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    global data
    email=Email_entry.get()
    website=Web_entry.get()
    passd=Password_entry.get()
    new_data={website:{"email":email,
                       "password":passd}}
    if len(website)<1 or len(email)<1 or len(passd)<1:
       messagebox.showinfo(title="oops" , message="Please fill in all details")

    else:

        is_ok=messagebox.askokcancel(title=website,message=f"Do you want to save this ?\n Email:{email}\n Password:{passd}")
        if is_ok:
            try:
                with open("data.json","r") as file:
                 data=json.load(file)
                 data.update(new_data)
            except:
                with open("data.json","w") as file:
                   json.dump(new_data,file,indent=4)      
            else:
               with open("data.json","w") as file:
                json.dump(data,file,indent=4)
                  
            Web_entry.delete(0,END)
            Password_entry.delete(0,END)

def search():
    try:
       with open("data.json","r") as file:
        data=json.load(file)
    except FileNotFoundError:
       messagebox.showinfo(message="No such file found")
          
    else:
     for key in data:
        if key==Web_entry.get():
         e=data[key]["email"]
         p=data[key]["password"]
         messagebox.showinfo(message=f"Email :{e}\nPassword: {p}")
        else:
             messagebox.showinfo(message="No such data found")
    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.minsize(width=240,height=240)
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
my_pass=PhotoImage(file="logo.png")
my_img=canvas.create_image(100,100,image=my_pass)
canvas.grid(column=1,row=0)

window.config(padx=20)

Website_label=Label(text="Website:",fg="black")
Website_label.grid(column=0,row=1)

Web_entry=Entry(width=35)
Web_entry.grid(row=1,column=1,sticky=EW)
Web_entry.focus()

Email_label=Label(text="Email:")
Email_label.grid(row=2,column=0)

Email_entry=Entry(width=35)
Email_entry.grid(row=2,column=1,columnspan=2,sticky=EW)
Email_entry.insert(index=0,string="ankitdevkota107@gmail.com")

Password_label=Label(text="Password:")
Password_label.grid(column=0,row=3)

Password_entry=Entry()

Password_entry.grid(column=1,row=3,sticky=EW)

generate=Button(text="Generate-password",command=generate)
generate.grid(column=2,row=3,sticky=EW)

    

search_button=Button(text="Search",command=search)
search_button.grid(row=1,column=2,sticky=EW)






Add_button=Button(text="ADD",command=add)
Add_button.grid(column=1,row=4,columnspan=2,sticky=EW)




















window.mainloop()