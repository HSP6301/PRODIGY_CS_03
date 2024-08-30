# Password Complexity Checker

## Introduction

The **Password Complexity Checker** is a Python-based application developed using PyQt5 that helps users evaluate the strength of their passwords. The application checks the password against various security criteria, such as length, use of uppercase and lowercase letters, digits, and special characters. It provides feedback on the password's complexity level, ranging from "Very Weak" to "Very Strong." Additionally, the tool offers suggestions for improving weaker passwords, helping users create stronger and more secure passwords.

## Features

1. **Password Visibility Toggle**: The application includes a toggle button that allows users to show or hide the entered password, enhancing both usability and security.
   
2. **Password Complexity Assessment**: The application evaluates passwords based on five criteria—length, lowercase letters, uppercase letters, digits, and special characters. The result is displayed as a rating (Very Weak, Weak, Medium, Strong, Very Strong).

3. **Password Improvement Suggestions**: If the password does not meet the "Very Strong" criteria, the application provides suggestions on how to improve the password's strength.

4. **Password Mutation for Suggestions**: The application can generate random variations of the entered password, incorporating different characters to create stronger alternatives.

5. **Copy-to-Clipboard Functionality**: Users can easily copy any of the generated password suggestions to the clipboard for quick use.

6. **Error Handling**: The application includes comprehensive error handling to ensure users are informed when their input is invalid, such as when the password field is left empty or contains spaces.

## Usage

To use the Password Complexity Checker, simply launch the application, enter a password in the input field, and click "Check Password." The application will display the password's complexity rating and provide suggestions if needed. If you want to generate alternative password suggestions, click the "Generate Suggestions" button, and the application will display a list of suggested passwords that can be copied to the clipboard.

## Error Handling

The application includes the following error handling mechanisms:

1. **Empty Password Input**: If the password field is left empty, an error message box will appear, prompting the user to enter a password.
   
2. **Spaces in Password**: If the password contains spaces, an error message will alert the user that spaces are not allowed.

3. **Clipboard Copying**: The application provides a smooth experience when copying suggested passwords to the clipboard, with visual feedback when hovering over the "COPY" button.

## Requirements

To run the Password Complexity Checker, the following are required:

- **Python 3.x**: The application is written in Python, so a compatible version of Python 3.x is needed.
- **PyQt5**: The PyQt5 library is used for the graphical user interface. Install it using pip if it's not already installed:
  
  ```bash
  pip install PyQt5
  ```
