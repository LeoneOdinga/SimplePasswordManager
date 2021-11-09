
from tkinter import *
from tkinter import messagebox
from SimplePasswordGenerator import randomPasswords
import pyperclip
import json

# generate random passwords when button clicked

def autoGeneratePassword():
    generatedPassword = randomPasswords(5,3,3)
    passwordEntry.insert(0,generatedPassword)
    pyperclip.copy(generatedPassword)

#function to save the password

def save():

    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    new_data = {
        website:{

            "email":email,
            "password":password,

        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops",message="Do Not Leave Any Fields Empty")

    else:
        is_okay = messagebox.askokcancel(title=f"Website: {website}",
                                         message=f"You Entered the Following Details: \n\nEmail/Username: {email}\n\nPassword: {password} \n\nClick OK to save changes or cancel")

        if is_okay:

            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:

                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # saving the updated data

                    json.dump(data, data_file, indent=4)
            finally:
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)

#function to search json file for website and password combination

def find_password():

    website = websiteEntry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error Opening File!", message="No File Data Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            pyperclip.copy(password)
            messagebox.showinfo(title=website,message=f"Email: {email} \nYour Password Has Been Copied To The Clip Board\nProceed And Paste!")
        else:
            messagebox.showinfo(title="Ooops",message="We Could Not Find the Item You requested For!")


#================================    UI Set-Up   ===============================================

window = Tk()
window.title("Password Manager")
window.minsize(width=700,height=550)
window.maxsize(width=700,height=550)
window.config(padx=20,pady=20)
canvas = Canvas(height=400,width=400)
window.config(bg="light yellow")
logo_image = PhotoImage(file="PasswordManagerlogo.png")
canvas.create_image(200,200,image=logo_image)
canvas.grid(row=0,column=1)

#labels

websiteLabel = Label(text="Website:",font=("Ariel,12,bold"))
websiteLabel.grid(row=1,column=0)
websiteLabel.config(fg="grey")

emailLabel = Label(text="Email/Username:",font=("Ariel,12,bold"))
emailLabel.grid(row=2,column=0)

passwordLabel = Label(text="Password:",font=("Ariel,12,bold"))
passwordLabel.grid(row=3,column=0)

#Entries

websiteEntry = Entry(width=21)
websiteEntry.place(x=158,y=409)
websiteEntry.focus()

emailEntry = Entry(width=35)
emailEntry.place(x=158,y=440)
emailEntry.insert(0,"leoneodinga41@gmail.com")

passwordEntry = Entry(width=21)
passwordEntry.place(x=158,y=470)

#buttons

generatePasswordButton = Button(text="Generate Password",command=autoGeneratePassword)
generatePasswordButton.place(x=290,y=467)

addButton = Button(text="Add",width=36,command =save)
addButton.place(x=140,y=500)

searchButton = Button(text="Search",width=15,command = find_password)
searchButton.place(x=290,y=409)

window.mainloop()