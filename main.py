from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Generating random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # Randomly select characters for the password
    random_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    
    # Combine all the selected characters and shuffle them
    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)
    
    password = "".join(password_list) # Join the characters to create the final password
    password_input.insert(0,password) # Insert the password in the password_input field
    pyperclip.copy(password) # Copy the password to the clipboard

# Saving data
def save_data():
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()
    
    data_dict = {
        user_website: {
            "Email": user_email,
            "Password": user_password
        }
    }
    
    # Check if any field is empty
    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Error", message="You cannot leave any field empty")
    else:
        # Ask the user for confirmation before saving data
        answer = messagebox.askyesno(title="Password Manager",message="Do you want to save it?")
        if answer:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    data = json.dump(data_dict, data_file, indent=4)
            else:
                data.update(data_dict)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # Clear the input fields after saving
                website_input.delete(0,END)
                password_input.delete(0,END)

# Find to find password in data file
def find_password():
    user_website = website_input.get()
    
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError: # Shows an error if data.json file doesn't exist
        messagebox.showerror(title="Error", message="No data file exists.")
    else:
        if user_website in data:
            # if password is present in data, then it shows to the user
            messagebox.showinfo(title=f"{user_website}", message=f"Email: {data[user_website]["Email"]}\nPassword: {data[user_website]["Password"]}")
        else:
            # if no password present for the searched website, then shows an error
            messagebox.showerror(title="Error", message=f"No password for {user_website} saved")

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20,bg="black")

# Canvas
canvas = Canvas(width=200,height=200,bg="black", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(90,100,image=logo)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website :",fg="white",bg="black")
website_label.grid(row=1,column=0)

email_label = Label(text="Email :",fg="white",bg="black")
email_label.grid(row=2, column=0)

password_label = Label(text="Password :",fg="white",bg="black")
password_label.grid(row=3,column=0)

# Entries
website_input = Entry(width=17)
website_input.grid(row=1,column=1)
website_input.focus() # Automaticall focus this input field

email_input = Entry(width=25)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"your_email@example.com") # Pre-fill with the default email

password_input = Entry(width=25)
password_input.grid(row=3,column=1,columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password,fg="white",bg="black")
generate_password_button.grid(row=4, column=1)

add_password = Button(text="Add",command=save_data, width=40, padx=10,fg="white",bg="black")
add_password.grid(row=5, column=0, columnspan=3)

search_password = Button(text="Search",bg="black",fg="white",command=find_password)
search_password.grid(row=1,column=2)

window.mainloop()