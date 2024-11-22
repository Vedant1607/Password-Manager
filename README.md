
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

1. Run the application:
   ```bash
   python main.py
   ```
2. The application window will open:
   - Enter the website name, email address, and generate a password.
   - Save the data by clicking the "Add" button.

3. Passwords are saved in the `data.txt` file in the following format:
   ```
   Website | Email | Password
   ```

## Files

- **main.py**: The main script for the application.
- **data.txt**: Stores the saved passwords.
- **logo.png**: Logo displayed in the application.

## License

This project is licensed under the MIT License. Feel free to use and modify it.

---

### Author

Developed by Vedant1607.
