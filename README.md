
# Password Manager

A simple password manager built with Python and Tkinter. It helps you generate strong passwords, save them along with associated email and website information, and securely store them in a text file.

## Features

- **Random Password Generator**: Creates a strong password using letters, numbers, and symbols.
- **Save Passwords**: Stores passwords along with the website and email in a text file (`data.txt`).
- **Pre-Filled Default Email**: Allows setting a default email address to be pre-filled in the email field.
- **User-Friendly GUI**: Easy-to-use interface with input fields, buttons, and alerts.

## Setting the Default Email

To pre-fill the email field with a custom default email, you can set it in the code beforehand. Modify the following line in `main.py` (Line 73):

```python
email_input.insert(0, "my_email@example.com")
```

Replace `"my_email@example.com"` with your desired email address. For example:

```python
email_input.insert(0, "your_email@example.com")
```

## Requirements

- Python 3.x
- Required Python libraries:
  - `tkinter` (default in Python)
  - `pyperclip` (to copy passwords to clipboard)
- A `logo.png` file for the application logo.

## Installation

1. Clone or download the repository.
2. Install the required Python libraries (if not already installed):
   ```bash
   pip install pyperclip
   ```
3. Ensure the `logo.png` file is in the project directory.

## Usage

### Saving a Password
1. Enter the **Website**, **Email**, and **Password** fields.
   - Use the "Generate Password" button to create a strong password.
2. Click the **Add** button to save the data.
   - The data will be saved in `data.json` in the following format:
     ```json
     {
       "example.com": {
         "Email": "user@example.com",
         "Password": "securepassword123"
       }
     }
     ```

### Searching for a Password
1. Enter the **Website** name in the **Website** field.
2. Click the **Search** button to look up the saved password for that website.
   - If the password exists, it will display the email and password.
   - If the website is not found or the `data.json` file does not exist, an error message will be shown.


### Pre-Filling Default Email
To customize the default email, update the following line in the code (Line 88):
```python
email_input.insert(0, "your_email@example.com")

### Handling Missing Files
If the `data.json` file does not exist, the program will automatically create one when you save data. If the file is missing while trying to read or search for passwords, the following behavior occurs:

1. **Saving Data**:
   - If the `data.json` file doesn't exist, the program creates it and writes the new password data to it.
2. **Searching for Password**:
   - If the `data.json` file doesn't exist, an error message will be displayed:
   ```

## Files

- **main.py**: The main script for the application.
- **data.json**: Stores the saved passwords in a JSON format.
- **logo.png**: Logo displayed in the application.

## License

This project is licensed under the MIT License. Feel free to use and modify it.

---

### Author

Developed by Vedant1607.
