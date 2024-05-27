from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   website_data= website_entry.get()
   email_data= email_entry.get()
   password_data=password_entry.get()
   new_data={
       website_data: {
           "email": email_data,
           "password": password_data,
       }
   }

   if len(website_data)==0 or len(password_data)==0:
       messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty !")

   else:
       try:
           with open(file="data.json" ,mode="r") as data_file:
               data = json.load(data_file)

       except FileNotFoundError:
           with open(file="data.json" , mode="w") as data_file:
               json.dump(new_data,data_file,indent=4)
       else:
           data.update(new_data)
           with open(file="data.json" ,mode="w") as data_file:
               json.dump(data,data_file,indent=4)
       finally:
           website_entry.delete(0,END)
           password_entry.delete(0,END)

#------------------------------------search button---------------------------------
def find_password():
    website=website_entry.get()
    try:
        with open(file="data.json" , mode="r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
         messagebox.showinfo(title="Error",message="No data file found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"email :{email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist")








# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
myimg=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=myimg)
canvas.grid(column=1,row=0)

website_label=Label(text="Website :")
website_label.grid(column=0,row=1)


website_entry=Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

username_label=Label(text="Username :")
username_label.grid(column=0,row=2)

email_entry=Entry(width=40)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "default@gmail.com")

password_label=Label(text="Email/Password :")
password_label.grid(column=0,row=3)

password_entry=Entry(width=22)
password_entry.grid(column=1, row=3, columnspan=1)


passgen_button=Button(text="Generate Password", command=generate_password)
passgen_button.grid(column=2, row=3)

search_button=Button(text="Search",width=13,command=find_password )
search_button.grid(column=2, row=1)

add_button=Button(text="Add",width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2)






window.mainloop()