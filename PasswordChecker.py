import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Resize the main window to a more square shape
        self.resize(500, 350)

    def initUI(self):
        self.setWindowTitle('Password Complexity Checker')

        layout = QVBoxLayout()

        # Horizontal layout for password input and show button
        h_layout = QHBoxLayout()

        # Password input field
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Initially hide the password
        self.password_input.setPlaceholderText('Enter your password')
        h_layout.addWidget(self.password_input)

        # Show/Hide password button
        self.show_button = QPushButton('Show', self)
        self.show_button.setCheckable(True)
        self.show_button.toggled.connect(self.toggle_password_visibility)
        h_layout.addWidget(self.show_button)

        layout.addLayout(h_layout)

        # Check button
        self.check_button = QPushButton('Check Password', self)
        self.check_button.clicked.connect(self.check_password)
        layout.addWidget(self.check_button)

        # Result label
        self.result_label = QLabel('', self)
        layout.addWidget(self.result_label)

        # Suggestion label with word wrap enabled
        self.suggestion_label = QLabel('', self)
        self.suggestion_label.setWordWrap(True)
        self.suggestion_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(self.suggestion_label)

        # List widget for password suggestions
        self.suggestions_list = QListWidget(self)
        layout.addWidget(self.suggestions_list)

        # Button to generate password suggestions
        self.generate_suggestions_button = QPushButton('Generate Suggestions', self)
        self.generate_suggestions_button.clicked.connect(self.generate_suggestions)
        layout.addWidget(self.generate_suggestions_button)

        self.setLayout(layout)

    def toggle_password_visibility(self, checked):
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)  # Show the password
            self.show_button.setText('Hide')
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  # Hide the password
            self.show_button.setText('Show')

    def check_password(self):
        password = self.password_input.text()

        # Input validation
        if not password:
            self.show_error_message("Input Error", "Password cannot be empty.")
            return

        if " " in password:
            self.show_error_message("Input Error", "Password cannot contain spaces.")
            return

        complexity = self.calculate_complexity(password)
        self.result_label.setText(complexity)

        if complexity != "Very Strong":
            suggestion = self.generate_suggestion(password)
            self.suggestion_label.setText(f"Suggestion: {suggestion}")
        else:
            self.suggestion_label.setText('')

    def show_error_message(self, title, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle(title)
        error_msg.setText(message)
        error_msg.exec_()

    def calculate_complexity(self, password):
        # Criteria for password complexity
        length_criteria = len(password) >= 8
        lowercase_criteria = any(char.islower() for char in password)
        uppercase_criteria = any(char.isupper() for char in password)
        digit_criteria = any(char.isdigit() for char in password)
        special_criteria = any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?\\|`~' for char in password)

        # Evaluating password complexity
        complexity_level = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria])

        if complexity_level == 5:
            return "Very Strong"
        elif complexity_level == 4:
            return "Strong"
        elif complexity_level == 3:
            return "Medium"
        elif complexity_level == 2:
            return "Weak"
        else:
            return "Very Weak"

    def generate_suggestion(self, password):
        # Suggestions to improve password strength
        suggestions = []

        if len(password) < 8:
            suggestions.append("Increase the length to at least 8 characters.")

        if not any(char.islower() for char in password):
            suggestions.append("Add lowercase letters.")

        if not any(char.isupper() for char in password):
            suggestions.append("Add uppercase letters.")

        if not any(char.isdigit() for char in password):
            suggestions.append("Include digits.")

        if not any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?\\|`~' for char in password):
            suggestions.append("Use special characters like !@#$%^&*")

        if not suggestions:
            suggestions.append("Try combining different types of characters.")

        return " ".join(suggestions)

    def generate_suggestions(self):
        current_password = self.password_input.text()

        # Input validation for Generate Suggestions
        if not current_password:
            self.show_error_message("Input Error", "Password cannot be empty.")
            return

        if " " in current_password:
            self.show_error_message("Input Error", "Password cannot contain spaces.")
            return

        self.suggestions_list.clear()

        if current_password:
            suggestions = self.generate_password_suggestions(current_password)
            for suggestion in suggestions:
                self.add_suggestion_item(suggestion)

    def generate_password_suggestions(self, base_password, num_suggestions=3):
        suggestions = []
        for _ in range(num_suggestions):
            suggestion = self.mutate_password(base_password)
            suggestions.append(suggestion)
        return suggestions

    def mutate_password(self, password):
        # Randomly capitalize letters
        password = ''.join(random.choice([c.upper(), c.lower()]) if c.isalpha() else c for c in password)
        
        # Randomly replace some characters with numbers or symbols
        replacements = {
            'a': '@', 's': '$', 'i': '1', 'o': '0', 'e': '3', 'l': '!', 't': '7'
        }
        password = ''.join(replacements.get(c.lower(), c) if random.random() < 0.3 else c for c in password)

        # Add a random number or symbol at the end
        password += random.choice(string.digits + string.punctuation)
        
        return password

    def add_suggestion_item(self, suggestion):
        item_widget = QWidget()
        item_layout = QHBoxLayout()

        # Suggestion label
        suggestion_label = QLabel(suggestion)

        # Copy button
        copy_button = QPushButton('COPY')
        copy_button.setFixedWidth(80)
        copy_button.setVisible(False)
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(suggestion))

        # Add widgets to layout
        item_layout.addWidget(suggestion_label)
        item_layout.addWidget(copy_button)
        item_layout.addStretch()
        item_widget.setLayout(item_layout)

        # Add item to list
        list_item = QListWidgetItem(self.suggestions_list)
        list_item.setSizeHint(item_widget.sizeHint())
        self.suggestions_list.addItem(list_item)
        self.suggestions_list.setItemWidget(list_item, item_widget)

        # Show copy button on hover
        item_widget.enterEvent = lambda event: copy_button.setVisible(True)
        item_widget.leaveEvent = lambda event: copy_button.setVisible(False)

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checker = PasswordChecker()
    checker.show()
    sys.exit(app.exec_())
