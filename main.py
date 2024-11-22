from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    
    # Check if any field is empty
    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Error", message="You cannot leave any field empty")
    else:
        # Ask the user for confirmation before saving data
        answer = messagebox.askyesno(title="Password Manager",message="Do you want to save it?")
        if answer:
            with open("data.txt",'a') as data:
                data.write(f"{user_website} | {user_email} | {user_password}\n")
            
            # Clear the input fields after saving
            website_input.delete(0,END)
            password_input.delete(0,END)

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
website_input = Entry(width=30)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus() # Automaticall focus this input field

email_input = Entry(width=30)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"your_email@example.com") # Pre-fill with the default email

password_input = Entry(width=30)
password_input.grid(row=3,column=1,columnspan=2)

# Buttons
generate_password = Button(text="Generate Password",command=generate_password,fg="white",bg="black")
generate_password.grid(row=4, column=1)

add = Button(text="Add",command=save_data, width=40, padx=10,fg="white",bg="black")
add.grid(row=5, column=0, columnspan=3)

window.mainloop()